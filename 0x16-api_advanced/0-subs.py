#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit
    :param subreddit: The name of the subreddit to query
    :return: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
