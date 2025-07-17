tasks = []
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task added: {task}")
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "Completed" if t["completed"] else "Not Completed"
        print(f"{i}. {t['task']} [{status}]")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
