import json
import socket


# КЛИЕНТ

class SocketClient:
    def __init__(self, host, port):
        self.target_host = host
        self.target_port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        self.client.connect((self.target_host, self.target_port))

    def get(self):
        request = 'GET / HTTP/1.1\r\n' + \
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
        return data[-1]

    def post(self, params, data):
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

        data = ''.join(total_data).splitlines()
        return data[-1]


    def put(self,params,data):
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
        return data[-1]

if __name__ == '__main__':
    s = SocketClient('127.0.0.1', 9090)
    data = json.dumps({'login': 'macho',
     'password': 'ass'})
    data1 = json.dumps({'login': 'amir',
     'password': 'oss'})
    data2 = json.dumps({'login': 'pop',
                        'password': 'looa'})
    res = s.put('/', data2)
    print(res)
