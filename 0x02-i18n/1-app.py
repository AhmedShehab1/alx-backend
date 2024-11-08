#!/usr/bin/env python3
"""
1-app
"""
from flask_babel import Babel
from flask import Flask, render_template
from pytz import timezone


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = timezone("UTC")
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("1-index.html")
