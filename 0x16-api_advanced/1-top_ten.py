#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """get 10 hot posts"""
    url = "https://www.reddit.com/r/{subreddit}/hot.jason?limit=10"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code !=200:
        print(None)
        return

    data = response.json().get("data").get("children")
    top_10_posts = "/n".join(post.get("data").get(title) for post in data)
    print (top_10_posts)
