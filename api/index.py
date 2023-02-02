from flask import Flask, request, abort
from api.custom import run_prompt

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"


@app.route("/about")
def about():
    out = run_prompt("test")
    return out
