import moduleForChallenge3 as mFO
import math
import random
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operation = input("Enter the operation you want to use: ")

if operation == '+':
  print(mFO.add(num1, num2))
elif operation == '-':
  print(mFO.subtract(num1, num2))
elif operation == '*':
  print(mFO.multiply(num1, num2))
elif operation == '/':
  print(mFO.divide(num1, num2))
elif operation == 'power':
  print(math.pow(num1, num2))
elif operation == 'sqrt':
  print(math.sqrt(num1))
elif operation == 'random':
  print(random.randrange(num1, num2))
else:
  print("Your operation is not supported in the program!")

print(f"Done!")

