tasks = []

while True:
  option = input("Enter your option from here (add, view, remove, exit): ").lower()

  if option == "add":
    newTask = input("Enter the new task you want to add it: ")
    if newTask not in tasks:
      tasks.append(newTask)
      print("The task is added.")
  elif option == "remove":
    deletedTask = input("Enter the task you want to remove it: ")
    if deletedTask not in tasks:
      print("The task is not exist!")
    else:
      tasks.remove(deletedTask)
      print(f"The task: ({deletedTask}) is removed.")
  elif option == "view":
    if not tasks:
      print("No tasks to display.")
    else:
      print("Your tasks:")
      for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
  elif option == "exit":
    print("Exiting the program. Goodbye!")
    break
  else:
    print("Invalid Option!")
