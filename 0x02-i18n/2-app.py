#!/usr/bin/env python3
"""
2-app
"""
from flask_babel import Babel
from flask import Flask, render_template, request
from pytz import timezone


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = timezone("UTC")
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    return render_template("2-index.html")
