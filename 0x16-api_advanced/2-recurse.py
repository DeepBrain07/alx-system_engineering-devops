#!/usr/bin/python3

"""
hot articles for a given subreddit
"""

from requests import get


def recurse(subreddit, hot_list=[]):
    """
    function that queries the Reddit API and returns a
    list of all hot articles for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        posts = results['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
    except Exception:
        return hot_list
    if results['data']['after'] is None:
        return hot_list
    else:
        recurse(subreddit, hot_list)
