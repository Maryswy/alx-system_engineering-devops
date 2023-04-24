#!/usr/bin/python3

"""
This module defines a function that exports task data in CSV format
"""

import csv

def export_tasks(user_id: int, username: str, tasks: list) -> None:
    """
    Exports all tasks owned by a given employee to a CSV file

    Args:
    - user_id (int): the ID of the employee
    - username (str): the username of the employee
    - tasks (list): a list of tasks, where each task is represented as a dictionary with the following keys:
        - title (str): the title of the task
        - completed (bool): True if the task is completed, False otherwise
        - assigned_to (str): the username of the employee to whom the task is assigned

    Returns:
    - None
    """
    # Filter tasks assigned to this user
    user_tasks = [task for task in tasks if task.get('assigned_to') == username]

    # Define CSV filename
    filename = f"{user_id}.csv"

    # Write CSV file
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in user_tasks:
            writer.writerow([user_id, username, task.get('completed'), task.get('title')])


if __name__ == "__main__":
    # Sample data
    tasks = [
        {'title': 'Complete task 1', 'completed': True, 'assigned_to': 'Mary'},
        {'title': 'Review task 2', 'completed': False, 'assigned_to': 'Mary'},
        {'title': 'Approve task 3', 'completed': True, 'assigned_to': 'Pavel'},
        {'title': 'Complete task 4', 'completed': False, 'assigned_to': 'Mary'},
        {'title': 'Review task 5', 'completed': True, 'assigned_to': 'Pavel'},
    ]

    # Define user ID and username
    user_id = 2
    username = 'Mary'

    # Export tasks
    export_tasks(user_id, username, tasks)
