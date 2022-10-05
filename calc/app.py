# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/<todo>")
def mymath(todo):
    a = int(request.args['a'])
    b = int(request.args['b'])
    print(type(a))
    themath = {'add': add,
               'sub': sub,
               'mult': mult,
               'div': div}
    result = themath[todo](a,b)
    return str(result)