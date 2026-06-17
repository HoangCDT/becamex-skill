#!/usr/bin/env bash
# Extract BECAMEX brand PNGs from BecaTruck PPT template.
# Usage: extract-assets.sh <path-to.pptx> <output-dir>

set -euo pipefail

PPTX="${1:?Usage: extract-assets.sh <pptx> <out-dir>}"
OUT="${2:?Usage: extract-assets.sh <pptx> <out-dir>}"

mkdir -p "$OUT"

unzip -p "$PPTX" ppt/media/image4.png > "$OUT/chevron.png"
unzip -p "$PPTX" ppt/media/image7.png > "$OUT/becamex-logo.png"

echo "Wrote: $OUT/chevron.png"
echo "Wrote: $OUT/becamex-logo.png"
echo "Note: copy user files separately:"
echo "  - cover-slide-bg.png (background, no logo)"
echo "  - cover-logo.png (BECAMEX logo for top-left on cover)"
