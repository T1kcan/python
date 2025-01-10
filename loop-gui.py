import FreeSimpleGUI as sg

button_labels = ["Add", "Edit", "Apply", "End", "Cancel", "Undo", "Redo"]
layout = []
for label in button_labels:
    layout.append([sg.Button(label)])

label = sg.Text("Type a to-do item.")
input_box = sg.InputText(tooltip='Enter a to-do item.', key="todo")
#add_button = sg.Button("Add")

window = sg.Window('My To Do App', layout=[input_box, layout], font=('Helvetica, 14'))
window.read()
window.close()