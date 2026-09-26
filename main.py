import os
import subprocess
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Bot is running')
    
    def log_message(self, format, *args):
        pass

def run_http():
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    server.serve_forever()

if __name__ == '__main__':
    # HTTP server background me chalao
    t = threading.Thread(target=run_http, daemon=True)
    t.start()
    # Tumhara actual bot chalao (bilkul as-is)
    subprocess.run([sys.executable, 'bot.py'])