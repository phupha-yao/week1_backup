# To-Do CLI App

A simple command-line to-do list application written in Python. Stores tasks in a JSON file and allows adding, listing, and marking tasks as done.

## Features
- Add tasks
- List tasks (sorted by status and alphabetically)
- Mark tasks as done
- Store tasks persistently in `tasks.json`

## Requirements
- Python 3.x

## Usage

### Add a task
```bash
python3 todo2.py add "Buy milk"

List tasks
python3 todo2.py list

Mark tasks as done
python3 todo2.py done 1

Installation
git clone https://github.com/phupha-yao/week1_backup.git
cd todo-cli

Notes

Tasks are stored in tasks.json.
Sorting: incomplete tasks first, then alphabetical order within each status.