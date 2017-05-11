from flask import Flask
import http.client
import socket
import constants

"""
To run (on Windows)
set FLASK_APP=client.py&&set FLASK_DEBUG=1
flask run --host=0.0.0.0
"""

app = Flask(__name__)

@app.route('/')
def index():
    send_join_request()
    return app.send_static_file("client.html")

def send_join_request():
    conn = http.client.HTTPConnection(constants.MASTER_SERVER)
    pass

class GameState(object):

    def __init__():
        self.player_name = None
        self.my_turn = False
        self.score = 0
        #self.board_state   Maybe later


if __name__ == "__main__":
    # ugly hack to get port number
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    my_port = sock.getsockname()[1]
    sock.close()
    
    app.run(port=my_port)