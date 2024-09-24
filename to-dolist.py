# Initialize an empty to-do list
to_do_list = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    to_do_list.append({"task": task, "status": "pending"})
    print(f'Task "{task}" added.')

# Function to display all tasks
def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task_info in enumerate(to_do_list, 1):
            print(f"{idx}. {task_info['task']} - {task_info['status']}")
        print()

# Function to remove a task by index or task name
def remove_task():
    task_name = input("Enter the task name to remove: ")
    found = False
    for task_info in to_do_list:
        if task_info['task'].lower() == task_name.lower():
            to_do_list.remove(task_info)
            print(f'Task "{task_name}" removed.')
            found = True
            break
    if not found:
        print(f'Task "{task_name}" not found in the list.')

# Optional function to mark a task as completed
def mark_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(to_do_list):
            to_do_list[task_index]['status'] = "completed"
            print(f'Task "{to_do_list[task_index]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Main program loop
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task()
        elif choice == '5':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-5).")

# Run the program
if __name__ == "__main__":
    main()
