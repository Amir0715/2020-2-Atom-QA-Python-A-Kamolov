import json
from time import sleep

import pytest

from mock_server.http_mock_server import SimpleMockHTTPServer
from socket_client.http_socket_client import SocketClient
from stub.simple_http_server import SimpleHTTPServer
from application import app
import settings

class TestServer:

    @pytest.fixture(scope='function')
    def mock(self):
        server = SimpleMockHTTPServer(settings.MOCK_HOST, settings.MOCK_PORT)
        server.start()
        yield server
        server.stop()

    @pytest.fixture(scope='session')
    def stub(self):
        server = SimpleHTTPServer(settings.STUB_HOST, settings.STUB_PORT)
        server.start()
        yield server
        server.stop()

    @pytest.fixture(scope='session')
    def app(self):
        application = app.run_app(settings.APP_HOST, settings.APP_PORT)
        yield application
        socket = SocketClient(settings.APP_HOST, settings.APP_PORT)
        socket.get('/shutdown')

    @pytest.fixture(scope='session')
    def socket(self):
        socket = SocketClient(settings.APP_HOST, settings.APP_PORT)
        yield socket

    def test_get_req(self, socket, mock, app):
        res = socket.get('/')
        assert res['status'] == 'ok'

    def test_add_user(self, socket, mock, app):
        user = json.dumps({"login": "amir", "password": "pass"})
        res = socket.post('/users/add', user)
        assert res['status'] == 'ok'
        users = socket.get('/users')
        assert users[0]['login'] == 'amir' and users[0]['password'] == 'pass'

    def test_update_user(self, socket, mock, app):
        user = json.dumps({"login": "amir", "password": "pass"})
        res = socket.post('/users/add', user)
        assert res['status'] == 'ok'
        user = json.dumps({"login": "amir", "password": "pass2"})
        res = socket.put('/users/update', user)
        assert res['status'] == 'ok'
        users = socket.get('/users')
        assert users[0]['login'] == 'amir' and users[0]['password'] == 'pass2'

    def test_update_user_negative(self, socket, mock, app):
        user = json.dumps({"login": "amir", "password": "pass2"})
        res = socket.put('/users/update', user)
        assert res['status'] == 'fail'
        users = socket.get('/users')

        with pytest.raises(KeyError):
            users[0]['login'] == 'amir' and users[0]['password'] == 'pass2'

    def test_get_all_users(self, socket, mock, app):
        user1 = json.dumps({"login": "amir", "password": "pass"})
        user2 = json.dumps({"login": "pavel", "password": "pass2"})
        user3 = json.dumps({"login": "alex", "password": "pass3"})
        res = socket.post('/users/add', user1)
        assert res['status'] == 'ok'
        res = socket.post('/users/add', user2)
        assert res['status'] == 'ok'
        res = socket.post('/users/add', user3)
        assert res['status'] == 'ok'

        users = socket.get('/users')
        print(type(users[0]['login']))
        assert (users[0]['login'] == 'amir' and users[0]['password'] == 'pass') \
               and (users[1]['login'] == 'pavel' and users[1]['password'] == 'pass2') \
               and (users[2]['login'] == 'alex' and users[2]['password'] == 'pass3')

    def test_without_mock(self, socket, app):
        res = socket.get('/')
        assert res['status'] == 'fail'


    def test_with_mock_e500(self, socket, mock, app):
        res = socket.get('/mock_e500')
        assert res['status'] == 'fail'