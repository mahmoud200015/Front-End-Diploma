# Data structures 

# Effiency -> Time, space
# context switching, garbage collection
# The correct measure of performance is (growth function)
# Operations growth: (Y = n) or (Y = n * n) or (Y = n ** 3)
#                   e.g. (Y = 2n**2 + n + 4)
# Asymptotic Notation: instead of Y = 2n**2 + n + 4 -> O(n**2) big o
# The best and the average case of performance , (O, omega, theta)
# worst case scenario(Big O) = O(n)
# best case scenario(Omega) = O(1)
# average case scenario(Theta) = O(n/2)
# The order of growth functions 
# 1.Fixed operation = O(1)
# 2.Log = O(log(n))
# 3.Linear Function = O(n)
# 4.N Log N = O(n log n)
# 5.Polynomial Function = O(n**2)
# 6.Exponential function = O(2**n)
# 7.Factorial = O(n!)
# 8.Square of n(worst) = O(n**n)

# import numpy as np
# Array Section, Two dimensional array, multi dim

Keys = ["Student Name", "Role No.", "Subject"]
Values = ["Alex", "12345", "Python"]
print(dict(zip(Keys, Values)))


# ArrayLists Section 

# Stack Section - example with python 

from collections import deque
# Creating an empty deque wiht deque class
stack = deque()

# Pushing elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
# print(stack[-1], stack)
# Popping elements from the stack
top_element = stack.pop()  # Removes and returns the top element (3 in this case)
print("Top element:", top_element)

# Accessing the top element without removing it
if stack:
    top_element = stack[-1]
    print("Top element without removing:", top_element)
else:
    print("Stack is empty")


# Queue Section - example with python deque class


# Creating an empty deque
queue = deque()

# Enqueue elements into the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue elements from the queue
front_element = queue.popleft()  # Removes and returns the front element (FIFO)
print("Front element:", front_element)

# Accessing the front element without removing it
if queue:
    front_element = queue[0]
    print("Front element without removing:", front_element)
else:
    print("Queue is empty")


# Done

#? In python from collection import deque
#* deque = Double-Ended Queue (stack and queue based on your behaviour)