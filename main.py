import json
import os

TASKS_FILE = "tasks.json"


class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(TASKS_FILE):
            return []
        with open(TASKS_FILE, "r") as f:
            return json.load(f)

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {title}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "✔" if task["completed"] else "✘"
            print(f'{task["id"]}. {task["title"]} [{status}]')

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print("Task marked as completed.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.save_tasks()
        print("Task deleted.")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()