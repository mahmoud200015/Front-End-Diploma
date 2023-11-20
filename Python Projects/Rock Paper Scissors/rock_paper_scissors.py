"""
- Start the game
- Ask the player to make a move (r, p, s)
- PC would select a move randomly

- PC == Player -> Tie
- (Player == P and PC == Rock) or
  (Player == R and PC == Scissors) or 
  (Player == Scissors and PC == Paper) -> User won / You won
- Any other case -> PC won / You lose 
"""

import random

moves = ["r", "p", "s"]
playerMove = input("Enter your move ('r' for Rock, 'p' for Paper, 's' for Scissors): ")
pcMove = moves[random.randint(0, 2)]
# pcMove = random.choice(moves)

print(f"You played: {playerMove}")
print(f"Pc played: {pcMove}")

if playerMove == pcMove:
  print("It's tie!")
elif (playerMove == 'p' and pcMove == 'r') or (playerMove == 'r' and pcMove == 's') or (playerMove == 's' and pcMove == 'p'):
  print("You Won, Congratulations!")
else:
  print("You Lose, Try Again!")

