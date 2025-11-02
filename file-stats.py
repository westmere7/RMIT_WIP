#!/usr/bin/env python3
import os
import json
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class FileStatsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/file-stats':
            # Handle file stats request
            query = parse_qs(parsed_path.query)
            file_path = query.get('file', [''])[0]
            
            # Sanitize path
            file_path = file_path.replace('../', '').replace('..\\', '')
            
            if file_path and os.path.exists(file_path):
                mtime = os.path.getmtime(file_path)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                response = json.dumps({
                    'lastModified': mtime,
                    'lastModifiedFormatted': str(mtime)
                })
                self.wfile.write(response.encode())
            else:
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'File not found'}).encode())
        else:
            # Serve static files normally
            super().do_GET()
    
    def end_headers(self):
        # Add Last-Modified header for all files
        if hasattr(self, 'translate_path'):
            path = self.translate_path(self.path)
            if os.path.exists(path) and os.path.isfile(path):
                mtime = os.path.getmtime(path)
                from email.utils import formatdate
                self.send_header('Last-Modified', formatdate(mtime, usegmt=True))
        super().end_headers()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = HTTPServer(('', port), FileStatsHandler)
    print(f'Server running on http://localhost:{port}/')
    server.serve_forever()
