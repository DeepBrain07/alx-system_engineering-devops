#!/usr/bin/python3
""" This script uses a REST API to generate information about an employee """
import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    link1 = "https://my-json-server.typicode.com/"
    link2 = "DeepBrain07/alx-system_engineering-devops/db"
    link = link1 + link2
    with urlopen(link) as f:
        """ opens the specified link """
        data = f.read().decode("UTF-8")
        data = json.loads(data)
    id = int(sys.argv[1])
    dictLst = data["employees"]
    for i in range(len(dictLst)):
        if dictLst[i]["id"] == id:
            name = dictLst[i].get("name")
            tasks_done = dictLst[i].get("tasks_done")
            total_tasks = dictLst[i].get("total_tasks")
            tmp = "Employee {} is done with tasks({}/{}):"
            print(tmp.format(name, tasks_done, total_tasks))
            print(dictLst[i]["task_title"])
