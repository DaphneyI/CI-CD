from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello, docker"

@app.route('/new-route')
def new_route():
    return 'this is a new route'
