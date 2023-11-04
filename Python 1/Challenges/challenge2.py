num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter the operation you want to calculate from..(+, -, *): ")

if operation == '+':
  print("Result is ", num1 + num2)
elif operation == '-':
  print("Result =", num1 - num2)
elif operation == '*':
  print("Result is ", num1 * num2)
else:
  print("We don't support this operation")


print("Thanks for using our software")