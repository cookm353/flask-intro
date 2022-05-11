from flask import Flask, request


app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return """Welcome!"""

@app.route("/welcome/<message>")
def welcome_message(message):
    return f"Welcome {message}!"


if __name__ == "__main__":
    app.run()