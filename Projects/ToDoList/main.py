#   add delete mark as complete view 

import time
import os

task_id = []
tasks_list = []
state_task = []
current_num_id = 0
next_num_id = 0

def add():
    global current_num_id
    global next_num_id

    task = input("Type your task: ")
    tasks_list.append(task)
    state_task.append("Not Done")
    task_id.append(current_num_id)
    next_num_id = current_num_id + 1 
    current_num_id = next_num_id


def delete():
    whichtask = int(input("ID of the task you want to delete: "))

    if whichtask <= len(task_id) and whichtask > 0:
        del tasks_list[whichtask]
        del state_task[whichtask]
        del task_id[whichtask]
        print("The task was successfully deleted !\n")
        time.sleep(2)
    else:
        print("No task found for the ID provided !\n")


def markdone():
    whichtask = int(input("ID of the task you want to mark as done: "))

    if whichtask <= len(task_id) and whichtask > 0:
        state_task[whichtask] = "Done    "


def view():
    
    print("-----------------------------------------------")
    print("| ID  |       Task        |       State       |")
    print("-----------------------------------------------")

    for x in range(0, len(tasks_list)):
        print(f"|  {task_id[x]}  | {tasks_list[x]}             |      {state_task[x]}     |")
    print("-----------------------------------------------")
    print("\n\n")


def mainMenu():
    print("Welcome to the To do List Application !\n")

    while True:
        print("What do you wish to do ?")
        choice = int(input("1. Add a Task \n2. Delete a Task \n3. View all Taskes \n4. Mark a Task as Done \n5. Exit \n"))

        os.system('clear')

        if choice == 1:
            add()
            os.system('clear')            

        elif choice == 2:
            view()
            delete()
            os.system('clear')

        elif choice == 3:
            view()

        elif choice == 4:
            view()
            markdone()
            os.system('clear')

        elif choice == 5:
            break
        else:
            print("You must type a number between 1-4 !\n")
            time.sleep(1)
            os.system('clear')

def main():
    mainMenu()
    

if __name__ == "__main__":
    main()


