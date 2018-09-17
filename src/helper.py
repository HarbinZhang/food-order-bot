from config import config, statOrderBody
import requests
import time, datetime
from apscheduler.schedulers.background import BackgroundScheduler
import json
import logging



def handlePayload(req):
    if 'payload' not in req:
        logging.warning("invalid params for payload")
        return "Invalid Params"
    payload = json.loads(req['payload'])
    print payload['actions']
    return statOrderBody


def handleJson(req):
    if 'challenge' in req:
        return handleChallenge(req)
    elif 'event' in req:
        if not checkUserOfEvent(req['event'], 'UBSMN15JA'):
            send({"text":"Who are you?"})
            logging.warning("Unauthorized User")
            return "OK"
        params = req['event']['text'].split(' ')
        if len(params) < 2:
            logging.warning("invalid params for event")
            return "Invalid Params"
        if params[1] == 'url':
            if postOrder(params):
                scheduleJob()
            else:
                logging.warning("invalid params for url")
                return "Invalid Params"
        elif params[1] == 'stat':
            statOrder()
        else:
            logging.warning("invalid params for actions")
            return "Invalid Params"
        res = "OK"
    else:
        res = "OMG"
    return res


def checkUserOfEvent(event, id):
    if 'user' not in event:
        return False
    if event['user'] != id:
        return False
    return True

def statOrder():
    send(statOrderBody)


def postOrder(params):
    if len(params) < 3:
        return False
    url = params[2]
    if len(url) == 0:
        return False
    name = params[3] if (len(params)==4) else "Demo"
    body = '<!here> ' + url + '\nFor tomorrow\'s ' + name + ' meeting\'s order\n'
    body += 'Order will be closed at 11:00AM tomorrow\nThanks!'
    body = {"text":body}
    send(body)
    return True


def scheduleJob():
    sched = BackgroundScheduler()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    sched.add_job(sendAlert_1hour, 'cron', year=tomorrow.year, month=tomorrow.month, 
            day=tomorrow.day, hour=10, minute=00)
    sched.add_job(sendAlert_10min, 'cron', year=tomorrow.year, month=tomorrow.month, 
            day=tomorrow.day, hour=10, minute=50)    
    sched.add_job(closeAlert, 'cron', year=tomorrow.year, month=tomorrow.month, 
            day=tomorrow.day, hour=11, minute=00)                    
    sched.start()

def sendAlert_1hour():
    body = {"text":"<!here> food order will be closed in 1 hour."}
    send(body)

def sendAlert_10min():
    body = {"text":"<!here> food order will be closed in 10 min."}
    send(body)

def closeAlert():
    body = {"text":"<@UBSMN15JA> closing order, please"}
    send(body)

def send(body):
    url = config["foodUrl"]
    requests.post(url, json=body)


def handleChallenge(req):
    return req['challenge']

