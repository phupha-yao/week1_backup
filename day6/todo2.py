import json
import sys
import os

fileName = "tasks.json"

def load_tasks():
    try:
        with open(fileName, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(fileName, "w") as file:
        json.dump(tasks, file, indent=2)

def add(task):
    tasks = load_tasks()
    if dupe_check(task):
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print(f"Added: {task}")
    else:
        print("Already added")

def list():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    index = 1
    sorted_tasks = sort_task(tasks)
    for value in sorted_tasks:
        if value['done'] == True:
            status = "Done"
        else:
            status = "Not Done"
        print(index, ". ", value['task'], ": ", status)
        index = index + 1

def remove_tasks(index):
    tasks = load_tasks()
    if index >= 0 and index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print("Successful")
    else:
        print("Not valid index")

def mark_done(index):
    tasks = load_tasks()
    if index >= 0 and index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
    else:
        print("Not valid index")

def dupe_check(task):
    tasks = load_tasks()
    for i in tasks:
        if task == i['task']:
            return False
    return True

def sort_task(tasks):
    sorted_tasks = sorted(tasks, key=lambda t: (t["done"], t["task"].lower()))
    return sorted_tasks

def main():
    if len(sys.argv) < 2:
        print("Command not valid")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == "add":
        task_text = " ".join(sys.argv[2:])
        if task_text:
            add(task_text)
        else:
            print("Error: No task provided.")
    elif command == "list":
        list()
    elif command == "remove":
        remove_tasks(int(sys.argv[2]) - 1)
    elif command == "done":
        mark_done(int(sys.argv[2]) - 1)
    else:
        print("No command exists")

if __name__ == "__main__":
    main()