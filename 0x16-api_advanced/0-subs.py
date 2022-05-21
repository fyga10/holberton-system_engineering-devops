#!/usr/bin/python3
"""
How many subs?
"""
import json
import requests


def number_of_subscribers(subreddit):
	"""
	function that queries the Reddit API 
	and returns the number of subscribers
	"""
    url = "https://www.reddit.com/r/{}/about.json"
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'
    }
    r_subs = requests.get(url.format(subreddit), headers=headers)
    if r_subs.status_code == 200:
        data = r_subs.json()['data']
        subscribers = data.get('subscribers')
        if subscribers is not None:
            return subscribers
    return 0
