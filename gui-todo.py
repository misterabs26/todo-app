from modules import functions as todofunc
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todofunc.get_todos(),
                      key="todos_items",
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button("Edit")

window = sg.Window('My Todo App',
                   layout=[[list_box,edit_button],
                           [label],
                           [input_box,add_button]],
                   font=('Helvetica',12))

def update_window(window_element, updated_value=None):
    if isinstance(updated_value, str):
        updated_value = [updated_value]
        return window[window_element].update(value = updated_value[0])
    if updated_value is None:
        updated_value = []

    return window[window_element].update(values = updated_value)

while True:
    event, values = window.read()

    match event:
        case "Add":
            todo = values["todo"] + "\n"
            todos = todofunc.get_todos()
            todos.append(todo)
            todofunc.write_todos(todos)
            input_box.update("")
            update_window('todos_items',todos)
        case "Edit":
            selected_todo = values["todos_items"][0]
            new_todo = values["todo"]+"\n"
            todos = todofunc.get_todos()
            target_todo_index = todos.index(selected_todo)

            todos[target_todo_index] = new_todo
            todofunc.write_todos(todos)
            input_box.update("")
            update_window('todos_items',todos)
        case 'todos_items':
            update_window('todo', values["todos_items"][0])
        case sg.WIN_CLOSED:
            print("Bye-bye")
            break

window.close()