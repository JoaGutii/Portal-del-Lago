#!/usr/bin/env bash
set -euo pipefail
echo "[BUILD] pip install..."
pip install -r backend/requirements.txt

if grep -q "DATABASE_URL" app.py; then
  echo "[BUILD] Patch DATABASE_URL -> env"
  if ! grep -q "os.getenv('DATABASE_URL')" app.py; then
    sed -i "1 i\import os" app.py
    sed -i "s|DATABASE_URL\s*=\s*\".*\"|DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:admin@localhost:5432/portal_del_lago')|g" app.py
  fi
fi
