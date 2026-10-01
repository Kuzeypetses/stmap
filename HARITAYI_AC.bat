@echo off
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python bulunamadi. Haritanin data\MAPLIST.xlsx dosyasini otomatik okuyabilmesi icin Python 3 gereklidir.
  pause
  exit /b 1
)
start "KuzeyPet ST Haritasi Server" /min python server.py
ping 127.0.0.1 -n 2 >nul
start "" http://127.0.0.1:8765/
