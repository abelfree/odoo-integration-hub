from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MockHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        size = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(size) if size else b"{}"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True, "received": json.loads(body)}).encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8099), MockHandler)
    server.serve_forever()
