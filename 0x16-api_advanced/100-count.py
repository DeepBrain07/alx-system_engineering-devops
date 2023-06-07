#!/usr/bin/python3
"""
Using reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)


def replace_word(word_list, old_word, new_word):
    """ replaces a word in a list """
    for i in range(len(word_list)):
        if word_list[i] == old_word:
            word_list[i] = new_word


def count_words(subreddit, word_list):
    """  parses the title of all hot articles, and prints
    a sorted count of given keyword """
    word_list = word_list.sort()
    count = 0
    lst = recurse(subreddit)
    for w in lst:
        replace_word(lst, w, w.lower())
    for wd in word_list:
        wd = wd.lower()
        for i in lst:
            if wd in i.split():
                count += 1
        print("{}: {}".format(wd, count))
        count = 0
