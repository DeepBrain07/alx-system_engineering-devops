#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and returns top 10
    listings for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print('None')

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        posts = results['data']['children']
        for post in posts:
            print(post['data']['title'])

    except Exception:
        print('None')
