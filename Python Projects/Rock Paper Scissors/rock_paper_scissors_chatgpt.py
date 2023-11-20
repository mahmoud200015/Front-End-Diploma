import random

# list of play options
options = ["rock", "paper", "scissors"]

# winning rules
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    # get player choice
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # check if player choice is valid
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # get computer choice
    computer_choice = random.choice(options)

    # print player choice and computer choice
    print(f"Player's choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    # check the result
    if player_choice == computer_choice:
        print("It's a tie!")
    elif rules.get(player_choice) == computer_choice:
        print("You win!, Congratulations!")
    else:
        print("You lose!, Try Again!")
