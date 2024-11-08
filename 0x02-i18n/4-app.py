#!/usr/bin/env python3
"""
4-app
"""
from flask_babel import Babel
from flask import Flask, render_template, request
from pytz import timezone


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = timezone("UTC")
    LANGUAGES = ["en", "fr"]


def get_locale():
    lang = request.args.get("lang")
    if lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
babel = Babel()
babel.init_app(app, locale_selector=get_locale)
app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("4-index.html")
