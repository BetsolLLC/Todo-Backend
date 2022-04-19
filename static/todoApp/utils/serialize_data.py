class TodoListSerializer:
    def __init__(self, todo_list, model_type, many=False):
        self.todo_list = todo_list
        self.model_type = model_type
        self.many = many

    def is_valid(self):
        return self.todo_list is not None

    def return_data(self):
        if self.many:
            result = []
            for i in self.todo_list:
                if self.model_type == 'todo':
                    i = i.__dict__
                temp_dict = {
                    'id': i['id'],
                    'title': i['title'],
                    'date_modified': i['date_modified'],
                    'completed': True if i['complete'] else False,
                }
                if self.many:
                    result.append(temp_dict)
                else:
                    return temp_dict
        else:
            if self.model_type == 'todo':
                result = self.todo_list.__dict__
            else:
                self.todo_list['completed'] = True if self.todo_list['completed'] else False
                result = self.todo_list
        return result

    def data(self):
        if self.is_valid():
            return self.return_data()
        else:
            return None
