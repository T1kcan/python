import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Purple")
clock = sg.Text('', key='clock')
label = sg.Text("Type a to-do item.")
input_box = sg.InputText(tooltip='Enter a to-do item.', key="todo")
add_button = sg.Button("Add",size=10)
#add_button = sg.Button(size=2, image_source="c:/Utils/Work/Python/add.png", mouseover_colors="LightBlue2",
#                       tooltip="Add To-Do", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

# button_labels = ["Close", "Apply"]
# layout = []
# for bl in button_labels:
#     layout.append([sg.Button(bl)])

complete_button = sg.Button("Complete")
#complete_button = sg.Button(size=2, image_source="c:/Utils/Work/Python/complete.png", mouseover_colors="LightBlue2",
#                       tooltip="Complete a To-Do", key="Complete")
exit_button = sg.Button("Exit",size=10)

window = sg.Window('My To-Do App', 
                   layout=[[clock], [label], [input_box, add_button],
                   [list_box, edit_button,complete_button],
                   [exit_button]], font=('Helvetica, 16'))

while True: #denies going directly to close function
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, event) #prints label of the button
    # print(2, values) #prints dictionary key, value
    # print(3, values["todos"]) #prints edit list values
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update('')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                #print("Select an item first!")
                sg.popup("Select an item first!", font=('Helvetica, 16'))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.popup("Select an item first!", font=('Helvetica, 16'))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()