import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a to-do item.")
input_box = sg.InputText(tooltip='Enter a to-do item.', key="todo")
add_button = sg.Button("Add")
window = sg.Window('My To-Do App', 
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica, 20'))

while True: #denies going directly to close function
    event, values = window.read()
    print(event) #prints label of the button
    print(values) #prints dictionary key, value
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()