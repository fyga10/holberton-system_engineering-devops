#!/usr/bin/python3
""" This module makes a request for a Fake API """

import json
import requests
import sys import argv

    resp1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    resp2 = requests.get('https://jsonplaceholder.typicode.com/users')

    users_json = resp2.json()
    todos_j = resp1.json()

    name = users_j[int(argv[1]) - 1]['username']

    dosome = []
    uid = argv[1]
    dic = {}
    lista = []
    for tmp in todos_j:
        if tmp['userId'] == int(uid):
            tmp['task'] = tmp.pop('title')
            tmp['username'] = name
            del tmp['id']
            del tmp['userId']
            lista.append(tmp)
    dic[str(uid)] = lista

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(dic, f)
