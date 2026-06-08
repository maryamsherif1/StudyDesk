import json
import os

TASKS_FILE = "tasks.json"
NOTES_FILE = "notes.json"

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

def show_menu():
    print("\n===== StudyDesk =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. View notes")
    print("6. Add note")
    print("7. Delete note")
    print("8. Exit")
    print("=====================")

def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i + 1}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_data(TASKS_FILE, tasks)
    print("Task added!")

def complete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to mark complete: "))
    tasks[num - 1]["done"] = True
    save_data(TASKS_FILE, tasks)
    print("Task marked as complete!")

def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to delete: "))
    tasks.pop(num - 1)
    save_data(TASKS_FILE, tasks)
    print("Task deleted!")

def view_notes(notes):
    print("\n--- Your Notes ---")
    if len(notes) == 0:
        print("No notes yet!")
    else:
        for i, note in enumerate(notes):
            print(f"{i + 1}. [{note['subject']}] {note['content']}")

def add_note(notes):
    subject = input("Enter subject (e.g. Math, OS, Networks): ")
    content = input("Enter your note: ")
    notes.append({"subject": subject, "content": content})
    save_data(NOTES_FILE, notes)
    print("Note saved!")

def delete_note(notes):
    view_notes(notes)
    if len(notes) == 0:
        return
    num = int(input("Enter note number to delete: "))
    notes.pop(num - 1)
    save_data(NOTES_FILE, notes)
    print("Note deleted!")

def main():
    tasks = load_data(TASKS_FILE)
    notes = load_data(NOTES_FILE)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            view_notes(notes)
        elif choice == "6":
            add_note(notes)
        elif choice == "7":
            delete_note(notes)
        elif choice == "8":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.")

main()