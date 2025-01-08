# file = open('whatever.txt', 'w')
# file.write('the text context of the write method\n alo')
# file.close

# file = open('whatever.txt', 'r')
# file.read()
# file.close()

# file = open("bear.txt", "r")
# content = file.read()
# print(content)

# file = open("essay.txt", "r")
# content = file.read()
# print(content.title())

# file = open("essay.txt", "r")
# content = file.read()
# print(len(content))

# file = open("essay.txt", "r")
# content = file.read()
# print(f"The file contains {len(content)} characters.")

# file = open("file.txt", "w")
# file.write("snail")
# file.close()

# The zip() Function
# In the coding area, we have defined two lists. Each country in the first list should be written in a new file corresponding to the name in the filenames list. So, "Albania" should be written in a new a.txt file, "Belgium" in a new "b.txt" file and so on.

# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
# for country, filename in zip(countries, filenames):
#     file = open(f"{filename}", "w")
#     file.write(country)
#     file.close()

# Creating Multiple Text Files
# In the coding area, we have defined a list of countries. Add some code that uses a for loop to generate a text file for each country (e.g., "Albania.txt", "Belgium.txt", and so on).

# Each file should have its country name as content (e.g., Albania.txt has Albania as content).

# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# for country in countries:
#     file = open(f"{country}.txt", "w")
#     file.write(country)
#     file.close()


# 1. prompts the user to enter a new member.
# 2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:

# John Smith
# Sen Lakmi
# Sono Octonot
# Solomon Right

# member = input("Add a new member: ")

# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()

# existing_members.append(member + "\n")

# file = open("members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()

# Open your computer IDE and place the following in a Python file:
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# Then, create a program that:
# 1. generates multiple text files by iterating over the filenames list,
# 2. and writes the text Hello  inside each generated text file.

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()


# filenames = ['a.txt', 'b.txt', 'c.txt']

# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)

# file = open("data.txt", 'w')

# file.write("100.12\n")
# file.write("111.23\n")

# file.close()

# contents = ["seviyorum ama kimi",
#            "en tatlı birisini",
#            "nasıl anlatsam sana",
#            "ilk harflerine baksana"]
# filenames = ["file1.txt",
#              "file2.txt",
#              "file3.txt",
#              "file4.txt"]
# for content, filename in zip(contents, filenames): #enumarate gibi ama editable
#     file = open(f"C:/Utils/Work/Python/test/{filename}", "w")
#     file.write(content)
#     file.close()

# filenames = ["1.doc","1.report","1.presentation"]
# filenames = [filename.replace('.','-') + '.txt' for filename in filenames]
# print(filenames)

# names = ["john smith", "jay santi", "eva kuki"]
# names = [name.title() for name in names]
# print(names)

# The output of your code should be as below:
# [9, 11, 11]
# usernames = ["john 1990", "alberta1970", "magnola2000"]
# usernames = [len(name) for name in usernames]
# print(usernames)

# user_entries = ['10', '19.1', '20']
# user_entries = [float(entries) for entries in user_entries]
# print(user_entries)

# numbers = [10, 20, 30]
# numbers = [number * 2 for number in numbers]
# print(numbers)

# user_entries = ['10', '19.1', '20']
# user_entries = [float(entries) for entries in user_entries]
# ii=0
# for i in user_entries:
#     ii += i
# print(ii)

# temperatures = [10, 12, 14]
# temperatures = [str(i) + '\n' for i in temperatures]
# file = open("file.txt", 'w')

# file.writelines(temperatures)

# with open("essay.txt", 'r') as file:
#     content = file.read()
# nr_chars = len(content)
# print(nr_chars)

# languages = ['English', 'German', 'Spanish']

# for language in languages:
#     with open(f"{language}.txt", "w") as file:
#         file.write(language)

# with open("story.txt", "r") as file:
#     content = file.read()
# with open("story_copy.txt", "w") as file2:
#     file2.write(content)

# with open("file.txt", 'r') as file:
#     content = file.read()

# print(content)
# print(len(content))

# password = input("Enter your password: ")
# if len(password) >= 7:
#     print("Great password there!")
# else:
#     print("Your password is weak.")

# password = input("Enter your password: ")
# if len(password) > 7:
#     print("Great password there!")
# elif len(password) == 7:
#     print("Password is OK, but not too strong")
# else:
#     print("Your password is weak.")

# day_temperatures = {"morning":22.1, "noon":29.1, "evening":19.1}
# print(day_temperatures.values())
# day_temperatures = {"morning": (22.1, 19.2, 21.1), "noon": (29.1, 23.3, 22.1), "evening": (19.1, 18.9, 19.0)}
# print(day_temperatures.values())

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[1:4])
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
 
# perimeter = (length + width) * 2
# area = length * width
 
# print("Perimeter is", perimeter)
# print("Area is", area)
 
# if perimeter < 14 and area > 10:
#     print("OK")
# else:
#     print("NOT OK")

# try:
#     width = float(input("Enter rectangle width: "))
#     lenght = float(input("Enter rectangle lenght: "))

#     if width == lenght:
#         exit("That looks like a square")
#     area = width * lenght
#     print(area)
# except ValueError:
#     print("Please enter a number.")

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
    
#     percentage = value/total_value * 100
#     print(percentage)
# except ValueError:
#     print("You need to enter a number. Run the program again.")

# try:
#     # Prompt the user to enter the total value and convert it to a float
#     total_value = float(input("Enter total value: "))
#     # Prompt the user to enter the value and convert it to a float
#     value = float(input("Enter value: "))
#     # Calculate the percentage using the formula value/total_value * 100
#     percentage = value / total_value * 100
#     # Print the calculated percentage
#     print(f"That is {percentage}%")
# except ValueError:
#     # Handle the case when the user doesn't enter a number
#     print("You need to enter a number. Run the program again.")

# try:
#     # Prompt the user to enter the total value and convert it to a float
#     total_value = float(input("Enter total value: "))
 
#     # Prompt the user to enter the value and convert it to a float
#     value = float(input("Enter value: "))
 
#     # Calculate the percentage using the formula value/total_value * 100
#     percentage = value / total_value * 100
 
#     # Print the calculated percentage
#     print(f"That is {percentage}%")
# except ZeroDivisionError:
#     # Handle the case when the user doesn't enter a number
#     print("Your total value cannot be zero.")

# colors = [11, 34, 98, 43, 45, 54, 54]

# for color in colors:
#     if color > 50:
#         print(color)

# passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]

# for password in passwords:
#     if len(password) < 8:
#         print(password)

# filenames = ["report.txt", "downloadst.txt", "success.txt", "folders.txt"]

# for filename in filenames:
#     file1 = filename.strip('txt').strip('.')
#     print(file1)

# filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

# for filename in filenames:
#     file1 = filename.strip('txt').strip('.')
#     file1 = file1.title()
#     print(file1)

# waiting_list = ["john", "marry"]
# name = input("Enter name: ")

# try:
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
# except ValueError:
#     print(f"{name} is not in the list.")

# def format_filename():
#     filename = "report.txt"
#     filename = filename[0:-4].title()
#     return filename
    

# ali = format_filename()
# print(ali)

# def square_number():
#     number = 5
#     number = number ** 2
#     return number
    
# ali = square_number()
# print(ali)

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#     return maximum
    
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
 
# print(fahrenheit)

# def get_average():
#     x = "hello"
#     return x.capitalize()
 
 
# print(get_average())

# def greet(message):
#     new_message = message.capitalize()
#     return new_message

# #greeting = greet("hello")
# user_entry = input("What greeting do you want? ")
# greeting = greet(user_entry)
# print(greeting)

# message = "5 12"
# odev = "hani-o-saçlarına"
# print(message.split(" "))
# odev = odev.split("-")
# print(odev)

# def liters_to_m3(liters):
#     liters = int(liters) / 1000
#     return liters
    
# def greeting(person):
#     return f"Hi {person}"

# print(greeting("tamer"))

# def foo(name):
#     # Return a greeting message with the provided name
#     return f"Hi {name}"

# def foo(s1, s2):
#     # Concatenate the two provided strings
#     return s1 + s2

# def concanates(first, second):
#     conjuction = first + second
#     return conjuction

# ali = concanates("ali", "weli")
# print(ali)

# def greeting(person):
#     return "Hi" + " " + person.capitalize()
    
# print(greeting("tamer"))

# def foo(name):
#     return f"Hi {name.title()}"

# print(foo("tamer"))

# def speed(distance, time):
#     return distance / time
    
# print(speed(200, 4))

# def prepare(text):
#     text = text.title()
#     text = text.strip()
#     return text
    
# print(prepare("hello    "))

# def circle_ara(r):
#     pi = 3.14
#     area = 2*pi * r**2
#     return area

# print(circle_ara(2))

# def get_age(year_of_birth, current_year=2025):
#     age = current_year - year_of_birth
#     return age
    
# print(get_age(1976))

# def get_nr_items(user_input):
#     list = user_input.split(",")
#     return len(list)

# print(get_nr_items("john, lisa, teresa"))

# def square_area(sayi):
#     area = sayi * sayi
#     return area

# print(square_area(7))

# def temperature(degree):
#     if float(degree) > 7:
#         message = "Warm"
#     elif float(degree) <= 7:
#         message = "Cold"

#     return message
    
# print(temperature(7))

# def foo(temperature):
#     if temperature > 7:
#         # If the temperature is greater than 7, it is considered warm
#         return "Warm"
#     else:
#         # If the temperature is not greater than 7, it is considered cold
#         return "Cold"

# def char_count(ifade):
#     if len(ifade) < 8:
#         return False
#     else:
#         return True
        
# print(char_count("mypass"))
# print(char_count("mylongpassword"))

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
    
  
# time = calculate_time(100)
# print(time)

# def water_state(temperature):
#     if temperature <= 0:
#         return "Solid"
#     elif temperature > 0 and temperature < 100:
#         return "Liquid"
#     elif temperature > 100:
#         return "Gas"


# FREEZING_POINT = 0
# BOILING_POINT = 100

# def water_state(temperature):
#     if temperature <= FREEZING_POINT:
#         return "Solid"
#     elif FREEZING_POINT < temperature < BOILING_POINT:
#         return "Liquid"
#     else:
#         return "Gas"
# print(water_state(170))

# def foo(temperature):
#     if temperature > 25:
#         return "Hot"
#     elif 15 < temperature < 25:
#         return "Warm"
#     else:
#         return "Cold"
        
# print(foo(15), foo(16), foo(25))

# def count(phrase):
#     return phrase.count('.')

# #from functions import count
# nr_of_periods = count("Trees are good. Grass is green.")
# print(nr_of_periods)

# import random

# # Get two numbers from the user and covert them to integers
# lower_bound = int(input("Enter the lower bound: "))
# upper_bound = int(input("Enter the upper bound: "))

# # Pick a random int using randint()
# rand = random.randint(lower_bound, upper_bound) 

# print(rand)

def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    parts = user_input.split(" ")
    
    # Store the two values in variables 
    lower_bound = int(parts[0])
    upper_bound = int(parts[1])
    
    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}

#from parsers import parse 
import random
 
# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")
 
# Parse the user string by calling the parse function
parsed = parse(user_input)
 
# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
 
print(rand)


