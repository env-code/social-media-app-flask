from flask import Flask

from .config import Config
from .extensions import db, jwt, migrate, mail, cors
from os import path,environ

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    cors.init_app(app)


    #create database
    with app.app_context():
        db.create_all()

    return app

def create_db(app):

    is_existDB = null