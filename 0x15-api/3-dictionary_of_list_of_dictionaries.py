#!/usr/bin/python3
""" This module makes a request for a Fake API """

if __name__ == "__main__":
    import requests as req
    from sys
    import json
    all = req.get('https://jsonplaceholder.typicode.com/todos').json()
    usuarios = req.get('https://jsonplaceholder.typicode.com/users').json()
    todo_all_users = {}
    for user in usuarios:
        user_todos = []
        for task in all:
            try:
                if task['userId'] == user['id']:
                    del task['userId']
                    del task['id']
                    task['username'] = user['username']
                    task['task'] = task.pop('title')
                    user_todos.append(task)
            except Exception:
                pass
        todo_all_users[user['id']] = user_todos
    with open('todo_all_employees.json', 'w') as f:
        json.dump(todo_all_users, f)
