#!/usr/bin/python3
"""This module makes a request for a Fake API"""

import json
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    done = 0
    users_ = 'https://jsonplaceholder.typicode.com/users/{}'
    tasks_ = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    response_u = requests.get(users_.format(user))
    response_t = requests.get(tasks_.format(user))
    name = response_u.json()['name']
    t_total = len(response_t.json())
    for tasks in range(t_total):
        if response_t.json()[tasks]['completed'] is True:
            done += 1
    text = "Employee {} is done with tasks({}/{}):"
    print(text.format(name, done, t_total))
    for tasks in range(t_total):
        if response_t.json()[tasks]['completed'] is True:
            task = response_t.json()[tasks]['title']
            print("\t {}".format(task))
