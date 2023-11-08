class Cat:
  def __init__(self, name, type, color, age,
              walkingSpeed, runningSpeed, doesMeow):
    self.name = name
    self.type = type
    self.color = color
    self.age = age
    self.walkingSpeed = walkingSpeed
    self.runningSpeed = runningSpeed
    self.doesMeow = doesMeow

  def walk(self):
    result = f"This cat is called {self.name} and it's {self.color} {self.type} cat and {self.age} months old and it's walking {self.walkingSpeed} steps in the second"
    if self.doesMeow:
      result += " and it meows."
    else:
      result += " and it doesn't meow."
    print(result)


  def run(self):
    result = f"This cat is called {self.name} and it's {self.color} {self.type} cat and {self.age} months old and it's running {self.runningSpeed} steps in the second"
    if self.doesMeow:
      result += " and it meows."
    else:
      result += " and it doesn't meow."
    print(result)
  
  # def meow(self):
  #   print()