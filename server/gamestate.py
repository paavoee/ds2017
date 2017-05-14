#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class GameState(object):

    def __init__(self):
        self.room_size = 2
        # "player_name": {"hostaddr": 192.168.0.1, "port: 8080}
        self.connected_players = {}
        self.status = "Waiting for players"
        self.turn_order = []
        self.current_turn = None

    def add_player(self, player_name, hostaddr, port):
        self.connected_players[player_name] = {"hostaddr": hostaddr, "port": port}
        if len(self.connected_players) == self.room_size:
            self.start_game()

    def start_game(self):
        self.status = "Game in progress"
        for name, conninfo in self.connected_players.items():
            self.turn_order.append(name)
            target_url = conninfo["hostaddr"] + ":" + conninfo["port"] + "/startgame"
            requests.post(target_url, json=self.connected_players)
        self.change_turn()

    def change_turn(self):
        if self.current_turn is None:
            self.current_turn = 0
        else:
            self.current_turn = (self.current_turn + 1) % len(self.turn_order)
        next_player = self.turn_order[self.current_turn]
        _url = self.get_url_for_player(next_player) + "/beginturn"
        requests.get(_url)

    def get_url_for_player(self, player_name):
        conn_info = self.connected_players[player_name]
        return conn_info["hostaddr"] + ":" + conn_info["port"]


if __name__ == "__main__":
    gs = GameState()
    gs.connected_players = \
        {
            "Player_1": {"hostaddr": "127.0.0.1", "port": "5001"},
            "Player_2": {"hostaddr": "127.0.0.1", "port": "5002"}
        }
    gs.turn_order = ["Make", "Seppo", "homo"]
    gs.current_turn = 5
    gs.change_turn()
