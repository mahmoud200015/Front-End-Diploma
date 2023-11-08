class Screwdriver:
  def __init__(self, color, len, type, doesRotate, doesTest):
    self.color = color
    self.len = len
    self.type = type
    self.doesRotate = doesRotate
    self.doesTest = doesTest

  def rotates(self):
    result = f"I'm a {self.len} cm {self.color} {self.type} screwdriver"
    if self.doesRotate:
      result += " and I rotate."
    else:
      result += " and I don't rotate."
    print(result)

  def testsElectricity(self):
    result = f"I'm a {self.len} cm {self.color} {self.type} screwdriver"
    if self.doesTest:
      result += " and I test electricity."
    else:
      result += " and I don't test electricity."
    print(result)
