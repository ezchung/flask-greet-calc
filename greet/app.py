from flask import Flask, request

app = Flask(__name__)


@app.get("/welcome")
def sayWelcome():
    return "welcome"


@app.get("/welcome/home")
def sayWelcomeHome():
    return "welcome home"


@app.get("/welcome/back")
def sayWelcomeBack():
    return "welcome back"


# @app.get("/welcome/<location>")
# def sayWelcomeLocation(location):
#     return f"welcome {location}"
