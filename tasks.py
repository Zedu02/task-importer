import json
import os

if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        json.dump([], file)

def add_task(task):
    tasks.append(task)
    save_tasks_to_file()

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' has been deleted.")
        save_tasks_to_file()
    else:
        print("Invalid task number!")

def load_tasks_from_file():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks_to_file():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

tasks = load_tasks_from_file()

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        task_text = input("Enter the task text: ")
        add_task(task_text)
    elif choice == "2":
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        task_index_to_delete = int(input("Enter the task number to delete: "))
        delete_task(task_index_to_delete)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option! Please choose again.")
