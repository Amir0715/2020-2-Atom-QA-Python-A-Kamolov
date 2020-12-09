import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import settings
# СЕРВЕР

class MockHandleRequests(BaseHTTPRequestHandler):
    users = None
    good_responses = json.dumps({'status': 'ok'}).encode()
    bad_responses = json.dumps({'status': 'fail'}).encode()
    timeout_responses = json.dumps({'status': 'timeout'}).encode()
    def _set_headers(self,code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers(200)
            self.wfile.write(self.good_responses)
        elif self.path == '/users':
            self._set_headers(200)
            self.wfile.write(json.dumps(self.users).encode())
        elif self.path == '/error500':
            self._set_headers(500)
            self.wfile.write(self.timeout_responses)


    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len).decode()
        if post_body:
            if self.headers['Content-Type'] == 'application/json':
                json_body = json.loads(post_body)
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
        if post_body:
            if self.headers['Content-Type'] == 'application/json':
                json_body = json.loads(post_body)
                print(self.users)
                if json_body and len(self.users) != 0:
                    login = json_body['login']
                    password = json_body['password']
                    for d in self.users:
                        if login == d['login']:
                            d['password'] = password
                    self._set_headers(200)
                    self.wfile.write(self.good_responses)
        else:
            self._set_headers(400)
            self.wfile.write(self.bad_responses)

class SimpleMockHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.users = []
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_users(self, users):
        self.handler.users.append(users)


if __name__ == '__main__':
    s = SimpleMockHTTPServer(settings.MOCK_HOST, settings.MOCK_PORT)
    s.start()
