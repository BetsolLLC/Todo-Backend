import logging

from flask import request, jsonify
from flask_restful import Resource

from static.todoApp.model.todo_list_model import Todo
from static.todoApp.utils.serialize_data import TodoListSerializer

logger = logging.getLogger(__name__)


class TodoListView(Resource):

    def get(self):
        try:
            serialize_instance = TodoListSerializer(Todo.get_all(), model_type="todo", many=True)
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
            title = request.get_json(force=True)['title']
            if title == "":
                raise ValueError("title is required")
            Todo.create(title)
            logger.info("New task created")

            return {"message": "successfully added task"}, 201
        except KeyError:
            return {"message": "missing title"}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": "missing title"}, 500
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500

    def put(self, todo_id):
        try:
            data = request.get_json(force=True)
            data["id"] = todo_id
            serializer = TodoListSerializer(data, model_type="dict")
            if serializer.is_valid():
                parsed_data = serializer.data()
                Todo.update(parsed_data['id'], parsed_data['title'], parsed_data['completed'])
                return {"message": "successfully updated task"}, 200
        except KeyError:
            return {"message": "missing required keys"}, 400
        except ValueError as e:
            logger.error(f"Error: {e}")
            return {"message": "Todo with the request id not found"}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500

    def patch(self):
        """
        TODO : Implement PATCH method
        :return:
        """
        return {"message": "PATCH method not implemented"}, 501

    def delete(self, todo_id):
        try:
            Todo.delete(todo_id)
            return {"message": "successfully deleted task"}, 200
        except KeyError:
            return {"message": "task not found"}, 400
        except ValueError as e:
            return {"message": "Todo with the request id not found"}, 400
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": "something went wrong"}, 500
