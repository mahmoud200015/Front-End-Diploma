fruits = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermillion',
]

print("My favorite list of fruits: ")
for fruit in fruits:
  print(str(fruits.index(fruit) + 1) + ". " + fruit.capitalize())

index = 0
while True:
  if (fruits[index] == "nectarines"):
    break
  print(fruits[index].capitalize())
  index += 1