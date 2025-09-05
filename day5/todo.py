import sys

if len(sys.argv) < 2:
    print("Usage: python todo.py [add/list/done] <task>")
    sys.exit()

command = sys.argv[1]

def load_task():
    try:
        file = open("tasks.txt", "r")
        tasks = file.read().split("\n")
        file.close
        return tasks
    except FileNotFoundError:
        return []
    
def save_task(tasks):
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

tasks = load_task()

if command == "add":
    tasks.append(sys.argv[2])
    save_task(tasks)
elif command == "list":
    if len(tasks) == 0:
        print("no tasks!")
        sys.exit(0)
    for i in range(0, len(tasks)):
        print(str((i + 1)) + "." + tasks[i])
elif command == "done":
    try:
        tasks.remove(sys.argv[2])
        save_task(tasks)
    except ValueError:
        print("No such task")