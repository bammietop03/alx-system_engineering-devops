#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
import requests


def get_todos():
    baseUrl = "https://jsonplaceholder.typicode.com"

    try:
        # Extracting the User Full Name
        url = baseUrl + "/users"
        response = requests.get(url)
        userdata = response.json()

        # Getting User Todos
        todoUrl = baseUrl + "/todos"
        responsei = requests.get(todoUrl)

        filename = "todo_all_employees.json"

        # Extracting JSON data from the response
        todos = responsei.json()

        dictionary = {}
        for data in userdata:
            user_id = data.get('id')
            username = data.get('username')

            dictionary[user_id] = []
            for todo in todos:
                task = todo.get('title')
                completed = todo.get('completed')

                dictionary[user_id].append({
                    "username": username,
                    "task": task,
                    "completed": completed
                })

        with open(filename, 'w') as file:
            json.dump(dictionary, file)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == '__main__':
    get_todos()
