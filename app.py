from __future__ import print_function
from flask import Flask, request, g
import sys

import logging
import os

from src.helper import handleJson, handlePayload
import sqlite3
import json


# TODO: clear sched
# TODO: show sched
# TODO: multi language option
# TODO: AI talk
# TODO: SSL

app = Flask(__name__)

@app.route('/', methods=['GET'])

def de_get():
    return 'Get, World!'

@app.route('/', methods=['POST'])
def do_post():
    contentType = request.headers.get('Content-Type')

    if contentType == 'application/json':
        res = handleJson(request.json)
        return res
    elif contentType == 'application/x-www-form-urlencoded':
        res = handlePayload(request.form)
        return json.dumps(res), 200, {'Content-Type': 'application/json'}
    else:
        for it in request.form:
            print (it,file=sys.stdout)
        print (request.form, sys.stdout)
        return "Invalid request"



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



if __name__ == '__main__':
    logging.basicConfig(filename="log/debug.log",
                    format='%(levelname)s\t%(asctime)s:%(filename)s:%(funcName)s:%(lineno)d %(name)s  %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

    app.debug = True
    app.run(host ='0.0.0.0', port=5000)