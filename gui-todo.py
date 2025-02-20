from modules import functions as todofunc
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
window = sg.Window('My Todo App',
                   layout=[[label],
                           [input_box],
                           [add_button]],
                   font=('Helvetica',12))
while True:
    event, values = window.read()

    match event:
        case "Add":
            todo = values["todo"] + "\n"
            todos = todofunc.get_todos()
            todos.append(todo)
            todofunc.write_todos(todos)
            input_box.update("")
        case sg.WIN_CLOSED:
            print("Bye-bye")
            break

window.close()