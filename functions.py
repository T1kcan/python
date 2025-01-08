FILEPATH = 'Work/Python/todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in to the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

print(__name__)

if __name__ == "__main__":
    print("Hello")
    print("If you see this line it means that the function code file is direcly called, not by import...")
    print("__name__ value is being printed as function when called as import function, when run directly it remain as __main__ in this code block...")