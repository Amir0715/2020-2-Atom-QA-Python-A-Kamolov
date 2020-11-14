import threading
import requests
from urllib.parse import urljoin
from flask import Flask, request, jsonify
import settings
from socket_client.http_socket_client import SocketClient

app = Flask(__name__)
sock = None
DATA = {}


def run_app(host, port):
    server = threading.Thread(target=app.run, kwargs={
        'host': host,
        'port': port
    })
    server.start()

    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()
    return jsonify({'status': 'fail'}), 500


@app.route('/')
def index():
    sock = SocketClient(settings.MOCK_HOST, settings.MOCK_PORT)
    try :
        mock_response = sock.get('/')
    except ConnectionRefusedError as e:
        return jsonify({"status": "fail"}), 500
    if mock_response['status'] == 'ok':
        return jsonify({"status": "ok"}), 200
    else :
        return jsonify({"status": "fail"}), 400

@app.route('/mock_e500')
def mock_error():
    sock = SocketClient(settings.MOCK_HOST, settings.MOCK_PORT)
    mock_response = sock.get('/error500')
    if mock_response['status'] == 'timeout':
        return jsonify({"status": "fail"}), 500
    else:
        return jsonify({"status": "ok"}), 200

@app.route('/users/add', methods=["GET", "POST"])
def add_user():
    sock = SocketClient(settings.MOCK_HOST, settings.MOCK_PORT)
    mock_response = sock.post('/', request.data.decode())
    if mock_response['status'] == 'ok':
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "fail"}), 400


@app.route('/users/update', methods=["GET", "PUT"])
def update_user():
    sock = SocketClient(settings.MOCK_HOST, settings.MOCK_PORT)
    mock_response = sock.put('/', request.data.decode())
    print(mock_response)
    if mock_response and mock_response['status'] == 'ok':
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "fail"}), 400


@app.route('/users')
def get_users():
    sock = SocketClient(settings.MOCK_HOST, settings.MOCK_PORT)
    mock_response = sock.get('/users')
    if mock_response:
        return jsonify(mock_response), 200
    else:
        return jsonify({"status": "fail"}), 400



if __name__ == '__main__':
    run_app(settings.APP_HOST, settings.APP_PORT)
