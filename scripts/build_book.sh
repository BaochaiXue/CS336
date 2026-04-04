#!/bin/bash
# build_book.sh — Full build pipeline for the CS336 textbook
# Usage: ./scripts/build_book.sh [--clean] [--quick]
#
# Options:
#   --clean   Remove auxiliary files before building
#   --quick   Single lualatex pass (no biber, no cross-refs)

set -euo pipefail

BOOK_DIR="$(cd "$(dirname "$0")/../book" && pwd)"
cd "$BOOK_DIR"

MAIN="textbook"

# Parse arguments
CLEAN=false
QUICK=false
for arg in "$@"; do
  case $arg in
    --clean) CLEAN=true ;;
    --quick) QUICK=true ;;
    *) echo "Unknown option: $arg"; exit 1 ;;
  esac
done

# Clean auxiliary files
if $CLEAN; then
  echo "🧹 Cleaning auxiliary files..."
  rm -f "${MAIN}".{aux,bbl,bcf,blg,log,out,run.xml,toc,lof,lot,fls,fdb_latexmk,synctex.gz}
  rm -f chapters/*.aux appendices/*.aux frontmatter/*.aux
  echo "   Done."
fi

echo "══════════════════════════════════════════════"
echo "  Building: ${MAIN}.tex"
echo "  Engine:   lualatex"
echo "  Bib:      biber"
echo "══════════════════════════════════════════════"

# First pass
echo ""
echo "📝 Pass 1: lualatex..."
lualatex -interaction=nonstopmode -halt-on-error "${MAIN}.tex"

if ! $QUICK; then
  # Bibliography
  echo ""
  echo "📚 Running biber..."
  biber "${MAIN}"

  # Second pass (resolve citations)
  echo ""
  echo "📝 Pass 2: lualatex..."
  lualatex -interaction=nonstopmode -halt-on-error "${MAIN}.tex"

  # Third pass (resolve cross-references)
  echo ""
  echo "📝 Pass 3: lualatex..."
  lualatex -interaction=nonstopmode -halt-on-error "${MAIN}.tex"
fi

echo ""
echo "══════════════════════════════════════════════"
echo "  ✅ Build complete: ${MAIN}.pdf"
echo "══════════════════════════════════════════════"
