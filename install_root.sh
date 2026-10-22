#!/usr/bin/env bash
set -euo pipefail
src="$(realpath "$1")"

cd "$src"
find . -type f -print0 | while IFS= read -r -d '' f; do
    sudo install -D -Z -m 0644 -o root -g root "$f" "/${f#./}"
done

sudo systemctl daemon-reload
