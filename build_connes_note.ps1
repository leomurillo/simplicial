<#
.SYNOPSIS
  One-off build of ExactVerification-SemilocalWeilForm-Note-v2.md -> .pdf
  Output lands in C:\Projects\Connes\ alongside the source .md.
#>
[CmdletBinding()]
param([switch]$SkipPdf)

$ErrorActionPreference = 'Stop'

$simplicial = Split-Path -Parent $PSCommandPath
$connesDir  = 'C:\Projects\Connes'
$source     = Join-Path $connesDir 'ExactVerification-SemilocalWeilForm-Note-v2.md'
$preamble   = Join-Path $simplicial 'latex\preamble.tex'
$buildDir   = Join-Path $simplicial 'build_connes'

foreach ($p in @($source, $preamble)) {
    if (-not (Test-Path $p)) { throw "Required file not found: $p" }
}
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

# ---- Refresh PATH so freshly installed tools are found ----------------------
$env:PATH = [System.Environment]::GetEnvironmentVariable('PATH', 'Machine') + ';' +
            [System.Environment]::GetEnvironmentVariable('PATH', 'User')   + ';' +
            $env:PATH

function Get-Tool {
    param([string]$Name, [string[]]$Fallback = @())
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    foreach ($p in $Fallback) { if (Test-Path $p) { return $p } }
    throw "Tool not found on PATH: $Name"
}

$pandoc  = Get-Tool 'pandoc'  @("$env:LOCALAPPDATA\Pandoc\pandoc.exe")
$latexmk = Get-Tool 'latexmk' @("$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\latexmk.exe")
Get-Tool 'xelatex' @("$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\xelatex.exe") | Out-Null

Write-Host "Using pandoc : $pandoc"
Write-Host "Using latexmk: $latexmk"

# ---- Parse source -----------------------------------------------------------
$lines = Get-Content $source -Encoding utf8

# Title: first H1
$title = ($lines | Where-Object { $_ -match '^#\s+\S' } | Select-Object -First 1) -replace '^#\s+', ''
if (-not $title) { throw 'Could not find H1 title' }

# Author: first **...**
$authorLine = ($lines | Where-Object { $_ -match '^\*\*[^*]+\*\*$' } | Select-Object -First 1)
if (-not $authorLine) { throw 'Could not find **author** line' }
$author = $authorLine -replace '^\*\*|\*\*$', ''

# Affiliation: first single-italic line (even with @)
$affiliationLine = ($lines | Where-Object { $_ -match '^\*[^*]+\*$' -and $_ -notmatch '\d{4}\*$' } | Select-Object -First 1)
$affiliation = if ($affiliationLine) { $affiliationLine -replace '^\*|\*$', '' } else { '' }

# Date: first italic line ending with a 4-digit year (flexible — accepts "June 2026")
$dateLine = ($lines | Where-Object { $_ -match '^\*[^*]+\d{4}\*$' } | Select-Object -First 1)
if (-not $dateLine) { throw 'Could not find italic date line' }
$date = $dateLine -replace '^\*|\*$', ''

# Version note: second **...**  (e.g. "Note, version 2 ...")
$versionLine = ($lines | Where-Object { $_ -match '^\*\*[^*]+\*\*$' } | Select-Object -Skip 1 | Select-Object -First 1)
$versionNote = if ($versionLine) { $versionLine -replace '^\*\*|\*\*$', '' } else { '' }

# Abstract: lines between ## Abstract and the next ---
$inAbstract  = $false
$absLines    = @()
foreach ($line in $lines) {
    if ($line -match '^##\s+Abstract\s*$')              { $inAbstract = $true;  continue }
    if ($inAbstract -and $line -match '^---\s*$')       { $inAbstract = $false; continue }
    if ($inAbstract)                                    { $absLines  += $line  }
}
$abstract = ($absLines -join "`n").Trim()

# Body: everything after the second --- (abstract closes it)
$dashCount = 0
$bodyLines = @()
$inBody    = $false
foreach ($line in $lines) {
    if (-not $inBody) {
        if ($line -match '^---\s*$') {
            $dashCount++
            if ($dashCount -ge 2) { $inBody = $true }
        }
        continue
    }
    $bodyLines += $line
}
$body = ($bodyLines -join "`n").TrimStart("`r", "`n")

# ---- Build YAML front matter ------------------------------------------------
function Esc-Yaml([string]$s) {
    $s.Replace('\', '\\').Replace('"', '\"')
}

$titleEsc = Esc-Yaml $title
# Clean ASCII title for PDF metadata (strip the math fragment)
$titleMeta = 'Exact-Arithmetic Verification of the Spectral Realization by Zeta-Cycles'

$authorStr = if ($affiliation) {
    "$author\newline\textit{$affiliation}"
} else {
    $author
}
$authorEsc  = Esc-Yaml $authorStr
$authorMeta = if ($affiliation) { "$author ($affiliation)" } else { $author }

$abstractYaml = ($abstract -split "`n" | ForEach-Object { '  ' + $_ }) -join "`n"

# Version note injected at top of body as an italic paragraph
$bodyPrefix = if ($versionNote) {
    "*$versionNote*`n`n"
} else { '' }

$yamlHeader = "---`ntitle: `"$titleEsc`"`ntitle-meta: `"$titleMeta`"`nauthor: `"$authorEsc`"`nauthor-meta: `"$authorMeta`"`ndate: `"$date`"`nabstract: |`n$abstractYaml`n---`n`n"

$preppedMd = Join-Path $buildDir 'paper.md'
Set-Content -Path $preppedMd -Value ($yamlHeader + $bodyPrefix + $body) -Encoding utf8
Write-Host "Wrote prepped markdown: $preppedMd"

# Extra macros not in the shared preamble (note-specific commands)
$extraMacros = Join-Path $buildDir 'extra_macros.tex'
Set-Content -Path $extraMacros -Value '\providecommand{\R}{\mathrm{R}}' -Encoding utf8

# ---- Pandoc: markdown -> .tex -----------------------------------------------
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
    "--include-in-header=$preamble",
    "--include-in-header=$extraMacros",
    '-V', 'documentclass=article',
    '-V', 'classoption=11pt',
    '-V', 'papersize=letter',
    '-V', 'geometry:margin=1in',
    '-V', 'colorlinks=true',
    '-V', 'mainfont=Latin Modern Roman',
    '-V', 'mathfont=Latin Modern Math',
    '-V', 'monofont=Latin Modern Mono'
)

Write-Host 'Running pandoc...'
& $pandoc @pandocArgs
if ($LASTEXITCODE -ne 0) { throw "pandoc failed with exit code $LASTEXITCODE" }
Write-Host "Wrote TeX: $texFile"

if ($SkipPdf) {
    Write-Host '-SkipPdf: stopping before PDF build.'
    return
}

# ---- latexmk: .tex -> .pdf --------------------------------------------------
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

# ---- Copy to Connes ---------------------------------------------------------
$outPdf = Join-Path $connesDir 'ExactVerification-SemilocalWeilForm-Note-v2.pdf'
Copy-Item (Join-Path $buildDir 'paper.pdf') $outPdf -Force

$info = Get-Item $outPdf
Write-Host ''
Write-Host ('OK   {0}  ({1:N0} KB)' -f $outPdf, ($info.Length / 1KB))
