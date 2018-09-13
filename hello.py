from __future__ import print_function
from flask import Flask, request
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def de_get():
    return 'Get, World!'

@app.route('/', methods=['POST'])
def do_post():
    if "challenge" in request.form:
        return request.form["challenge"]
    for it in request.form:
        print (it,file=sys.stdout)
    print (request.form, sys.stdout)
    return "OMG"

if __name__ == '__main__':
    app.debug = True
    app.run(host ='0.0.0.0', port=5000)