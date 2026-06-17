#!/usr/bin/env bash
# Package becamex-slide for distribution (zip).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILL_NAME="$(basename "$SKILL_ROOT")"
DIST_DIR="$SKILL_ROOT/dist"
ZIP_PATH="$DIST_DIR/${SKILL_NAME}.zip"

mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"

(
  cd "$(dirname "$SKILL_ROOT")"
  zip -r "$ZIP_PATH" "$SKILL_NAME" \
    -x "$SKILL_NAME/dist/*" \
    -x "$SKILL_NAME/.DS_Store" \
    -x "*/.DS_Store"
)

echo "Created: $ZIP_PATH"
echo "Share this zip. Recipient runs: unzip becamex-slide.zip && cd becamex-slide && bash scripts/install.sh"
