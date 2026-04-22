# Building `simplicial_vector_calculus.pdf`

This document describes how to reproduce the PDF from the canonical markdown
source (`simplicial_vector_calculus.md`). The build is deliberately minimal
and fully offline after the one-time toolchain install.

## What the build does

1. Parses `simplicial_vector_calculus.md` and extracts:
   - the H1 title,
   - the `**Author**` line,
   - the `*Month DD, YYYY*` date line,
   - the `## Abstract` block (everything between that heading and the next
     horizontal rule `---`).
2. Writes a preprocessed markdown file with a YAML front matter block
   containing `title`, `author`, `date`, `abstract`; the body that follows
   it is the manuscript minus the front-matter title block.
3. Invokes `pandoc` to convert the preprocessed markdown to a standalone
   LaTeX document, injecting `latex/preamble.tex` as extra header.
4. Invokes `latexmk -xelatex` to compile the LaTeX to PDF (2 passes for
   table of contents / cross-references).
5. Copies the final PDF next to the source as
   `simplicial_vector_calculus.pdf`.

Intermediate artifacts live under `build/` and are safe to delete at any
time. Pass `-Clean` (PowerShell) or `--clean` (bash) to force a fresh build.

## Directory layout

```
.
├── simplicial_vector_calculus.md   # canonical source
├── simplicial_vector_calculus.pdf  # build output (gitignored OK)
├── latex/
│   └── preamble.tex                # xelatex preamble injected via pandoc
├── build/                          # pandoc + latexmk intermediates
├── build.ps1                       # Windows / PowerShell build script
├── build.sh                        # POSIX build script
└── BUILD.md                        # this file
```

## Windows (PowerShell) — one-time toolchain install

```powershell
# 1. Install pandoc (~40 MB) and MiKTeX (~1 GB base + on-demand packages).
winget install --id JohnMacFarlane.Pandoc --source winget `
               --accept-source-agreements --accept-package-agreements --silent
winget install --id MiKTeX.MiKTeX --source winget --scope user `
               --accept-source-agreements --accept-package-agreements --silent

# 2. Enable silent auto-install of missing LaTeX packages (no prompts).
initexmf --set-config-value=[MPM]AutoInstall=1

# 3. (Recommended) Pre-install the Latin Modern math font so the first
#    build does not stall on a package download.
miktex packages install lm-math
initexmf --update-fndb
```

### Build

```powershell
# From the project root:
pwsh ./build.ps1             # incremental
pwsh ./build.ps1 -Clean      # wipe build/ first (recommended after edits)
pwsh ./build.ps1 -SkipPdf    # stop after generating build/paper.tex
```

## Linux / macOS — one-time toolchain install

```bash
# Debian / Ubuntu:
sudo apt install pandoc texlive-xetex latexmk \
                 texlive-fonts-recommended texlive-latex-extra

# macOS (Homebrew):
brew install pandoc
brew install --cask mactex-no-gui   # full TeX Live; includes xelatex + latexmk
```

### Build

```bash
chmod +x build.sh
./build.sh                # incremental
./build.sh --clean        # wipe build/ first
./build.sh --skip-pdf     # stop after generating build/paper.tex
```

## Expected output (smoke test)

A successful run ends with a line of the form

```
OK   .../simplicial_vector_calculus.pdf  (178 KB)
```

and produces a ~27-page PDF containing:
- Title, author, date (from the top of the markdown);
- Abstract (native LaTeX `abstract` environment);
- A clickable table of contents (sections and subsections);
- Sections 1–9, Acknowledgments, References, Appendices A–D.

## Customising

- **Preamble tweaks** (fonts, theorem env styling, link colours, hyperref
  metadata): edit `latex/preamble.tex` and rebuild.
- **Pandoc variables** (margins, font size, link colours applied via
  pandoc's own `\hypersetup`, TOC depth, etc.): edit the `pandocArgs`
  array in `build.ps1` (or the `pandoc` invocation in `build.sh`).
- **Front-matter parsing**: `build.ps1` / `build.sh` identify the title /
  author / date by regex. If you restructure the top of the markdown
  (author line no longer `**...**`, etc.), the scripts will fail loudly
  with a specific "Could not parse ..." message.

## Troubleshooting

- **`pandoc: command not found`** / **`latexmk: command not found`**:
  open a new shell after installing via `winget`, or run the PATH refresh
  that `build.ps1` performs at its top.
- **`The font "Latin Modern Math" cannot be found`**: run
  `miktex packages install lm-math && initexmf --update-fndb`.
- **MiKTeX keeps asking whether to install a package**: re-run step 2 of
  the install block (`initexmf --set-config-value=[MPM]AutoInstall=1`).
- **PDF is missing cross-reference numbers / TOC page numbers are `??`**:
  run `build.ps1 -Clean` (or `build.sh --clean`). `latexmk` normally
  handles multi-pass compilation, but a stale `build/paper.aux` from an
  aborted earlier run can confuse it.
