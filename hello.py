import rook
import logging
import os

from flask import Flask
app = Flask(__name__)

x = 0

@app.route('/')
def hello_world():
    global x
    if (x == 3):
        x = 0
    else:
        x = x + 1
    rook.flush()
    print ("BLAH")
    print (os.environ.get("ROOKOUT_LABELS"))
    return 'Hello, World! ' + str(x) + ' \n'

if __name__ == "__main__":
    rook.start(log_to_stderr=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000, threaded=True)
