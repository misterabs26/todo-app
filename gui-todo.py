from modules import functions as todofunc
import FreeSimpleGUI as sg
import time

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
                           buttons],
                   font=('Helvetica',12))

def update_window(window_element, updated_value=None):
    if isinstance(updated_value, str):
        updated_value = [updated_value]
        return window[window_element].update(value = updated_value[0])
    if updated_value is None:
        updated_value = []

    return window[window_element].update(values = updated_value)

while True:
    event, values = window.read(timeout=200)

    # will check if the window is open before updating it else, it will close
    if event == sg.WIN_CLOSED or event == "Exit":
        sg.popup("Bye-bye", text_color="yellow", auto_close=True)
        break
    if window:
        window["clock"].update(value=time.strftime("%b, %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todo = values["todo"] + "\n"
            todos = todofunc.get_todos()
            todos.append(todo)
            todofunc.write_todos(todos)
            input_box.update("")
            update_window('todos_items',todos)
        case "Edit":
            try:
                selected_todo = values["todos_items"][0]
                new_todo = values["todo"]+"\n"
                todos = todofunc.get_todos()
                target_todo_index = todos.index(selected_todo)

                todos[target_todo_index] = new_todo
                todofunc.write_todos(todos)
                input_box.update("")
                update_window('todos_items',todos)
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
            except IndexError:
                sg.popup("Please select an item first.",font=('Helvetica',15))
        case 'todos_items':
            update_window('todo', values["todos_items"][0])


window.close()