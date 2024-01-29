#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys


def get_todos(employee_id):
    baseUrl = f"https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_id

    try:
        # Extracting the User Full Name
        url = baseUrl + "/" + employee_id
        response = requests.get(url)
        todos = response.json()
        employee_name = todos['name']

        # Getting User Todos
        todoUrl = url + "/todos"
        responsei = requests.get(todoUrl)

        # Extracting JSON data from the response
        todos = responsei.json()

        # Filter completed tasks
        completed_tasks = []
        for data in todos:
            if data['completed']:
                completed_tasks.append(data)

        # Total number of tasks
        total_tasks = len(todos)

        # Number of completed tasks
        total_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, total_completed_tasks, total_tasks))
        # Printing titles of completed tasks
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    get_todos(sys.argv[1])
