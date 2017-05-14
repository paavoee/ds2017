#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request

import json

from gamestate import GameState

"""
To run (on Windows)
set FLASK_APP=server.py&&set FLASK_DEBUG=1
flask run --host=0.0.0.0
"""

app = Flask(__name__)


@app.route('/')
def status():
    game_status = gamestate.status
    players_list = gamestate.connected_players.keys()
    if len(players_list) > 0:
        connected_players = " ".join(players_list)
    else:
        connected_players = "None"
    msg = "Game status: " + game_status + ". Connected players: " + connected_players
    return msg



@app.route('/join', methods=['POST'])
def join():
    payload = request.get_json()
    hostname = request.remote_addr
    gamestate.add_player(payload["player_name"], hostname, payload["port"])
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

#@app.route('/resume', methods=['POST'])
#hit when a player has closed their client / browser


if __name__ == "__main__":
    gamestate = GameState()
    app.run(debug=True, port=8000)
