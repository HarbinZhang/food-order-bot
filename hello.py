from flask import Flask, request

app = Flask(__name__)
app.config['TESTING'] = True
app.config['FLASK_ENV'] = "development"

@app.route('/', methods=['GET'])
def de_get():
    return 'Get, World!'

@app.route('/', methods=['POST'])
def do_post():
    if "challenge" in request.form:
        return request.form["challenge"]
    return "hi"
