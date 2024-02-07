#!/usr/bin/env python3
"""
A basic Flask application for internationalization (i18n) using Flask-Babel.
"""

from typing import List
from flask import Flask, render_template
from flask_babel import Babel

class AppConfig:
    """
    Application configuration class.
    """
    LANGUAGES: List[str] = ['en', 'fr']
    DEFAULT_LANGUAGE: str = 'en'
    DEFAULT_TIMEZONE: str = 'UTC'

# Create an instance of Flask
my_app = Flask(__name__)
# Load configuration from the AppConfig class
my_app.config.from_object(AppConfig)

# Initialize Babel for internationalization
babel = Babel(my_app)

@my_app.route('/', strict_slashes=False)
def display_index() -> str:
    """
    Render the index template.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    my_app.run()
