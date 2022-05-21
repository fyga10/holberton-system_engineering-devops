#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], pag=""):
    """returns a list of all hot post titles for a given subreddit"""
    header = {"User-Agent": "Mozilla/5.0"}
    url_ = 'https://www.reddit.com/r/' + subreddit +\
          '/hot.json?after={}'.format(pag)
    rp = requests.get(url_, headers=header, allow_redirects=False)
    if rp.status_code != 200:
        return None
    else:
        response = rp.json()
        tmp = response.get('data').get('children')
        for data in tmp:
            hot_list.append(data.get('data').get('title'))
        pag = response.get('data').get('after')
        if pag is not None:
            recurse(subreddit, hot_list, pag)
        return hot_list
