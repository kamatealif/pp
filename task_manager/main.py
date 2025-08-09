"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os 

def load_tasks(file):
    tasks = []
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if '||' in line:
                    text, status = line.strip().rsplit("||", 1)
                    tasks.append({"text": text, "status": status == "True" or status == "True" or status == "DONE"})
    return tasks

def save_task(file, tasks):
    with open(file, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "True" if task['status'] else "False"
            f.write(f"{task['text']}||{status}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            status_icon = "✅" if task['status'] else "❌"
            print(f"{index}. {task['text']} {status_icon}")
    print()

def show_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print()

if __name__ == "__main__":
    TASK_FILE = 'tasks.txt'

    tasks = load_tasks(TASK_FILE)

    headline = "Welcome to the Task Manager"

    while True:
        print(headline.center(50, "="))
        show_menu()
        choice = int(input("Choose an option (1-5): ").strip())

        match choice:
            case 1:
                task_text = input("Enter the task: ").strip()
                if task_text:
                    new_task = {"text": task_text, "status": False}
                    tasks.append(new_task)
                    save_task(TASK_FILE, tasks)
                    print("Task added successfully.")
                else:
                    print("Task cannot be empty.")
            case 2:
                display_tasks(tasks)
            case 3:
                display_tasks(tasks)
                try:
                    task_number = int(input("Enter the task number to mark as completed: "))
                    if 1 <= task_number <= len(tasks):
                        tasks[task_number -1]['status'] = True
                        save_task(TASK_FILE, tasks)
                        print("Task marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            case 4:
                display_tasks(tasks)
                try:
                    task_number = int(input("Enter the task number to delete: "))
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"[{removed_task['text']}] deleted successfully.")
                        save_task(TASK_FILE, tasks)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            case 5:
                print("Exiting the Task Manager. Goodbye!")
                exit()
            
            case _:
                print("Please choose a valid option (1-5).")