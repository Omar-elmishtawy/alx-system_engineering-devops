#!/usr/bin/python3
""" Restful api"""

import requests
from sys import argv
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    todo = "{}/user/{}/todos".format(url, argv[1])
    user = "{}/users/{}".format(url, argv[1])
    todo_result = requests.get(todo).json()
    user_result = requests.get(user).json()
    user_name = user_result.get("name")

    total_number_of_tasks = len(todo_result)
    list_of_done_tasks = []
    no_of_done_tasks = 0
    for todo in todo_result:
        if (todo.get("completed")):
            no_of_done_tasks += 1
            list_of_done_tasks.append(todo.get("title"))


    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, no_of_done_tasks, total_number_of_tasks))

    for done in list_of_done_tasks:
        print("\t {}".format(done))
