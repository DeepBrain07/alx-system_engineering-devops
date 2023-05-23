#!/usr/bin/python3
""" This script uses a REST API to generate information about an employee """
import json
from urllib.request import urlopen


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    with urlopen(url) as f:
        data = f.read().decode("UTF-8")
        data = json.loads(data)
    fileName = "todo_all_employees.json"
    Dict = {}
    for i in range(len(data)):
        name = data[i].get("username")
        id = str(data[i].get("id"))
        Dict[id] = []
        todo_url = url + "/" + id + "/" + "todos"
        with urlopen(todo_url) as f:
            data2 = f.read().decode("UTF-8")
            data2 = json.loads(data2)
        myDict = {}
        for j in range(len(data2)):
            myDict["username"] = name
            myDict["task"] = data2[j].get("title")
            myDict["completed"] = data2[j].get("completed")
            Dict[id].append(myDict)
    with open(fileName, "a") as f:
        json.dump(Dict, f)
