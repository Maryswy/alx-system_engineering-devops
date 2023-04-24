#!/usr/bin/python3

import csv

# Define function to export data to CSV format
def export_tasks_to_csv(user_id, username, tasks):
    # Set up file name based on user_id
    file_name = f"{user_id}.csv"

    # Open file in write mode and write headers
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Loop through tasks and write each row to the CSV file
        for task in tasks:
            writer.writerow([user_id, username, task["completed"], task["title"]])

        # Print message indicating successful export
        print(f"{len(tasks)} tasks exported to {file_name} for user {user_id} ({username})")


if __name__ == "__main__":
    # Example usage
    user_id = 2
    username = "Antonette"
    tasks = [
        {"userId": 2, "id": 2, "title": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
        {"userId": 2, "id": 2, "title": "distinctio vitae autem nihil ut molestias quo", "completed": True},
        {"userId": 2, "id": 2, "title": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": False},
        {"userId": 2, "id": 2, "title": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": False},
        {"userId": 2, "id": 2, "title": "voluptas quo tenetur perspiciatis explicabo natus", "completed": True},
        {"userId": 2, "id": 2, "title": "aliquam aut quasi", "completed": True},
        {"userId": 2, "id": 2, "title": "veritatis pariatur delectus", "completed": True},
        {"userId": 2, "id": 2, "title": "nesciunt totam sit blanditiis sit", "completed": False},
        {"userId": 2, "id": 2, "title": "laborum aut in quam", "completed": False},
        {"userId": 2, "id": 2, "title": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": True},
        {"userId": 2, "id": 2, "title": "repudiandae totam in est sint facere fuga", "completed": False},
        {"userId": 2, "id": 2, "title": "earum doloribus ea doloremque quis", "completed": False},
        {"userId": 2, "id": 2, "title": "sint sit aut vero", "completed": False},
        {"userId": 2, "id": 2, "title": "porro aut necessitatibus eaque distinctio", "completed": False},
        {"userId": 2, "id": 2, "title": "repellendus veritatis molestias dicta incidunt", "completed": True},
        {"userId": 2, "id": 2, "title": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": True},
        {"userId": 2, "id": 2, "title": "sunt cum tempora", "completed": False},
        {"userId": 2, "id": 2, "title": "totam quia non", "completed": False},
        {"userId": 2, "id": 2, "title": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": False},
        {"userId": 2, "id": 2, "title": "totam atque quo nesciunt", "completed": True},
    ]

    export_tasks_to_csv(user_id, username, tasks)

