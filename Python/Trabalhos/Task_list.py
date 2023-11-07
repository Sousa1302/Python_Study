print("Welcome to the task list!")

tasks = []
show_menu = True

while True:
    if show_menu:
        print("Type 'help' to use the app or 'exit' to quit")
    else:
        print("-------------------------------")
        print("-      Add a task - A         -")
        print("-      Remove a task - R      -")
        print("-      Check a task - C       -")
        print("-      Show all tasks - S     -")
        print("-------------------------------")
    
    help_key = input("-> ")

    if help_key.lower() == "exit":
        print("Program has been terminated.\n")
        break

    if show_menu:
        if help_key.lower() != "help":
            print("Sorry, I don't know what you're talking about!\n")
            continue

    if help_key.lower() == "help":
        show_menu = not show_menu
        continue

    if help_key == "A":
        task_name = input("Insert a task: ")
        tasks.append(task_name)
        print("Okay, your task was created successfully!\n")

    elif help_key == "R":
        print("Task List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        task_index = int(input("Enter the number of the task you want to remove: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number. Please try again.\n")
        else:
            removed_task = tasks.pop(task_index)
            print(f"The task '{removed_task}' was removed successfully!\n")
            show_menu = True  

    elif help_key == "C":
        print("Your task list: ")
        for task in tasks:
            print(tasks)
        input("What task do you wish to check? ")
        print("Okay, your task was checked successfully!\n")
    
    elif help_key == "S":
        print("Task List:")
        for task in tasks: 
            print(task)
    
    else:
        print("Sorry, I don't know what you're talking about!\n")
















