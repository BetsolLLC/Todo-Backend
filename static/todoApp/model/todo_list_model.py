from static import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean,default=False)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())

    @staticmethod
    def get_all():
        return Todo.query.all()

    @staticmethod
    def get_by_id(task_id):
        return Todo.query.get(task_id)

    @staticmethod
    def create(title):
        todo = Todo(title=title, complete=False)
        db.session.add(todo)
        db.session.commit()
        return todo

    @staticmethod
    def update(task_id, title):
        todo = Todo.get_by_id(task_id)
        todo.title = title
        db.session.commit()
        return todo

    @staticmethod
    def delete(task_id):
        todo = Todo.get_by_id(task_id)
        db.session.delete(todo)
        db.session.commit()
        return todo

    @staticmethod
    def update_complete(task_id):
        pass