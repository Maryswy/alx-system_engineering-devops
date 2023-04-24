#!/usr/bin/python3
"""Export tasks owned by a specific employee to a CSV file"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    # Set up API endpoint and query parameters
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": argv[1]}

    # Send GET request to API endpoint
    response = requests.get(url, params=params)

    # Raise exception if API request was unsuccessful
    response.raise_for_status()

    # Parse JSON response to Python dictionary
    tasks = response.json()

    # Write tasks to CSV file
    with open(argv[1] + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([task["userId"], task["title"], str(task["completed"]), task["title"]])

    # Define user ID, username, task_completed_status, task_title
    user_id = 2
    username = 'Mary'
    task_completed_status = 'True'
    task_completed_status = 'False'
    task_title = ''
