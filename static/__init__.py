from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = <yourURI>

    # from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)

    # from static.todoApp import todo_list
    # app.register_blueprint(todo_list)

    return app
