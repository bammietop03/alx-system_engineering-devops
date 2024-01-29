#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
import requests
import sys


def get_todos(employee_id):
    baseUrl = f"https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_id

    try:
        # Extracting the User Full Name
        url = baseUrl + "/" + employee_id
        response = requests.get(url)
        data = response.json()

        # Getting User Todos
        todoUrl = url + "/todos"
        responsei = requests.get(todoUrl)

        username = data['username']
        filename = f"{employee_id}.json"

        # Extracting JSON data from the response
        todos = responsei.json()

        dictionary = {employee_id: []}
        for todo in todos:
            dictionary[employee_id].append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": username
            })
        with open(filename, 'w') as file:
            json.dump(dictionary, file)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    get_todos(sys.argv[1])
