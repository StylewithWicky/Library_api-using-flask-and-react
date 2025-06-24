from flask import Flask
from .extensions import db,migrate,dwt
from config import Config


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)

    from .controllers.book_controller import book_bp

    return app