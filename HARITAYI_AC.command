#!/bin/bash
cd "$(dirname "$0")"
URL="http://127.0.0.1:8765/"
if ! command -v python3 >/dev/null 2>&1; then
  osascript -e 'display dialog "Python 3 bulunamadi. Haritanin data/MAPLIST.xlsx dosyasini otomatik okuyabilmesi icin Python 3 gereklidir." buttons {"Tamam"} default button 1' 2>/dev/null || true
  exit 1
fi
if ! curl -fsS --max-time 1 "$URL" >/dev/null 2>&1; then
  nohup python3 server.py > /tmp/kuzeypet_st_haritasi.log 2>&1 &
  sleep 1
fi
open "$URL"
