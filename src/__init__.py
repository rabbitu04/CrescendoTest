import json

from flask import Flask

from src.line_bot import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_file('config.json', load=json.load)
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    app.user_records = {}

    return app
