<#
.SYNOPSIS
  Build the simplicial_vector_calculus.pdf from its markdown source.

.DESCRIPTION
  Converts `simplicial_vector_calculus.md` to LaTeX via pandoc, then compiles
  a PDF with XeLaTeX (via latexmk). Outputs `simplicial_vector_calculus.pdf`
  in the project root. Intermediate files live under `build/`.

.PARAMETER Source
  Markdown source file (default: simplicial_vector_calculus.md).

.PARAMETER Clean
  Wipe the `build/` directory before building (forces a fresh run).

.PARAMETER SkipPdf
  Only generate the `.tex`; do not invoke latexmk. Useful for debugging.

.EXAMPLE
  pwsh ./build.ps1

.EXAMPLE
  pwsh ./build.ps1 -Clean
#>
[CmdletBinding()]
param(
    [string]$Source  = 'simplicial_vector_calculus.md',
    [switch]$Clean,
    [switch]$SkipPdf
)

$ErrorActionPreference = 'Stop'

# --- Paths -------------------------------------------------------------------
$root     = Split-Path -Parent $PSCommandPath
$srcPath  = Join-Path $root $Source
if (-not (Test-Path $srcPath)) { throw "Source not found: $srcPath" }

$buildDir = Join-Path $root 'build'
$latexDir = Join-Path $root 'latex'
$preamble = Join-Path $latexDir 'preamble.tex'
if (-not (Test-Path $preamble)) { throw "Preamble not found: $preamble" }

$pdfName  = [System.IO.Path]::ChangeExtension($Source, '.pdf')
$finalPdf = Join-Path $root $pdfName

if ($Clean -and (Test-Path $buildDir)) {
    # Preserve build/utils (shared maintenance scripts); wipe the rest.
    Get-ChildItem -LiteralPath $buildDir -Force |
        Where-Object { $_.Name -ne 'utils' } | Remove-Item -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

# --- Locate tools ------------------------------------------------------------
# Refresh PATH from Machine + User so a freshly-installed pandoc/miktex is found
# without opening a new shell.
$env:PATH = [System.Environment]::GetEnvironmentVariable('PATH', 'Machine') + ';' +
            [System.Environment]::GetEnvironmentVariable('PATH', 'User')   + ';' +
            $env:PATH

function Get-Tool {
    param([string]$Name, [string[]]$Fallback = @())
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    foreach ($p in $Fallback) {
        if (Test-Path $p) { return $p }
    }
    throw "Tool not found on PATH: $Name (install via: winget install JohnMacFarlane.Pandoc; winget install MiKTeX.MiKTeX)"
}

$pandoc  = Get-Tool 'pandoc'  @("$env:LOCALAPPDATA\Pandoc\pandoc.exe")
$latexmk = Get-Tool 'latexmk' @("$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\latexmk.exe")

# Make sure xelatex is resolvable by latexmk (it is, if miktex is on PATH)
Get-Tool 'xelatex' @("$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\xelatex.exe") | Out-Null

Write-Host ("Using pandoc : {0}" -f $pandoc)
Write-Host ("Using latexmk: {0}" -f $latexmk)

# --- Pre-process: strip the markdown title block ----------------------------
# The MD source carries a human-readable title block (lines 1..N up to the
# first `---` horizontal rule). Pandoc gets a pruned body plus explicit
# --metadata title/author/date so the PDF has a native \maketitle + abstract.
$lines = Get-Content $srcPath -Encoding utf8

# Parse title / author / date from the source
$title  = ($lines | Where-Object { $_ -match '^# \S' } | Select-Object -First 1) -replace '^#\s+',''
if (-not $title) { throw "Could not parse title (H1) from $Source" }

# Derive a clean PDF-metadata version of the title by stripping any raw LaTeX
# commands the displayed title carries (e.g. \heb{ל} for the font-switched
# Hebrew letter): pandoc's default title-meta extraction drops the command
# *and* its argument, which would erase the letter from the metadata too.
# We collapse \heb{X} -> X so the metadata keeps the literal character.
$titleMeta = $title -replace '\\heb(?:\[[^\]]*\])?\{([^}]*)\}', '$1'

$authorLine = ($lines | Where-Object { $_ -match '^\*\*[^*]+\*\*$' } | Select-Object -First 1)
if (-not $authorLine) { throw "Could not parse author (**...**) from $Source" }
$author = $authorLine -replace '^\*\*|\*\*$',''
$authorMeta = $author

# Optional affiliation: the first single-italic line that is neither an
# email (`@`) nor a date (`Month DD, YYYY`). If present, append it to the
# author on a new line on the title page via raw LaTeX (`\\ \textit{...}`).
# Pandoc's default markdown variant has raw_tex enabled, so the commands
# survive into the output .tex untouched.
$affiliationLine = ($lines | Where-Object {
    $_ -match '^\*[^*@]+\*$' -and $_ -notmatch '\d{4}\*$'
} | Select-Object -First 1)
if ($affiliationLine) {
    $affiliation = $affiliationLine -replace '^\*|\*$',''
    # \newline (not \\) so pandoc's metadata-as-markdown parser, which
    # treats `\\` as the markdown escape for a literal backslash, doesn't
    # render the line break as `\textbackslash{}`.
    $author      = "$author\newline\textit{$affiliation}"
    $authorMeta  = "$authorMeta ($affiliation)"
}

# Date: take the date field we wrote during authoring.
# Accepts the plain form "*Month DD, YYYY*" OR an enriched preprint form
# such as "*Preprint, version 1.0 — May 21, 2026*" — any italic line that
# ends with "Month DD, YYYY".
$dateLine = ($lines | Where-Object { $_ -match '^\*[^*]*[A-Z][a-z]+\s+\d{1,2},\s+\d{4}\*$' } | Select-Object -First 1)
if (-not $dateLine) { throw "Could not parse date (*Month DD, YYYY*) from $Source" }
$date = $dateLine -replace '^\*|\*$',''

# If the date line carries a "Preprint, version X" prefix, surface the whole
# date string (version + date) as the PDF subject so it lands in the document
# metadata alongside the title-page rendering of the date.
$subject = $null
if ($date -match '^Preprint') {
    $subject = $date
}

# Find the first `---` horizontal rule that closes the title block.
$hrIdx = $null
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^---\s*$') { $hrIdx = $i; break }
}
if ($null -eq $hrIdx) { throw "Could not find the title-block terminator (first '---' line)" }

# Body = everything after the first '---' horizontal rule
$body = ($lines[($hrIdx + 1)..($lines.Count - 1)] -join "`n")

# Extract abstract (between '## Abstract' and the next '---')
$abstract = $null
$absStart = $null; $absEnd = $null
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($null -eq $absStart -and $lines[$i] -match '^##\s+Abstract\s*$') { $absStart = $i + 1; continue }
    if ($null -ne $absStart -and $lines[$i] -match '^---\s*$')           { $absEnd   = $i - 1; break }
}
if ($null -ne $absStart -and $null -ne $absEnd -and $absEnd -ge $absStart) {
    $abstract = ($lines[$absStart..$absEnd] -join "`n").Trim()
}

# Strip the original Abstract block from the body so it isn't duplicated
if ($null -ne $absStart) {
    $preStart = ($lines[0..($absStart - 2)])   # up to and including `## Abstract` line? no: stop before it
    # Rebuild body excluding the abstract block (## Abstract..closing ---)
    $keep = @()
    $skipping = $false
    for ($i = $hrIdx + 1; $i -lt $lines.Count; $i++) {
        if (-not $skipping -and $lines[$i] -match '^##\s+Abstract\s*$') { $skipping = $true; continue }
        if ($skipping -and $lines[$i] -match '^---\s*$')                { $skipping = $false; continue }
        if ($skipping) { continue }
        $keep += $lines[$i]
    }
    $body = ($keep -join "`n").TrimStart("`r","`n")
}

# YAML front matter for pandoc.
# Backslashes (raw LaTeX commands like \heb{...}) and double-quotes both need
# escaping inside YAML's double-quoted scalars; .Replace() is used so that
# regex metacharacters in the input have no effect.
function Esc-Yaml([string]$s) {
    return $s.Replace('\','\\').Replace('"','\"')
}

$subjectLine = if ($subject) { 'subject: "{0}"' -f (Esc-Yaml $subject) } else { '' }

$yaml = @"
---
title: "$(Esc-Yaml $title)"
title-meta: "$(Esc-Yaml $titleMeta)"
author: "$(Esc-Yaml $author)"
author-meta: "$(Esc-Yaml $authorMeta)"
date: "$(Esc-Yaml $date)"
$subjectLine
abstract: |
$(
    if ($abstract) {
        ($abstract -split "`n" | ForEach-Object { '  ' + $_ }) -join "`n"
    } else { '  ' }
)
---

"@

$preppedMd = Join-Path $buildDir 'paper.md'
Set-Content -Path $preppedMd -Value ($yaml + $body) -Encoding utf8
Write-Host ("Wrote prepped markdown: {0}" -f $preppedMd)

# --- Pandoc: markdown -> standalone .tex ------------------------------------
$texFile = Join-Path $buildDir 'paper.tex'

$pandocArgs = @(
    $preppedMd,
    '--from=markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+smart+implicit_figures+autolink_bare_uris',
    '--to=latex',
    "--output=$texFile",
    '--standalone',
    '--wrap=preserve',
    '--pdf-engine=xelatex',
    '--top-level-division=section',
    '--table-of-contents',
    '--toc-depth=3',
    "--include-in-header=$preamble",
    '-V', 'documentclass=article',
    '-V', 'classoption=11pt',
    '-V', 'papersize=letter',
    '-V', 'geometry:margin=0.7in',
    '-V', 'colorlinks=true',
    '-V', 'mainfont=Latin Modern Roman',
    '-V', 'mathfont=Latin Modern Math',
    '-V', 'monofont=Latin Modern Mono'
)

Write-Host 'Running pandoc...'
& $pandoc @pandocArgs
if ($LASTEXITCODE -ne 0) { throw "pandoc failed with exit code $LASTEXITCODE" }
Write-Host ("Wrote TeX: {0}" -f $texFile)

if ($SkipPdf) {
    Write-Host '-SkipPdf specified; stopping before PDF build.'
    return
}

# --- latexmk: .tex -> .pdf --------------------------------------------------
Write-Host 'Running latexmk (xelatex)...'
Push-Location $buildDir
try {
    & $latexmk '-xelatex' '-interaction=nonstopmode' '-halt-on-error' '-file-line-error' 'paper.tex'
    if ($LASTEXITCODE -ne 0) {
        throw "latexmk failed with exit code $LASTEXITCODE (see $buildDir\paper.log)"
    }
} finally {
    Pop-Location
}

# --- Publish ---------------------------------------------------------------
$builtPdf = Join-Path $buildDir 'paper.pdf'
if (-not (Test-Path $builtPdf)) { throw "Expected PDF not produced: $builtPdf" }
Copy-Item $builtPdf $finalPdf -Force

$info = Get-Item $finalPdf
Write-Host ''
Write-Host ('OK   {0}  ({1:N0} KB)' -f $finalPdf, ($info.Length / 1KB))
