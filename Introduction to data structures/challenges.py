
#* Your solution (python), ChatGPT (java) - Put all of them here
#*-----------------------

# Min & Max of an Array 

arr1 = [1, 345, 234, 21, 56789]
arr2 = [3, 2, 1, 56, 10000, 167]

arr1.sort()
print(f"Min= {arr1[0]}, Max= {arr1[-1]}")

print(f"Min= {min(arr1)}, Max= {max(arr1)}")

minNum = arr1[0]
maxNum = arr1[0]

for num in arr1:
  if minNum > num:
    minNum = num
  if maxNum < num:
    maxNum = num
print(f"Min= {minNum}, Max= {maxNum}")

# -------------------------

# Reverse array order

arr1 = [1, 345, 234, 21, 56789]

# arr1.reverse() # reversed the list itself
# print(arr1)
reversed_arr1 = arr1[::-1]
print(reversed_arr1)
reversed_arr2 = list(reversed(arr1))
print(reversed_arr2)

arr2 = []

for i in range(len(arr1)-1, -1, -1):
  arr2.append(arr1[i])
print(arr2)

# -------------------------

# Reverse array in place

arr1 = [1, 345, 234, 21, 56789]

# arr1.reverse()
print(arr1)

for i in range(len(arr1) // 2):
  temp = arr1[i]
  arr1[i] = arr1[len(arr1) - 1 - i]
  arr1[len(arr1) - 1 - i] = temp

print(arr1)

# -------------------------

# Frequency of element in an array

arr1 = [1, 345, 1, 21, 1]

print(arr1.count(1))

arr1.sort()
counter = 0
for num in arr1:
  if num == 1:  counter += 1
print(counter)

# -------------------------

# Cyclic array rotation by one

arr1 = [1, 345, 234, 21, 56789]

new_arr = []
# new_arr = [arr1[-1]] + arr1[:-1]
print(new_arr)

new_arr.append(arr1[-1])
for i in range(0, len(arr1)-1):
  new_arr.append(arr1[i])
print(new_arr)

# -------------------------

# Cyclic array rotation by one in place

arr1 = [1, 345, 234, 21, 56789]

for i in range(len(arr1)-2, -1, -1):
  temp = arr1[i]
  arr1[i] = arr1[i-1]
  arr1[i-1] = temp

print(arr1)

arr2 = [1, 2, 3, 4, 5]
temp = arr2[len(arr2)-1]

for i in range(len(arr2)-2, -1, -1):
  arr2[i+1] = arr2[i]

arr2[0] = temp
print(arr2)


# -------------------------

# Find the missing number in an array

arr3 = [1, 2, 3, 5]

mis_num = 0
arr3.sort()

# for i, v in enumerate(arr3):
#   if i + 1 != v:
#     mis_num = i + 1
#     break
# print(mis_num)

sum_arr = sum(arr3)
sum_real = 0
for i in range(1,max(arr3)+1):
  sum_real += i
mis_num = sum_real - sum_arr
print(mis_num)

# --------------------------

# Create ArrayList

# Challenge isn't done


# -------------------------

# Stack using ArrayList

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

last_element = stack.pop()

print("Last elemnt = " + str(last_element) + " with delete it.")
print("Last elemnt = " + str(stack[-1]) + " without delete it.")

search = stack.index(3)

print(search)


# -------------------------

# Stack with getMin

print(f"Minimum number in stack = {min(stack)}")

# -------------------------

# Two stacks in array

# Not solved

# -------------------------

# Balanced Brackets

stack = []
opening_brackets = {'(', '[', '{'}
closing_brackets = {')': '(', ']': '[', '}': '{'}
exp_test = ['(', '{', '[', '{' ']', '}', ')']

for char in exp_test:
  if char in opening_brackets:
    stack.append(char)
  elif char in closing_brackets:
    if not stack or stack[-1] != closing_brackets[char]:
      print("False")
      break
    stack.pop()

print(stack)
print(len(stack) == 0)

# -------------------------

# Queue using ArrayDeque methods

# Done with java , Queue challenges

# -------------------------

# Done