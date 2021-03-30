import rook
import logging
import os

from flask import Flask
app = Flask(__name__)

x = 0

@app.route('/')
def hello_world():
    isUserNew("Bartholomew", "Villavicencio", "Otorhinolaryngologist")
    global x
    if (x == 3):
        x = 0
    else:
        x = x + 1
    return 'Hello, World! ' + str(x) + ' \n'

def isUserNew(last, first, occ):
    #      SELECT UserID FROM users WHERE LastName = lastName    
    #                                 AND FirstName = firstName
    #                                 AND Occupation = occupation;
    if (False):
        print("addNewUser(lastName, firstName, occupation)")
        return True;
    print("user exists")
    return False;


if __name__ == "__main__":
    rook.start(log_to_stderr=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000, threaded=True)
