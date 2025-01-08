age = 20
# price = 19.95
# first_name = 'Tamer'
# is_online = True
# print('Hello World', age, price,first_name,is_online)

# name = input('What is your name? ')
# print('Hello '+name)

# birth_year = input('Enter your birth year: ' )
# age = 2024 - int(birth_year)
# print('You are ' + str(age) + ' year old...')

# first = float(input('Enter first number: ') )
# second = float(input('Enter second number: ') )
# sum = first + second
# print('Total is :' + str(sum))

# course = 'Python for beginners'
# print(course.capitalize())
# print(course.upper())
# print(course.lower())
# print(course.find('n'))
# print(course.replace('for', '4'))
# print('Python' in course)

# print(10+4)
# print(10/3)
# print(10//3)
# print(10%3)
# print(10*3)
# print(10**3)

# x = 10
# x = x+3
# x += 3

# price = 25
# print(price > 10 and price < 30)
# print(not price >10 )

# temperature=5
# if temperature > 30:
#     print("It's a hot day")
#     print('Drink plenty of water')
# elif temperature > 20: # [20 - 30]
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print('Done')

# i=1
# while i<=1_000:
#     print(i)
#     i=i+1

# i=1
# while i<=20:
#     print(i * '*')
#     i=i+1

# names=["ali", "veli", "49", "elli"]
# print(names)
# print(names[0])
# print(names[-1])
# print(names[0:3])

# numbers=[1,2,3,4,5]
# numbers.append(7)
# print(numbers)
# numbers.insert(5,6)
# print(numbers)
# numbers.remove(7)
# print(numbers)
# #numbers.clear()
# print(len(numbers))
# print(numbers)

# for item in numbers:
#     print(item)
# #while method:
# i=0
# while i < len(numbers):
#     print(numbers[i])
#     i=i+1

# numbers=range(0, 11, 2)
# print(numbers)
# for number in numbers:
#     print(number)
# for number in range(5):
#     print(number)

# #tuples are constant can not be changed
# numbers=(1,2,3)
# numbers.count

# first = 'John'
# last = 'Bonn'
# msg = f'{first} [{last}] is a developer'
# print(msg)
# print(len(msg))
# print(len(first))
# print(msg.find('p'))
# print(msg.replace('Bonn', 'herhavzundibiaynı'))
# print('herhav' in msg)
# print('lop' in msg)
# print(msg.title())
# print(msg.upper())
# x=10
# import math
# print(math.sin(x))

# print("aa{}aa{}".format("AA",11))
# a=12
# c=10
# b="ali"
# print("a:{} b:{}".format(a,b))
# print("{}".format(a*c))

# def topla(x1,x2):
#     return x1+x2
# print(topla(11,22))

# for i in range(0,3):
#     print(i)
# i=5
# while i<=10:
#     print(i)
#     i+=1

# p={"adi":"Tamer","soyadi":"Bincan"}
# print(p)
# print(p["adi"],p["soyadi"])

# class ogrenci:
#     adi=""
#     yas=0
#     def don(self):
#         return self.adi

# og1=ogrenci()
# og1.adi="Mustafa"
# og1.yas=49
# print(og1.adi, og1.yas)
# print(og1.don())

# try:
#     print("test")
#     a=23/0
# except Exception as e:
#     print("hata aldı:",e)
#     print(e)
# finally:
#     print("kapanıyor")

# matrix = [[j for j in range(4)] for i in range(4)] 
# print(matrix)

# def input_number():
#     return int(input("Enter a number: "))
# input1=input_number()
# print("You entered " +str(input1))

# def my_function(*students):
#   print("The tallest student is " + students[2])

# my_function("James", "Ella", "Jackson")

# a = 0
# def add_three(a):
# 	return a+3

# result = add_three(a)
# print(result)
# def get_odd_func(numbers):
#     odd_numbers = [num for num in numbers if num % 2]
#     return odd_numbers

# print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))

# def my_function(names):
#   for i in names:
#     print(i, end=' ')

# names = ["john", "mark", "emmy"]
# my_function(names)

# def mean_func(list1):
#     return sum(list1) / len(list1)

# print(mean_func([5, 2, 2, 4]))

# def my_function(numbers):
#   for i in numbers:
#     print(i*2+10, end=' ')

# numbers = [1, 2, 3]
# my_function(numbers)

# x = 20
# def my_function():
#   print(x, end=' ')

# my_function()
# print(x, end=' ')

# def my_function(*argv):
#   print(argv)

# my_function('Hello', 'World!')
# for num in range(5, 9):
#    for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break

# prices=[10,20,30]
# total=0
# for item in prices:
#     total += item
# print(f"Total: {total}")

# for x in range(4):
#     for y in range(3):
#         print(f"( {x} , {y} )")

# numbers = [5,2,5,2,2]
# for number in numbers:
#     print(number * "x")

# numbers = [5,2,5,2,2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

#find the biggest number on the list:
# numbers = [1,2,9,7,3,2,5,3,4,5,6]
# # max=0
# # for number in numbers:
# #     if number > max:
# #         max = number
# # print(max)

# # remove duplicates:
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# #digit to words:
# numbers={'1':"one", '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
# output=''
# phone_number=input('Enter your phone number: ')
# for number in phone_number:
#     output += numbers.get(number, '!') + ' '
# print(output)

# message = input('> ')
# words = message.split(' ')
# emojis = {
#     ':)': 'gülen surat',
#     ':(': 'somurtan surat'
# }
# output  = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)

#functions:
# def greet_user(name):
#     print(f'Hi {name}!')
#     print('Welcome aboard')

# print('start')
# greet_user('John')
# greet_user('Marry')
# print('finish')

# def square(number):
#     return number * number  

# print(square(3))

#functions:
# def emoji_convertor(message):
#     words = message.split(' ')
#     emojis = {
#         ':)': 'gülen surat',
#         ':(': 'somurtan surat'
#     }
#     output  = ''
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output

# message = input('> ')
# print(emoji_convertor(message))

#exceptions:
# try:
#     age = int(input('Age: '))
#     income = 2000
#     risk = income / age
#     print(risk)
# except ZeroDivisionError:
#     print('Yaş sıfır olabilemez!')
# except ValueError:
#     print('numara girecen olm')

#classes:
#naming convention, bu classda adını tanımladık, talk ile ekrana adını yazdırdık.
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, I'am {self.name}")

# john = Person("John Smith")
# john.talk()
# bob = Person("Bob Smith")
# bob.talk()

import random
# members=["ali", "veli", "kırkdokuz", "elli"]
# leader=random.choice(members)
# print(leader)

# for i in range(3):
#     print(random.random())
#     print(random.randint(10,30))

# class Dice:
#     def roll(self):
#         first=random.randint(1,6)
#         second=random.randint(1,6)
#         return first,second
    
# dice=Dice()
# print(dice.roll())

#file path library:
from pathlib import Path # büyük harf ile başladığından class olduğunu anlıyoruz.

# path = Path("TuranCyberHub1")
# print(path.exists())
# print(path.absolute())
# #print(path.mkdir())
# #print(path.rmdir())

path = Path()
#for file in path.glob('*.py'):
for file in path.glob('*.xlsx'):
    print(file)