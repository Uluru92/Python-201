'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.

'''

import requests
from pprint import pprint

base_url_users = "http://demo.codingnomads.co:8080/tasks_api/users"
base_url_task = "http://demo.codingnomads.co:8080/tasks_api/tasks"


def print_menu():
    print("\nPlease select from the following options (enter the number of the action you'd like to take):")
    print("1) Create a new account (POST)")
    print("2) View all your tasks (GET)")
    print("3) View your completed tasks (GET)")
    print("4) View only your incomplete tasks (GET)")
    print("5) Create a new task (POST)")
    print("6) Update an existing task (PATCH/PUT)")
    print("7) Delete a task (DELETE)")
    print("8) Exit")

def create_account():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    response = requests.post(base_url_users, json=data)
    if response.status_code == 201:
        print("Account created successfully!")
    else:
        print(f"Failed to create account: {response.text}")

def view_tasks():
    response = requests.get(base_url_task)
    task_list = []
    if response.status_code == 200:
        tasks = response.json()["data"] 
        print("\nYour tasks:")
        for task in tasks:
            task_list.append(f"ID: {task["id"]} / User ID:{task["userId"]} / Name: {task["name"]}")
        pprint(task_list)
    else:
        print("Failed to fetch tasks.")

def view_completed_tasks():
    response = requests.get("http://demo.codingnomads.co:8080/tasks_api/tasks?completed=true")
    task_completed_list = []
    if response.status_code == 200:
        tasks = response.json()["data"]
        print("\nYour completed tasks:")
        for task in tasks:
            task_completed_list.append(f"ID: {task["id"]} / User ID:{task["userId"]} / Name: {task["name"]}")
        pprint(task_completed_list)
    else:
        print("Failed to fetch tasks.")

def view_incomplete_tasks():
    response = requests.get("http://demo.codingnomads.co:8080/tasks_api/tasks?completed=false")
    task_incompleted_list = []
    if response.status_code == 200:
        tasks = response.json()["data"]
        print("\nYour incomplete tasks:")
        for task in tasks:
            task_incompleted_list.append(f"ID: {task["id"]} / User ID:{task["userId"]}  / Name: {task["name"]}")
        pprint(task_incompleted_list)
    else:
        print("Failed to fetch tasks.")

def create_task():
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    userId = int(input("Enter user ID: "))
    data = {
        "name": task_name,
        "description": task_description,
        "userId": userId,
        "completed": False
    }
    response = requests.post(base_url_task, json=data)
    if response.status_code == 201:
        print("Task created successfully!")
    else:
        print(f"Failed to create task: {response.text}")

def update_task():
    task_id = input("Enter task ID to update: ")
    userId = input("Enter user ID to update: ")
    task_name = input("Enter updated task name: ")
    task_description = input("Enter updated task description: ")
    completed = input("Is the task completed? (yes/no): ").strip().lower()

    if completed == "yes":
        completed_task = True
    if completed == "no":
        completed_task = False
    
    data = {
        "userId":userId,
        "name": task_name,
        "description": task_description,
        "completed": completed_task
    }
    response = requests.put(f"{base_url_task}/{task_id}", json=data)
    if response.status_code == 200:
        print("Task updated successfully!")
    else:
        print(f"Failed to update task: {response.text}")

def delete_task():
    task_id = input("Enter task ID to delete: ")
    response = requests.delete(f"{base_url_task}/{task_id}")
    if response.status_code == 200:
        print("Task deleted successfully!")
    else:
        print(f"Failed to delete task: {response.text}")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_completed_tasks()
        elif choice == "4":
            view_incomplete_tasks()
        elif choice == "5":
            create_task()
        elif choice == "6":
            update_task()
        elif choice == "7":
            delete_task()
        elif choice == "8":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()