#!/usr/bin/env bash
set -euo pipefail

CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"
MANIFEST="$CLAUDE_HOME/.pm-kit-manifest"

if [[ ! -f "$MANIFEST" ]]; then
  echo "No claude-code-pm-kit manifest found at $MANIFEST"
  exit 0
fi

backup_dir="$(awk -F= '/^BACKUP_DIR=/{print $2}' "$MANIFEST" | tail -n 1)"

while IFS= read -r rel; do
  [[ -n "$rel" ]] || continue
  rm -rf "$CLAUDE_HOME/$rel"
done < <(awk -F= '/^PATH=/{print $2}' "$MANIFEST" | sort -r)

if [[ -n "${backup_dir:-}" && -d "$backup_dir" ]]; then
  if find "$backup_dir" -mindepth 1 -print -quit | grep -q .; then
    cp -R -p "$backup_dir"/. "$CLAUDE_HOME"/
    echo "Restored backup from $backup_dir"
  fi
fi

rm -f "$MANIFEST"
echo "Claude Code PM Kit uninstalled from $CLAUDE_HOME"
