#!/usr/bin/env python
import os
import sqlite3
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def home():
        return render_template("home.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print("registering")
        print(request.form["username"])
        print(request.form["password"])
        return render_template("home.html")
    else:
        print("big redirect")
        return render_template("home.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("logging in")
        print(request.form["username"])
        print(request.form["password"])
        return render_template("home.html")
    else:
        print("big redirect")
        return render_template("home.html")

if __name__ == '__main__':
    app.run()