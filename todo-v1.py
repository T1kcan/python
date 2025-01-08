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
while True:
    user_action = input("Type add, show, edit, complete or exit :")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            #todos.append(todo) #oluşturduğumuz boş list obselete now
            # file = open('C:/Utils/Work/Python/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            # with ile aynı okumayı yapabiliriz:
            with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            #file = open('Work/Python/todos.txt', "w")
            # file = open(r"C:/Utils/Work/Python/todos.txt", "w")
            # file.writelines(todos)
            # file.write('test to test\n')
            # file.close()

            with open(r"C:/Utils/Work/Python/todos.txt", "w") as file:
                file.writelines(todos)



        case 'show' | 'display' | 'Show' | 'Display':
            #print(todos)
            # file = open('C:/Utils/Work/Python/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
                todos = file.readlines()


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
                
        case 'edit' | 'Edit':
            number = int(input('Number of todo to edit: '))
            number = number -1
            with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
                todos = file.readlines()
            print('existing todos:', todos)
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            print('new todos now:', todos)
            with open(r"C:/Utils/Work/Python/todos.txt", "w") as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('C:/Utils/Work/Python/todos.txt', 'r') as file:
                todos = file.readlines()
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(number - 1)

            with open(r"C:/Utils/Work/Python/todos.txt", "w") as file:
                file.writelines(todos)
            
            message = f"Todo {item} was removed from the list"
            print(message)

            print(f"There are {len(todos)} item(s) left in the list...")

        case 'exit' | 'quit':
            break
        case _: #whatever:
            print('Ne yazıyon olum, çık çık çık')
print('Bye!')