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