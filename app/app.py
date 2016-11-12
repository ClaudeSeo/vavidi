# -*- coding: utf-8 -*-
from flask import Flask
from translation import blueprint


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(blueprint)

    @app.errorhandler(404)
    def not_found(error):
        return '404 Not found', 404

    return app
