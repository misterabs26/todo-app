#from functions import get_todos, write_todos -- importing specific functions
#import functions -- importing the whole module
#from functions import * -- not recommended
#import functions as todofunc -- giving an alias to the module

#importing the module from a directory
from modules import functions as todofunc
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + '\n'

        todos = todofunc.get_todos()
        todos.append(todo.capitalize())
        todofunc.write_todos(todos)

    elif user_action.startswith("show"):
        todos = todofunc.get_todos()

        for i, todo in enumerate(todos):
            print(f"{i+1}. {todo.strip("\n")}")

    elif user_action.startswith("edit"):
        try:
            task_no = int(user_action[5:])
            new_task = input("Enter a new task: ").capitalize()

            todos = todofunc.get_todos()
            todos[task_no - 1] = new_task + "\n"
            todofunc.write_todos(todos)
        except ValueError:
            print("Invalid Command")
            continue

    elif user_action.startswith("complete"):
        try:
            task_no = int(user_action[9:])
            todos = todofunc.get_todos()
            task_index = task_no-1
            removed_task = todos[task_index]
            todos.pop(task_index)

            todofunc.write_todos(todos)

            message = f"Task: '{removed_task.strip("\n")}' is completed"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Please indicate the task number to be marked as completed")
            continue
    elif user_action.startswith("exit"):
        print("Bye-bye")
        break
    else:
        print("Invalid Command")




