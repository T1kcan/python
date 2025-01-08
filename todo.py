# user_prompt = 'Enter a todo: '

# todos = []
# while True:
#     todo = input(user_prompt)
#     todos.append(todo)
#     print(todos)

# filenames = ["ali.1.txt","veli.1.txt", "deli.1.txt"]
# for filename in filenames:
#     filename = filename.replace('.', '-', 1)
#     print(filename)

# usernames = ['the blueman', 'sorted hedgehog', 'infinite lagoon']

# for username in usernames:
#     username = username.replace(' ', '_')
#     print(username)

# mood = "sad"
# strength = 1.12
# rank = 1

# for item in [mood, strength, rank]:
#     print(type(item))

# todos = ["clean", "throw", "do"]
# for index, item in enumerate(todos):
#     print(index, item)
# products = ['table', 'chair', 'door']
# for index, item in enumerate(products):
#     print(index, ":", item)

# filenames = ['document', 'report', 'presentation']
# for index, filename in enumerate(filenames):
#     row = f"{index}-{filename}.txt"
#     print(row)

# filenames = ['document', 'report', 'presentation']
# for index, filename in enumerate(filenames):
#     print(f"{index}-{filename.capitalize()}.txt")

# for i, j in enumerate('Hello'):
#     print(i,j)

# mystring = "ali"
# mylist = ["ali", "veli", "deli"]
# print(len(mystring))
# print(len(mylist))

# waiting_list =  ["sen", "ben", "john"]
# waiting_list.sort()
# for index, item in enumerate(waiting_list):
#     row = f"{index + 1}.{item.capitalize()}"
#     print(row)

#todos = []
# def get_todos():
#     with open('C:/Utils/Work/Python/todos.txt', 'r') as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
from functions import get_todos, write_todos
#import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit :")
    #user_action = user_action.strip()

    #match user_action:
    #    case 'add':
    #if 'add' in user_action or 'new' in user_action or 'more' in user_action:
    if user_action.startswith('add'):
        #todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:] + '\n'
        #todos.append(todo) #oluşturduğumuz boş list obselete now
        # file = open('C:/Utils/Work/Python/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        # with ile aynı okumayı yapabiliriz:

        # with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
        #     todos = file.readlines()
        #todos = get_todos()
        todos = get_todos() #(C:/Utils/Work/Python/todos.txt')
        todos.append(todo)

        #file = open('Work/Python/todos.txt', "w")
        # file = open(r"C:/Utils/Work/Python/todos.txt", "w")
        # file.writelines(todos)
        # file.write('test to test\n')
        # file.close()

        # with open(r"C:/Utils/Work/Python/todos.txt", "w") as file:
        #     file.writelines(todos)
        write_todos(todos) #, "C:/Utils/Work/Python/todos.txt")



        # case 'show' | 'display' | 'Show' | 'Display':
    #elif 'show' in user_action:
    elif user_action.startswith('show'):
        #print(todos)
        # file = open('C:/Utils/Work/Python/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        # with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
        #     todos = file.readlines()
        #todos = get_todos()
        todos = get_todos() #('C:/Utils/Work/Python/todos.txt')

        #print fonksiyonu \n eklediği için iki satır boşluk oluyor. Çözüm yeni list oluştur:
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # 2'nci yöntem list comprehension. creates new list on the fly:
        #new_todos =  [item.strip('\n') for item in todos]
    
        for index, item in enumerate(todos): #todos ->new_todos
            item = item.title()
            # 3'ncü yöntem direk loopun içinde itemı striplemek:
            item = item.strip('\n')
            #print(index,"-",item)
            row = f"{index + 1}.{item}"
            print(row)

    #    case 'edit' | 'Edit':
    #elif 'edit' in user_action:
    elif user_action.startswith('edit'):
        try:
            #number = int(input('Number of todo to edit: '))
            number = int(user_action[5:])
            number = number -1

            # with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
            #     todos = file.readlines()
            #todos = get_todos()
            todos = get_todos() #('C:/Utils/Work/Python/todos.txt')

            print('existing todos:', todos)
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            print('new todos now:', todos)
            # with open(r"C:/Utils/Work/Python/todos.txt", "w") as file:
            #     file.writelines(todos)
            write_todos(todos) #, "C:/Utils/Work/Python/todos.txt")

        except ValueError:
            print("Your command is not valid")
            # user_action = input("Type add, show, edit, complete or exit :")
            # user_action = user_action.strip()
            continue
        #case 'complete':
    #elif 'complete' in user_action:
    elif user_action.startswith('complete'):
        #number = int(input("Number of the todo to complete: "))
        try:
            number = int(user_action[9:])

            # with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
            #     todos = file.readlines()
            #todos = get_todos()
            todos = get_todos() #('C:/Utils/Work/Python/todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            # with open(r"C:/Utils/Work/Python/todos.txt", "w") as file:
            #     file.writelines(todos)
            write_todos(filepath="C:/Utils/Work/Python/todos.txt", todos_arg=todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

            print(f"There are {len(todos)} item(s) left in the list...")
        except IndexError:
            print("There is no item with that number.")
            continue
        #case 'exit' | 'quit':
    #elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        break
        #case _: #whatever:
    else: #'other' in user_action:
        print('Ne yazıyon olum, çık çık çık')
print('Bye!')