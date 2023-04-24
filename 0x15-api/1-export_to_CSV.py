#!/usr/bin/python3
"""
This module provides a function to export task data to CSV format
"""

import csv
import requests

# Define function to export data to CSV format


def export_tasks_to_csv(user_id, username, tasks):
    # Set up file name based on user_id
    file_name = f"{user_id}.csv"

    # Open file in write mode and write headers
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Loop through tasks and write each row to the CSV file
        for task in tasks:
            writer.writerow([user_id, username, task["completed"],
                             task["title"]])

        # Print message indicating successful export
        print(f"{len(tasks)} tasks exported {file_name} for user {user_id})")


if __name__ == "__main__":
    # Example usage
    user_id = 2
    username = "Antonette"
    tasks = [
        {"userId": 2, "title": "suscipit repellat ", "completed": False},
        {"userId": 2, "title": "distinctio vitae aute", "completed": True},
        {"userId": 2, "title": "et itaque necessit", "completed": False},
        {"userId": 2, "title": "adipisci non ad ", "completed": False},
        {"userId": 2, "title": "voluptas quo ", "completed": True},
        {"userId": 2, "title": "aliquam aut quasi", "completed": True},
        {"userId": 2, "title": "veritatis pariatur ", "completed": True},
        {"userId": 2, "title": "nesciunt totam sit", "completed": False},
        {"userId": 2, "title": "laborum aut in quam", "completed": False},
        {"userId": 2, "title": "nemo perspiciatis repell", "completed": True},
        {"userId": 2, "title": "repudiandae totam in es", "completed": False},
        {"userId": 2, "title": "earum doloribus ea dolo", "completed": False},
        {"userId": 2, "title": "sint sit aut vero", "completed": False},
        {"userId": 2, "title": "porro aut necess", "completed": False},
        {"userId": 2, "title": "repellendus veritatis ", "completed": True},
        {"userId": 2, "title": "excepturi deleniti ", "completed": True},
        {"userId": 2, "title": "sunt cum tempora", "completed": False},
        {"userId": 2, "title": "totam quia non", "completed": False},
        {"userId": 2, "title": "doloremque quibusdam as", "completed": False},
        {"userId": 2, "title": "totam atque quo nesciunt", "completed": True},
    ]

    export_tasks_to_csv(user_id, username, tasks)
