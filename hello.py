import rook
import logging

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    rook.flush()
    return 'Hello, World!\n'

if __name__ == "__main__":
    rook.start(log_to_stderr=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000, threaded=True)
