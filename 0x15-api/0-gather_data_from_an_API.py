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
            EMPLOYEE_NAME = dictLst[i].get("EMPLOYEE_NAME")
            NUMBER_OF_DONE_TASKS = dictLst[i].get("NUMBER_OF_DONE_TASKS")
            TOTAL_NUMBER_OF_TASKS = dictLst[i].get("TOTAL_NUMBER_OF_TASKS")
            tmp = "Employee {} is done with tasks({}/{}):"
            print(tmp.format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
            print(dictLst[i].get("TASK_TITLE"))
