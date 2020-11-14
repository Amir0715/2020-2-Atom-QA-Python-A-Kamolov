import json
import socket
import time


# КЛИЕНТ


class SocketClient:
    def __init__(self, host, port):
        self.target_host = host
        self.target_port = port

    def _set_connection(self, timeout):
        start = int(time.time())
        end = start + timeout
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(4)
        status = 1
        while int(time.time()) < end:
            try:
                status = self.client.connect_ex((self.target_host, self.target_port))
                if status == 0:
                    return status
            except Exception:
                pass
        if status != 0:
            raise ConnectionRefusedError

    def get(self, params):
        self._set_connection(4)
        request = 'GET {params} HTTP/1.1\r\n'.format(params=params) + \
                  'Host:{host}\r\n\r\n'.format(host=self.target_host + ':' + str(self.target_port))

        self.client.send(request.encode())

        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        return json.loads(data[-1])

    def post(self, params, data):
        self._set_connection(4)
        body_bytes = data.encode()
        req = f'POST {params} HTTP/1.1\r\n' + \
              'Host: {host}\r\n'.format(host=self.target_host + ':' + str(self.target_port)) + \
              'Content-Type: application/json\r\n' + \
              'Content-Length: {length}\r\n\r\n'.format(length=len(body_bytes)) + \
              '{body}'.format(body=data)
        self.client.send(req.encode())
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        self.client.close()
        data = ''.join(total_data).splitlines()
        return json.loads(data[-1])

    def put(self, params, data):
        self._set_connection(4)
        body_bytes = data.encode()
        req = f'PUT {params} HTTP/1.1\r\n' + \
              'Host: {host}\r\n'.format(host=self.target_host + ':' + str(self.target_port)) + \
              'Content-Type: application/json\r\n' + \
              'Content-Length: {length}\r\n\r\n'.format(length=len(body_bytes)) + \
              '{body}'.format(body=data)
        self.client.send(req.encode())
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        if len(data) != 0:
            return json.loads(data[-1])
        else:
            return None
