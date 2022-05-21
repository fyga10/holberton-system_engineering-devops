#!/usr/bin/python3
"""
Top Ten
"""
import json
import requests


def top_ten(subreddit):
    """
     function that queries the Reddit API and prints the
     titles of the first 10 hot posts listed
    """
    url = "https://www.reddit.com/r/{}/hot.json"
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'
    }
    r_title = requests.get(url.format(subreddit), headers=headers)
    if r_title.status_code == 200:
        data = r_title.json()['data']['children']
        for x in range(10):
            print(data[x]['data']['title'])
    else:
        print(None)
