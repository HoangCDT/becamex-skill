#!/usr/bin/env bash
# Copy bundled BECAMEX brand assets into a deck output directory.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BUNDLED="$SKILL_ROOT/template/becamex-assets"
OUT="${1:-.}"

if [ ! -d "$BUNDLED" ]; then
  echo "Missing bundled assets: $BUNDLED" >&2
  exit 1
fi

DEST="$OUT/becamex-assets"
mkdir -p "$DEST"

for f in chevron.png becamex-logo.png cover-logo.png cover-slide-bg.png; do
  cp "$BUNDLED/$f" "$DEST/$f"
  echo "  $DEST/$f"
done

echo ""
echo "Done. Brand assets copied to: $DEST"
