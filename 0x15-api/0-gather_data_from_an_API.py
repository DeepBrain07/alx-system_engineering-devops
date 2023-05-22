#!/usr/bin/python3
""" This script uses a REST API to generate information about an employee """
import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    with urlopen(url) as f:
        data = f.read().decode("UTF-8")
        data = json.loads(data)
    id = int(sys.argv[1])
    for i in range(len(data)):
        if data[i].get("id") == id:
            name = data[i].get("name")
    todo_url = url + "/" + str(id) + "/" + "todos"
    with urlopen(todo_url) as f:
        data = f.read().decode("UTF-8")
        data = json.loads(data)
    total_task = len(data)
    task_done = 0
    for i in range(len(data)):
        if data[i].get("completed") is True:
            task_done += 1
    myStr = "Employee {} is done with tasks({}/{}):"
    print(myStr.format(name, task_done, total_task))
    for i in range(len(data)):
        if data[i].get("completed") is True:
            tmp = data[i].get("title")
            print("\t {}".format(tmp))
