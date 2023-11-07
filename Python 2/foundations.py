# # notes
# """
# multiline comment
# in python 
# use three double quotes 
# The Only Way
# """

# x, y, z = 1, 2, 3
# print(z, y, x)

# v = y = z = "one value"
# print(v, y, z)

# names = ["ali", "mahmoud", "nada"]
# x, y, z = names
# print(z)

# x = "ali"
# def testVar():
#   global x 
#   x = "ahmed"
#   print(x)
# testVar()
# print(x)

# str, int, float, complex, bool
# list, tuple, range
# dict, set, frozenset
# bytes, bytearray, memoryview
# type(None)

# string = str("ali")
# number = int(10)
# boolean = bool(True)


# # Collections: list, dictionary

# # list
# colors = ["red", "yellow", "blue", "green"]
# print(colors.pop())
# print(colors)

# # dict
# phoneBook = {
#   "ahmed": "010",
#   "ali": "011",
#   "mahmoud": "012",
#   "12": number,
# }
# print(sorted(list(phoneBook.keys())))
# print(phoneBook)

# my_dict = {'fruits': ['apple', 'banana', 'cherry'], 'count': [3, 2, 5]}
# print(my_dict)

# print("cba".split())

# # Iterations

# numbers = [2, 3, 4, 5]

# for num in numbers:
#   print(num, numbers[numbers.index(num)])

# counter = 5
# while counter < 100:
#   print(counter)
#   counter += 25

# # Using external code

# import random
# print(random.randrange(1, 20))

# from Challenges import challenge2
# # print(challenge2.fruits)

# import math
# print(math.pi)
# print(math.sqrt(4))
# print(math.pow(2, 3))
# print(math.fabs(-3.5))
# print(math.floor(10.2))
# print(math.ceil(10.2))

# # import turtle
# from turtle import *
# # color('red', 'yellow')
# # begin_fill()
# # while True:
# #   forward(200)
# #   left(170)
# #   if abs(pos()) < 1:
# #     break
# # end_fill()
# # done()


# # Working with strings

# myName = "Mahmoud Ayman"
# myAge = 23
# result = "Welcome " + myName
# result += ". Your age is " + str(myAge)
# print(result)

# result = f"Welcome {myName}. Your age is {myAge}." # string interpolation
# print(result)

# print(myName.capitalize())
# print(myName.lower())
# print(myName.find("Ayman"))
# print(myName.replace("Ayman", "Abdalmoaz"))
# print(myName[8:])
# print(myName.split(" "))
# print(myName.strip())
# print(myName.count("a"))
# print(myName.swapcase())
# print(myName.index("A"))


# import re
# phrase = "ahmed 283 years old and mohamed 30 years and sara is 23 yeaers old"
# print(re.sub("(\w+) \d+", "myName", phrase))
# print(re.match("\w*\s", phrase))

# # Planning a program

# # style guide for python: PEP 8
# # style guide for javascript: airbnb

# # ! writing pseudocode is the first step before writing code

# # inputs and outputs

# valuesFile = open("./values.txt", "rt")
result = ""

# try:
#     with open("./output.txt", "rt") as outputFile:
#         print("Start reading from file")
#         for line in outputFile:
#             print(line)
#             result += line
#         print(result)
# except FileNotFoundError:
#     print("The file 'output.txt' was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")


valuesFile = open("values.txt", "rt")
outputFile = open("output.txt", "wt")
print("Start reading from file")
sum = 0
for line in valuesFile:
    sum += int(line)
    print(line.rstrip(), file=outputFile)
print("Sum: " + str(sum), file=outputFile)
outputFile.close()
print("I am done")

import os

file_path = './output.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Continue processing the file
else:
    print(f"The file '{file_path}' does not exist.")


# # with open("values.txt", "rt") as file:
#   # file.write("This is new")

# # for line in valuesFile:
# #   print(line)