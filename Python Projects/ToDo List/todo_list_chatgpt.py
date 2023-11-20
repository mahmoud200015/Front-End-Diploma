def add_task(todo_list):
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added.")


def view_tasks(todo_list):
    if not todo_list:
        print("No tasks to display.")
    else:
        for task in todo_list:
            print(task)


def remove_task(todo_list):
    if not todo_list:
        print("No tasks to remove.")
    else:
        task = input("Enter a task: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")


todo_list = []

while (True):
    user_action = input("Enter an option (add, view, remove, exit): ")

    if (user_action == "add"):
        add_task(todo_list)
    elif (user_action == "view"):
        view_tasks(todo_list)
    elif (user_action == "remove"):
        remove_task(todo_list)
    elif (user_action == "exit"):
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid command")
