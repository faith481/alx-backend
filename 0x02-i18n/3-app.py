#!/usr/bin/env python3
"""Module for a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.url_map.strict_slashes = True
babel = Babel(app)


class Config:
    """Class for the flask_babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Gets and returns the locale of a web page"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Index page of the Flask application"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
