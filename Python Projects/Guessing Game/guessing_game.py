# The numbers from 1 to 100
# use dict instead of list to make it better

import random

guessingNumber = random.randint(1, 10)
attemptsList = []
attempts = 0

def showScore():
  if not attemptsList:
    print("There isn't a high score currently, start playing!")
  else:
    print(f"The current high score is {min(attemptsList)} attempts")
    print(f"All Scores: {attemptsList}")


print("Hello, player! Welcome to the guessing game!")
playerName = input("what's your name? ")
wannaPlay = input(
  f"Hi, {playerName}, Do you like to play the guessing game?"
  " Enter (Yes/No): "
)

if wannaPlay.lower() == "yes":
  while True:
    try:
      userNumber = int(input("Enter the guessing number [1-10]: "))
      attempts += 1
      if userNumber < 1 or userNumber > 10:
        raise ValueError("Please guess a number within the given range")
      if userNumber == guessingNumber:
        print(f"You won! The guessing number = {guessingNumber}")
        print(f"You took {attempts} attempts to win!🔥")
        attemptsList.append(attempts)
        wannaPlayAgain = input("Would you like to play again? (Yes/No): ")
        if wannaPlayAgain.lower() == "yes":
          attempts = 0
          guessingNumber = random.randint(1, 10)
          showScore()
          continue
        else:
          print("That's cool, have a good day.")
          break
      elif userNumber > guessingNumber:
        print("It's greater than the guessing number!")
      else:
        print("It's smaller than the guessing number!")
    except ValueError as err:
      print(err)
else:
  print(f"That's cool, have a good day ,{playerName}.")
