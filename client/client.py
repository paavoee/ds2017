#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import http.client
import json
import requests
import socket

import clientstate

"""
To run (on Windows)
set FLASK_APP=client.py&&set FLASK_DEBUG=1
flask run --host=0.0.0.0
"""

MASTER_SERVER_URL = "http://127.0.0.1:8000"

app = Flask(__name__)


@app.route('/')
def index():
    send_join_request()
    return app.send_static_file("client.html")


@app.route('/startgame', methods=['POST'])
def start():
    # parse player list
    players = request.get_json()
    clientstate.peers.update(players)
    return "OK"
    # see if I have the first turn
        # if yes, unlock UI
    # if no, lock UI


@app.route('/beginturn')
def begin_turn():
    clientstate.begin_turn()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/endturn')
def end_turn(): pass


@app.route('/gameupdate', methods=['POST'])
def game_update(): pass


def send_join_request():
    player_name = "Player_" + str(my_port)
    req = requests.post(MASTER_SERVER_URL + "/join", json={"player_name": player_name, "port": my_port})
    req.raise_for_status()


if __name__ == "__main__":
    # ugly hack to get port number
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    my_port = str(sock.getsockname()[1])
    sock.close()
    
    app.run(debug=True, port=my_port)
