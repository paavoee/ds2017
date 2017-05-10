from flask import Flask

"""
To run (on Windows)
set FLASK_APP=server.py&&set FLASK_DEBUG=1
flask run --host=0.0.0.0
"""

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World"
