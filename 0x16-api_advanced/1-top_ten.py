#!/usr/bin/python3
"""Contains top_ten function"""


import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Custom User Agent"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        print("None")  # Print None if subreddit is not found
        return

    try:
        data = response.json()
        children = data['data']['children']
        for child in children:
            print(child['data']['title'])
    except (KeyError, ValueError):
        print("None")  # Print None if there is an error in parsing JSON data



