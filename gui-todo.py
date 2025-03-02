from modules import functions as todofunc
import FreeSimpleGUI as sg
import time
import os

# Creates todos.txt file if it does not exist
if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass


sg.theme("Green")

clock = sg.Text(key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todofunc.get_todos(),
                      key="todos_items",
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

buttons = [add_button,edit_button,complete_button,exit_button]

window = sg.Window('My Todo App',
                   layout=[[clock],
                           [list_box],
                           [label],
                           [input_box],
                           [buttons]],
                   font=('Helvetica', 12))

def update_window(window_element, updated_value=None):
    """Updates listbox and input text"""
    element = window[window_element]
    if isinstance(element, sg.Input):
        element.update(value=updated_value)
    elif isinstance(element, sg.Listbox):
        if updated_value is None:
            updated_value = []
        if isinstance(updated_value, str):
            updated_value = [updated_value]
        element.update(values = updated_value)

while True:
    event, values = window.read(timeout=200)

    # Exit immediately if window is closed
    if event == sg.WIN_CLOSED or event == "Exit":
        sg.popup("Bye-bye", text_color="yellow", auto_close=True)
        break

    window["clock"].update(value=time.strftime(f"%b, %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todo = values["todo"].strip()
            todos = todofunc.get_todos()
            todos.append(todo + "\n")
            todofunc.write_todos(todos)
            input_box.update("")
            update_window('todos_items',todos)
        case "Edit":
            try:
                selected_todo = values["todos_items"][0]
                new_todo = values["todo"].strip()
                # checks if there is being inputted
                if new_todo:
                    todos = todofunc.get_todos()
                    target_todo_index = todos.index(selected_todo)

                    todos[target_todo_index] = new_todo + "\n"
                    todofunc.write_todos(todos)
                    update_window('todos_items',todos)
                else:
                    sg.popup("Please enter a valid to-do item.", font=('Helvetica', 15))
            except IndexError:
                sg.popup("Please select an item first.",
                         font=('Helvetica',15))
        case "Complete":
            try:
                selected_todo = values["todos_items"][0]
                todos = todofunc.get_todos()
                target_todo_index = todos.index(selected_todo)

                todos.pop(target_todo_index)
                todofunc.write_todos(todos)
                update_window('todos_items',todos)
                update_window('todo',"")
                # if there still pending todos, the list selection will set to the first item
                if todos:
                    window["todos_items"].update(set_to_index=0)
            except IndexError:
                sg.popup("Please select an item first.",font=('Helvetica',15))
        case 'todos_items':
            update_window('todo', values["todos_items"][0].strip())

window.close()