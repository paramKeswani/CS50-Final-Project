from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/index.html")