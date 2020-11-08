import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

# СЕРВЕР

class StubHandleRequests(BaseHTTPRequestHandler):
    data = None
    users = []
    good_responses = json.dumps({'Status': 200}).encode()
    bad_responses = json.dumps({'Status': 400}).encode()

    def _set_headers(self,code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        self.wfile.write(self.good_responses)

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode()
        print(self.headers['Content-Type'])
        if post_body:
            if self.headers['Content-Type'] == 'application/json':
                json_body = json.loads(post_body)
                print(json_body)
                if json_body:
                    self.users.append(json_body)
                    self._set_headers(200)
                    self.wfile.write(self.good_responses)
        else:
            self._set_headers(400)
            self.wfile.write(self.bad_responses)

    def do_PUT(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode()
        print(self.headers['Content-Type'])
        if post_body:
            if self.headers['Content-Type'] == 'application/json':
                json_body = json.loads(post_body)
                if json_body:
                    login = json_body['login']
                    password = json_body['password']
                    for d in self.users:
                        print(d)
                        if login == d['login']:
                            d['password'] = password
                    self._set_headers(200)
                    self.wfile.write(self.good_responses)
        else:
            self._set_headers(400)
            self.wfile.write(self.bad_responses)

class SimpleHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = StubHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = json.dumps(data).encode()


if __name__ == '__main__':
    s = SimpleHTTPServer('127.0.0.1', 9090)
    s.set_data({"Test": "Test"})
    s.start()
