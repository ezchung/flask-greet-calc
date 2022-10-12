# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/')
def hello_world():
  return "hello world"

map = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div
}


@app.get("/<operation>")
def operate(operation):

  a = request.args["a"]
  b = request.args["b"]

  fn = map[operation]

  return f"{fn(int(a), int(b))}"
  
