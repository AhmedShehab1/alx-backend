#!/usr/bin/env python3
"""
4-app
"""
from typing import Dict, Union
from flask_babel import Babel
from flask import Flask, render_template, request, g
from pytz import timezone

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = timezone("UTC")
    LANGUAGES = ["en", "fr"]


def get_locale():
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang

    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
babel = Babel()
babel.init_app(app, locale_selector=get_locale)
app.config.from_object(Config)


def get_user() -> Union[Dict, None]:
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    g.user = get_user()


@app.route("/")
def index():
    return render_template("5-index.html")
