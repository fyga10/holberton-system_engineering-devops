#!/usr/bin/python3
"""API"""


if __name__ == '__main__':
    import json
    import requests
    import sys
    user_state = make_user_dict()
    print('Employee {} is done with tasks({}/{}):'.format(
                                                    user_state['name'],
                                                    user_state['done_tasks'],
                                                    user_state['total_tasks']))
    def make_user_dict():
    """ This function returns the dictionary with the relevant information """
    user_dict = {}
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_info = get_info("{}users/{}".format(base_url, sys.argv[1]))
    user_dict['name'] = user_info['name']
    raw_json = get_info('{}todos'.format(base_url))
    done_tasks = 0
    total_tasks = 0
    tasks = []
    for element in raw_json:
        if element['userId'] == int(sys.argv[1]):
            total_tasks += 1
            if element['completed'] is True:
                done_tasks += 1
                tasks += [element['title']]
    user_dict['done_tasks'] = done_tasks
    user_dict['total_tasks'] = total_tasks
    user_dict['tasks'] = tasks
    return user_dict
    for element in user_state['tasks']:
        print('\t {}'.format(element))