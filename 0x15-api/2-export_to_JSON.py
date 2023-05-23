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
            name = data[i].get("username")
    todo_url = url + "/" + str(id) + "/" + "todos"
    with urlopen(todo_url) as f:
        data = f.read().decode("UTF-8")
        data = json.loads(data)
    id = str(id)
    fileName = id + ".json"
    Dict = {id: []}
    myDict = {}
    for i in range(len(data)):
        myDict["task"] = data[i].get("title")
        myDict["completed"] = data[i].get("completed")
        myDict["username"] = name
        Dict[id].append(myDict)
    with open(fileName, "w+") as f:
        json.dump(Dict, f)
