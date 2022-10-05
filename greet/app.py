from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome/<verb>')
def come_in(verb):
    if verb == "home":
        return "welcome home"
    elif verb == "back":
        return "welcome back"

@app.route('/welcome')
def come():
    return "welcome"