tasks = []

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

def add_task(task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added to your to-do list.")

def mark_completed(task_name):
    for task in tasks:
        if task["task"] == task_name:
            task["completed"] = True
            print(f"Task '{task_name}' marked as completed.")
            return
    print(f"Task '{task_name}' not found in the to-do list.")

def remove_task(task_name):
    for task in tasks:
        if task["task"] == task_name:
            tasks.remove(task)
            print(f"Task '{task_name}' removed from your to-do list.")
            return
    print(f"Task '{task_name}' not found in the to-do list.")

while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '3':
        task_name = input("Enter the task name to mark as completed: ")
        mark_completed(task_name)
    elif choice == '4':
        task_name = input("Enter the task name to remove: ")
        remove_task(task_name)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
