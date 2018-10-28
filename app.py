from __future__ import print_function
from flask import Flask, request
import sys

from src.helper import *
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from config import statOrderBody

# TODO: more send options
# TODO: auth 
# TODO: clear sched
# TODO: show sched
# TODO: multi language option
# TODO: AI talk
# TODO: database for reviews
# TODO: SSL

app = Flask(__name__)
# scheduler = BackgroundScheduler()

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
        return "OK", 200
    else:
        for it in request.form:
            print (it,file=sys.stdout)
        print (request.form, sys.stdout)
        return "Invalid request"




if __name__ == '__main__':
    logging.basicConfig(filename="log/debug.log",
                    format='%(levelname)s\t%(asctime)s:%(filename)s:%(funcName)s:%(lineno)d %(name)s  %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
    app.debug = True
    # scheduler.start()
    app.run(host ='0.0.0.0', port=5000)