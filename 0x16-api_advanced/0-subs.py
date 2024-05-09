#!/usr/bin/python3
"""
Should contain the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0
    
    try:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, ValueError):
        return 0



