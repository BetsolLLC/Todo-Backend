from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from static import db
from static import cors
from static.todoApp.model.todo_list_model import Todo
from static.todoApp.utils.serialize_data import TodoListSerializer
import logging

logger = logging.getLogger(__name__)


class TodoListView(Resource):
    def before_request(self, *args, **kwargs):
        return cors.before_request(self, *args, **kwargs)

    def get(self):
        try:
            serialize_instance = TodoListSerializer(Todo.get_all())
            logger.debug(f"serialize_instance called here")
            if serialize_instance.is_valid():
                data = {
                    "todo_list": serialize_instance.data(),
                }
                return jsonify(data), 200
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500

    def post(self):
        try:
            title = request.form.get("title")
            Todo.create(title)
            logger.info("New task created")

            return {"message": "successfully added task"}, 201
        except KeyError:
            return {"message": "missing title"}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500

    def put(self):
        try:
            todo_id = request.form.get("todo_id")
            title = request.form.get("title")
            Todo.update(todo_id, title)

            return {"message": "successfully updated task"}, 200
        except KeyError:
            return {"message": "missing title"}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": "Todo with the request id not found"}, 400
 
    def patch(self):
        try:
            todo_id = request.form.get("todo_id")
            Todo.update_complete(todo_id)

            return {"message": "successfully completed task"}, 200
        except KeyError:
            return {"message": "Task not found"}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": "Todo with the request id not found"}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500
    def delete(self):
        try:
            todo_id = request.form.get("todo_id")
            Todo.delete(todo_id)
            return {"message": "successfully deleted task"}, 200
        except KeyError:
            return {"message": "task not found"}, 400
        except ValueError as e:
            return {"message": "Todo with the request id not found"}, 400