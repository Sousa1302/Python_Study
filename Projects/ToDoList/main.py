#   add delete mark as complete view 

import time
import os

task_id = []
tasks_list = []
state_task = []
num_id = 0

def add():
    global num_id
    task = input("Type your task: ")
    tasks_list.append(task)
    state_task.append("Not Done")
    task_id.append(num_id)
    num_id += 1

#Problem here (it doesnt recognize the id given)
def delete():
    whichtask = int(input("ID of the task you want to delete: "))

    if whichtask <= len(task_id) and whichtask > 0:
        del tasks_list[whichtask]
        del state_task[whichtask]
        del task_id[whichtask]
    else:
        print("No task found for the ID provided !\n")


def markdone():
    whichtask = int(input("ID of the task you want to mark as done: "))

    if whichtask <= len(task_id) and whichtask > 0:
        state_task[whichtask] = "Done"

# Problem here ( The id keeps adding so all the tasks have the same id)
def view():
    global num_id

    print("-----------------------------------------------")
    print("| ID  |       Task        |       State       |")
    print("-----------------------------------------------")

    for x in range(0, len(tasks_list)):
        print(f"| {num_id} | {tasks_list[x]}             |      {state_task[x]}     |")
        

def mainMenu():
    print("Welcome to the To do List Application !\n")

    while True:
        print("What do you wish to do ?")
        choice = int(input("1. Add a Task \n2. Delete a Task \nView all Taskes \nMark a Task as Done \n"))

         


def main():
    add()
    #time.sleep(1)
    #os.system('clear')
    view()
    add()
    #markdone()
    view()
    delete()

    

if __name__ == "__main__":
    main()


