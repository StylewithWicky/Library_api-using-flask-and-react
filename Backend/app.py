from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import Sqlalchemy
from config import Config

db=Sqlalchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)

    from .controllers.book_controller import book_bp

    return app