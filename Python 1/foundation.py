import keyword;

print("Hello World!")

name = "Mahmoud Ayman"
age = 23
print("My name is " + name + ", My age is", age)
print(type(name), type(age))

print(keyword.kwlist) # print all keywords in python

print(3 // 2) # division without decimal numbers
print(3 ** 2) # pow numbers

print(False == 0)

# one line comment, no multiple in py

if True:
  print("Always Printed")
  print("Second of block lines, INDENTATION")
elif True:
  print("Only for Test")
else:
  print("Never Printed")


def hasJob(state):
  if (state == 'employed'):
    print("OK!")
  return "Returning"

hired = hasJob("employed")
print(hired)
hasJob("unemployed")

def printSum(num1, num2):
  print(num1 + num2)

printSum(12,13)

# function functionName(para) {
#   return;
# }

def function_name(para):
  return

"""
multiline comment
in python 
use three double quotes 
The Only Way
"""

