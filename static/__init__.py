from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from static.logger_config import custom_logger


db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger('static')
logger = custom_logger(logger)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/SampleDb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)

    from static.todoApp import todo_list
    app.register_blueprint(todo_list, url_prefix="/api/v1")

    return app
