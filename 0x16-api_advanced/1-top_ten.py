#!/usr/bin/python3

import requests


def top_ten(subreddit):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36"
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
    else:
        print(None)
