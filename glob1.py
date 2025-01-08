from glob import glob

myfiles = glob("*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())

