#!/usr/bin/env bash
# Install becamex-slide into Cursor and/or Antigravity personal skills directories.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="$(cd "$SCRIPT_DIR/.." && pwd)"

AGENT="${1:-all}"

install_to() {
  local dest="$1"
  local label="$2"
  local dest_dir
  dest_dir="$(cd "$(dirname "$dest")" && pwd)"
  local src_dir
  src_dir="$(cd "$SKILL_SRC" && pwd)"

  if [ "$dest_dir" = "$src_dir" ]; then
    echo "Skip $label: destination is the source skill directory."
    return 0
  fi

  echo "Installing becamex-slide for $label..."
  echo "  From: $SKILL_SRC"
  echo "  To:   $dest"
  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  cp -R "$SKILL_SRC" "$dest"
  rm -rf "$dest/dist"
  echo "  Done: $dest"
}

case "$AGENT" in
  cursor)
    install_to "${CURSOR_SKILLS_DIR:-$HOME/.cursor/skills}/becamex-slide" "Cursor"
    echo ""
    echo "Restart Cursor or open a new Agent chat to use the skill."
    ;;
  antigravity)
    install_to "${ANTIGRAVITY_SKILLS_DIR:-$HOME/.agent/skills}/becamex-slide" "Antigravity"
    echo ""
    echo "Restart Antigravity or open a new chat to use the skill."
    ;;
  all)
    install_to "${CURSOR_SKILLS_DIR:-$HOME/.cursor/skills}/becamex-slide" "Cursor"
    install_to "${ANTIGRAVITY_SKILLS_DIR:-$HOME/.agent/skills}/becamex-slide" "Antigravity"
    echo ""
    echo "Restart Cursor/Antigravity or open a new chat to use the skill."
    ;;
  *)
    echo "Usage: $0 [cursor|antigravity|all]" >&2
    exit 1
    ;;
esac

echo "See README.md for usage."
