#!/usr/bin/python3
""" This module makes a request for a Fake API """

import json
import requests
import sys

if __name__ == "__main__":
    user_ = sys.argv[1]
    file = "{}.csv".format(user_)
    users_u = 'https://jsonplaceholder.typicode.com/users/{}'
    tasks_u = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    response_u = requests.get(users_u.format(user_))
    response_t = requests.get(tasks_u.format(user_))
    usernam = response_u.json()['username']
    t_tota = len(response_t.json())
    with open(file, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in range(t_tota):
            status = response_t.json()[tasks]['completed']
            task = response_t.json()[tasks]['title']
            csv_writer.writerow([user_, usernam, status, task])
