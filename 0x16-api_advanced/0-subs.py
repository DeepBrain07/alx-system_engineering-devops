#!/usr/bin/python3
""" This module queries the Reddit API and returns the
number of subscribers """


import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    headers = {"User-Agent": user_agent}

    try:
        str = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = requests.get(str, headers=headers)
        return response.json()["data"]["subscribers"]
    except Exception as e:
        return 0
