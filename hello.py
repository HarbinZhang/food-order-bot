from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def de_get():
    return 'Get, World!'

@app.route('/', methods=['POST'])
def do_post():
    if "challenge" in request.form:
        return request.form["challenge"]
    for it in request.form:
        print it
    return "hi"

if __name__ == '__main__':
    app.debug = True
    app.run(host ='0.0.0.0', port=5000)