import os
import subprocess
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Railway variables se .env file banao
def create_env_file():
    env_content = f"""TELEGRAM_BOT_TOKEN={os.getenv('TELEGRAM_BOT_TOKEN', '')}
ADMIN_IDS={os.getenv('ADMIN_IDS', '')}
DEVELOPER_USERNAME={os.getenv('DEVELOPER_USERNAME', '')}
REQUIRED_CHANNEL_IDS={os.getenv('REQUIRED_CHANNEL_IDS', '')}
"""
    with open('.env', 'w') as f:
        f.write(env_content)
    print("✅ .env file created from environment variables")
    print(f"   TOKEN: {os.getenv('TELEGRAM_BOT_TOKEN', '')[:20]}...")
    print(f"   ADMIN: {os.getenv('ADMIN_IDS', '')}")

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
    # Pehle .env file banao
    create_env_file()
    
    # HTTP server background me chalao
    t = threading.Thread(target=run_http, daemon=True)
    t.start()
    
    # Ab tumhara actual bot chalao
    subprocess.run([sys.executable, 'bot.py'])