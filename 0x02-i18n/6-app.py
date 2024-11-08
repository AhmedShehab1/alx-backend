#!/usr/bin/env python3
"""
4-app
"""
from datetime import datetime
from typing import Dict, Union
from flask_babel import Babel, format_datetime
from flask import Flask, render_template, request, g
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = pytz.timezone("UTC").zone
    LANGUAGES = ["en", "fr"]


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    locale_param = request.args.get("locale")
    if locale_param in app.config["LANGUAGES"]:
        return locale_param
    user = getattr(g, "user")
    if user and user.get("locale") in app.config["LANGUAGES"]:
        return user["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    try:
        tz_param = request.args.get("timezone")
        if tz_param:
            return pytz.timezone(tz_param).zone
        else:
            user = getattr(g, "user")
            if user and user.get("timezone"):
                return pytz.timezone(user["timezone"]).zone
    except UnknownTimeZoneError:
        pass
    return "UTC"


babel = Babel()
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


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
    tz = get_timezone()
    user_time = datetime.now(pytz.timezone(tz))

    foramtted_time = format_datetime(user_time)
    return render_template("index.html", current_time=foramtted_time)
