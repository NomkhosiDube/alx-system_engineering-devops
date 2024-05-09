#!/usr/bin/python3
"""Contains recurse function"""


import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieves titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Custom User Agent"
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None  # Return None if subreddit is not found

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        hot_list.append(child.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


    
