from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from static import db
from static.todoApp.model.todo_list_model import Todo
from static.todoApp.utils.serialize_data import TodoListSerializer
import logging

logger = logging.getLogger(__name__)



class TodoListView(Resource):

    def get(self):
        serialize_instance = TodoListSerializer(Todo.get_all())
        logger.debug(f"serialize_instance called here")
        if serialize_instance.is_valid():
            data = {
                "todo_list": serialize_instance.data(),
            }
            return jsonify(data), 200

    def post(self):
        title = request.form.get("title") or request.form.get("title")
        Todo.create(title)
        logger.info("New task created")
        # return redirect(url_for("home"))
        return {"message": "successfully added task"}, 201

    def put(self):
        todo_id = request.form.get("todo_id") or request.form.get("todo_id")
        title = request.form.get("title") or request.form.get("title")
        Todo.update(todo_id,title)
        logger.info("Task Updated")
        # return redirect(url_for("home"))
        return {"message": "successfully updated task"}, 200
 
    def patch(self):
        pass

    def delete(self):
        todo_id = request.form.get("todo_id") or request.form.get("todo_id")
        Todo.delete(todo_id) 
        logger.info("Task Deleted")
        # return redirect(url_for("home"))
        return {"message": "successfully deleted task"}, 200