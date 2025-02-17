from modules import functions as todofunc
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")
window = sg.Window('My Todo App', layout=[[label], [input_box],[add_button]])
window.read()
window.close()