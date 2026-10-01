#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

HOST = "127.0.0.1"
PORT = 8765
ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        try:
            clean_path = self.path.split("?", 1)[0]
            local_path = Path(self.translate_path(clean_path))
            if local_path.name == "MAPLIST.xlsx" and local_path.is_file():
                st = local_path.stat()
                self.send_header("X-File-Version", f"{st.st_mtime_ns}-{st.st_size}")
        except Exception:
            pass
        super().end_headers()

if __name__ == "__main__":
    print(f"Kuzey Pet ST Haritasi: http://{HOST}:{PORT}/")
    print("Bu pencere acik kaldigi surece data/MAPLIST.xlsx canli olarak okunur.")
    ThreadingHTTPServer((HOST, PORT), NoCacheHandler).serve_forever()
