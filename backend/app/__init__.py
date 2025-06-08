from flask import Flask
from .extensions import mongo
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    mongo.init_app(app)


    return app