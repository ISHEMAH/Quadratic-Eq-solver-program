# price = 10
# rating = 8.8
# name = 'hugues'
# is_published = False
# print(is_
# published)

# name = 'John Smith'
# age = 20
# is_new = True
#
# name = input('What is your name ? \n')
# print('Hey, ' + name)
# color = input('What is your favorite color? \n')
# print(name +'\'s favorite color is '+ color )

# birth_year = input('What is your birth year:\n')
# print(type(birth_year ))
# age = 2023 - int(birth_year)
# print(age)

# grams = input('Enter grams\n')
# kilograms = int(grams) * 1000
# print(kilogram)

# course = "Python's course for beginners"
# course = 'python course for "beginners"'

# course = '''hey
# hey
# hey
# hey
# hey
# hey
# hey
# '''
# print(course)

# course = "Python's course for beginners"
# print(course[9:15])

# course = "Python's course for beginners"
# another = course[:]
# print(another)
# first = 'hugues'
# last = 'ish'
# msg = f'{first} [{last}] is a coder'
# print(msg)

# course = 'i am hugues'
# # print(course.upper())
# # print(course.replace('hugues','ishema'))
# # print('hugues' in course)
#
# # print(7 ** 5)
#
# x= 10
# x-=6
#
# print(x)

# import math
#
# print(math.exp(7))

# is_hot = False
# is_cold = False
# if is_hot:
#     print('It,s a hot day')
#     print('Drink a lot of water')
# elif is_cold:
#     print("It's a cold day")
#     print("Wear a coat")
# else:
#     print("It's a lovely day")
# print('enjoy your your day')

# is_adult = True
# is_rwandan = False
#
# if is_adult or is_rwandan:
#     print("Eligible to vote")
# else:
#     print('not eligible to vote')
# weight = input("Weigth: ")
# initial = input("(L)bs or (k)g: ")
# if initial.lower() == 'l':
#     final = int(weight)*0.45
#     print(f"Your weight is {final} Kg\n")
# elif initial.lower() == 'k':
#     final = int(weight)/0.45
#     print(f"Your weight is {final} bs\n")
# else:
#     print('Invalid character')

# secretnumber = 9
# counter = 0
# limit = 3
# while counter < limit:
#     guess = int(input('Guess: '))
#     counter += 1
#     if guess == secretnumber:
#         print("You guested right")
#         break
#     # elif not guess == secretnumber and counter == 3:
#     #     print('you failed')
# else:
#     print('you failed')



# i = 1
# while i < 400:
#     command = (input('>')).lower()
#     if command == 'help':
#       print('''
#     start - to start the car
#     stop - to stop the car
#     quit - to quit''')
#
#     elif command == 'start' :
#        print('car started')
#     elif command== 'stop':
#        print('car stopped')
#     elif command == 'quit':
#         break
#     else:
#      print('invalid')

# for item in range(5,10,3):
#     print(item)

# prices = [10,20,30]
#
# for item in prices:
#     item += item
# print(f"the total is {item}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

# numbers = [2, 2, 2, 2, 5]
# i = 0
# for current in numbers:
#     current = numbers[i]
#     i += 1
#     print('x'*current)
# for item in numbers:
#     output = ''
#     for count in range(item):
#         output += 'x'
#     print(output)

# numbers = [10, 9, 13, 15, 25, 1]
# max = numbers[0]
# for number in numbers:
#     if max < number:
#         max = number
# print(max
# numbers = [9, 4, 6, 5, 6, 5, 7]
# numbers.remove(6)
# numbers.clear()
# x = 0
# for number in numbers:
#     for number in numbers:
        # if number not == number:
# coordinates = (1,2,3)
# # x = coordinates[0]
# x,y,z = coordinates
#


# customer = {
#      "name":"john",
#      "age": 30,
#      "is_male":True
#  }
#
# print(customer.get("age"=
# number = input("number")
# integers = {"0":"zero",
#             "1":"one",
#             "2":"two",
#             "3":"three",
#             "4":"four",
#             "5":"five",
#             "6":"six",
#             "7":"seven",
#             "8":"eigth",
#             "9":"nine",
#             }
output = ""



# for ch in number:
#      output += integers.get(ch) + " "
#
# print(output)

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)":"😁",
#     ":(":"😔",
#     "<3":"💓"
# }
#
# for word in words:
#     output += emojis.get(word, word) + " "
#
# print(output)
# name = 'hugues'
# def greet_user(name):
#     print(f'Hey {name}')
#     print('Welcome aboard')
# greet_user('hugues')
# greet_user('jonn')

# def square(number):
#     return number*number
# result =  square(3)
# print(result)]


# def emoji(message):
#     words = message.split(" ")
#     output = ''
#     emojis = {
#         ":)": "😁",
#         ":(": "😔"
#     }
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
# message = input(">")
# result = emoji(message)
# print(result)
# try:
#     age = int(input("Age: "))
#     income = 2000
#     risk = income / age
#     print(risk)
# except ZeroDivisionError:
#     print("Value cant be zero")

# class Point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y = y
#
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# point1 = Point()
# point1.x = 10
# print(point1.x)
# point1.draw()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print(f"Heyy there Iam {self.name} and Im {self.age} old")
#
# john = Person("John smith","15")
# john.talk()
#
# bob = Person("Bob cross","21")
# bob.talk()

# class Mammal:
#     def walk(self):
#         print("walk")
#
# class Dog(Mammal):
#   def bark(self):
#       print("bark")
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
# dog1 = Dog()
# dog1.walk()
# dog1.bark()

# import converters
# from converters import kg_to_lbs
# kg_to_lbs(100)
# converters.
# print(converters.kg_to_lbs(70))


# def find_max(numbers):
#     max = numbers[0]
#     for number in numbers:
#         if max > number:
#             max = number
#     return max
# print(max)
# numbers = [10,3,2,9,13]
# # max = find_max(numbers)
#
# print(max(numbers))
# from ecommerce import shipping
# shipping.calc_shipping()
# import random
#
# for i in range(3):
#     print(random.randint(10,19))
# members = ["mary","mosg","hugues"]
# leader = random.choice(members)
# print(leader)

# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())

# import openpyxl as xl
# from openpyxl.chart import  BarChart, Reference
# filename = input('input file name')
# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#     for row in range(2, sheet.max_row+1):
#         cell = sheet.cell(row , 3)
#         corrected_price = cell.value *0.9
#         corrected_price_cell = sheet.cell(row , 4)
#         corrected_price_cell.value = corrected_price
#     values = Reference(sheet, min_row=2,
#               max_row=sheet.max_row,
#               min_col=4,
#               max_col=4)
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#     wb.save(filename)

# hugues = set(("ishema","mudahinyuka"))
#
# # for x in hugues:
# #     print(x)
#
# # print(len(hugues))
# hugues.remove("ishema")
# hugues.add("ishema")
# hugues.discard("hugu")
#
# print(hugues)
# hugues = {
#     "age":15,
#     "residence":"kigali",
#     "school":"RCA"
# }
# hugues["favcolor"] = "green"
# hugues.popitem()
#
# for x,y in hugues.items():
#     print(x,y)

# def mult(x):
#     return 5*x
# print(mult(3))

# def fact(n):
#     if n==1 or n==0:
#         return 1
#
#     elif n<0:
#         return "Use a positive number"
#
#     else:
#         return n*fact(n-1)
#
# print(fact(0))
# class MyClass:
#     x = 5
# hu = MyClass()
#
# print(hu.x)

# class Person:
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#
#     def greet(self):
#         print("hey my name is "+ self.name)
# person1 = Person("hugues",15)
#
# person1.greet()

# import json
#
# x = '{"name":"hugues","age":15}'
#
# y = json.loads(x)
#
# print(y["age"])
# import re
#
# txt = "The rain in Spain"
#
# x = re.search("^The.*Spain$",txt)
#
# if (x):
#     print(txt)
# else:
#     print("no such file")
# txt = "The rain in spain"
#
# x= re.sub("spain","Rwanda",txt)
#
# print
# price = 40000
# txt = "The new Air jordan costs {:.2f} RWF"
# print(txt.format(price))


num = input("Enter a number:\n")
number = int(num)


def factorial(digit):
    if digit == 0 or digit == 1:
        return 1
    elif digit < 0:
        return "Use a positive number"
    else:
        while digit >=1:
            fact = digit * factorial(digit - 1)
            digit -= 1
            return fact

print("The factorial of "+num+" is "+ str(factorial(number)))

