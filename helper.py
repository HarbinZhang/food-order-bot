from config import config, statOrderBody
import requests
import time, datetime
from apscheduler.schedulers.background import BackgroundScheduler
import json


def handlePayload(req):
    payload = json.loads(req['payload'])
    print payload['actions']
    return "payload"

def handleJson(req):
    if 'challenge' in req:
        return handleChallenge(req)
    elif 'event' in req:
        params = req['event']['text'].split(' ')
        if params[1] == 'url':
            postOrder(params)
            scheduleJob()
        elif params[1] == 'stat':
            statOrder()
        res = "OK"
    else:
        res = "OMG"
    return res


def statOrder():
    send(statOrderBody)


def postOrder(params):
    url = params[2]
    name = params[3] if (len(params)==4) else "Demo"
    body = '<!here> ' + url + '\nFor tomorrow\'s ' + name + ' meeting\'s order\n'
    body += 'Order will be closed at 11:00AM tomorrow\nThanks!'
    body = {"text":body}
    send(body)


def scheduleJob():
    sched = BackgroundScheduler()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    sched.add_job(sendAlert_1hour, 'cron', year=tomorrow.year, month=tomorrow.month, 
            day=tomorrow.day, hour=10, minute=00)
    sched.add_job(sendAlert_10min, 'cron', year=tomorrow.year, month=tomorrow.month, 
            day=tomorrow.day, hour=10, minute=50)    
    sched.add_job(sendAlert_10min, 'cron', year=tomorrow.year, month=tomorrow.month, 
            day=tomorrow.day, hour=10, minute=50)                    
    sched.start()

def sendAlert_1hour():
    body = {"text":"<!here> food order will be closed in 10 min."}
    send(body)

def sendAlert_10min():
    body = {"text":"<!here> food order will be closed in 1 hour."}
    send(body)

def closeAlert():
    body = {"text":"<!harbin> closing order, please"}
    send(body)

def send(body):
    url = config["foodUrl"]
    # url = "http://18.191.72.192:3000"
    post = requests.post(url, json=body)


def handleChallenge(req):
    return req['challenge']
