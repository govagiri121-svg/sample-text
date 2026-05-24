import json
import os

FILE = "tasks.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)

def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add(tasks):
    name = input("Task name: ").strip()
    if name:
        tasks.append({"name": name, "done": False})
        save(tasks)
        print("Task added!")
    else:
        print("Name cannot be empty.")

def view(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {status} {t['name']}")

def mark_done(tasks):
    view(tasks)
    try:
        n = int(input("Task number to mark done: "))
        tasks[n - 1]["done"] = True
        save(tasks)
        print("Marked as done!")
    except (ValueError, IndexError):
        print("Invalid number.")

def delete(tasks):
    view(tasks)
    try:
        n = int(input("Task number to delete: "))
        removed = tasks.pop(n - 1)
        save(tasks)
        print(f'Deleted: {removed["name"]}')
    except (ValueError, IndexError):
        print("Invalid number.")

def main():
    tasks = load()
    while True:
        print("\n1. Add  2. View  3. Mark Done  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1": add(tasks)
        elif choice == "2": view(tasks)
        elif choice == "3": mark_done(tasks)
        elif choice == "4": delete(tasks)
        elif choice == "5": break
        else: print("Invalid choice.")

main()
