from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Creating a Flask App
app = Flask(__name__)
CORS(app)

# Connecting the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zybrdrdsgxvtss:bd83da69e431203e28acfe61ffcdd891b303914f3cd6005058fff79f19a5abd6@ec2-54-173-77-184.compute-1.amazonaws.com:5432/d5pn062kkjdnfu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False         
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Creating a Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())

class TodoListSerializer:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def is_valid(self):
        return self.todo_list is not None

    def data(self):
        if self.is_valid():
            result = [
                {
                    "id": i.id,
                    "title": i.title,
                    "completed": i.complete,
                    "date_modified": i.date_modified,
                } for i in self.todo_list]
            return result
        else:
            return None
# Routes
@app.route("/")
def home():
    serialize_instance = TodoListSerializer(Todo.query.all())
    if serialize_instance.is_valid():
        data = {
            "todo_list": serialize_instance.data(),
        }
        return jsonify(data), 200


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return {"message":"successfully created"}, 200


@app.route("/update/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return {"message":"successfully completed"}, 200


@app.route("/delete/<int:todo_id>", methods=["DELETE"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return {"message":"successfully deleted"}, 200


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
