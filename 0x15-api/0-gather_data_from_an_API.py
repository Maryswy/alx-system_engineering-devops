#!/usr/bin/python3

"""
This script retrieves and displays the TODO list progress of a given employee ID using the provided REST API"""

import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """
    Retrieves the TODO list progress of a given employee ID from the provided REST API
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": employee_id})
    response.raise_for_status()


    # count completed tasks and total tasks
    completed_tasks = 0
    total_tasks = len(response.json())
    task_titles = []


    def calculate_progress(tasks):
        completed_tasks = 0
        total_tasks = len(tasks)
        task_titles = []

        for task in tasks:
            if task["completed"]:
                completed_tasks += 1
                task_titles.append(task["title"])
        return (completed_tasks, total_tasks, task_titles)

    return calculate_progress(response.json())


if __name__ == "__main__":
    # check if an employee ID is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide an employee ID as a command-line argument.")
        sys.exit()

    employee_id = int(sys.argv[1])


    # retrieve employee todo list progress
    completed_tasks, total_tasks, task_titles = get_employee_todo_list_progress(employee_id)

    # display progress information
    print(f"Employee {employee_id} is done with tasks ({completed_tasks}/{total_tasks}):")

    for title in task_titles:
        print(f"\t- {title}")
