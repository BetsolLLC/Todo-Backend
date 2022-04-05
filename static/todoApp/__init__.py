from flask import Blueprint

from .views.todo_list_view import TodoListView

todo_list = Blueprint('todo', __name__)
todo_list.add_url_rule('/', view_func=TodoListView.as_view('todo_list'), methods=['GET', 'POST', 'DELETE', 'PUT','PATCH'])