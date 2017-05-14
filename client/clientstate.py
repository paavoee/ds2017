#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

peers = {}
my_turn = False

def begin_turn():
    my_turn = True


if __name__ == "__main__":
    peers = \
        {
            "Player_1": {"hostaddr": "127.0.0.1", "port": "5001"},
            "Player_2": {"hostaddr": "127.0.0.1", "port": "5002"}
        }
