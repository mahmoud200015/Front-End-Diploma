list1 = ["ali", "ahmed", "mohamed"]
list1.insert(2, "alaa")
print(list1)

# ---------------------

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# ! very important

x = 200
print(isinstance(x, int))

# Short Hand If
if 10 > 20: print("a is greater than b")

# The pass Statement
if False: pass

for x in range(2, 30, 3):
  print(x)

for x in [0, 1, 2]:
  pass
# not like in other programmign language we couldn't make 
# if, for is empty we put (pass)

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

from collections import deque

queue = deque()

print(queue)

# Plan for project o-x , prepare files and libraries



