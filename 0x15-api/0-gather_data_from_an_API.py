#!/usr/bin/python3
""" This script uses a REST API to generate information about an employee """
import json
import sys
from urllib.request import urlopen


with urlopen("https://my-json-server.typicode.com/DeepBrain07/alx-system_engineering-devops/db") as f:
    data = f.read().decode("UTF-8")
    data = json.loads(data)
id = int(sys.argv[1])
dictLst = data["employees"]
for i in range(len(dictLst)):
    if dictLst[i]["id"] == id:
        name = dictLst[i]["name"]
        tasks_done = dictLst[i]["tasks_done"]
        total_tasks = dictLst[i]["total_tasks"]
        print("Employee {} is done with tasks({}/{}):".format(name, tasks_done, total_tasks))
