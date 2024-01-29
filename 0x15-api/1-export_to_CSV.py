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
        data = response.json()

        # Getting User Todos
        todoUrl = url + "/todos"
        responsei = requests.get(todoUrl)

        username = data['username']
        csv_filename = f"{employee_id}.csv"

        # Extracting JSON data from the response
        todos = responsei.json()

        with open(csv_filename, mode='w') as file:
            for todo in todos:
                file.write('"{}","{}","{}","{}"\n'
                           .format(employee_id, username, todo['completed'],
                                   todo['title']))

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    get_todos(sys.argv[1])
