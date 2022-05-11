# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/")
def landing():
    return "<h1>Calcutron 5000</h1>"

@app.route("/<function>")
def math(function):
    a = int(request.args["a"])
    b = int(request.args["b"])

    if function == "add":
        result = add(a, b)
    elif function == "sub":
        result = sub(a, b)
    elif function == "mult":
        result = mult(a, b)
    elif function == "div":
        result = div(a, b)
    
    return f"{result}"


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<function>")
def do_math(function):
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{operators[function](a, b)}"