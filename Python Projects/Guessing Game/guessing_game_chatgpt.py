import random

# Initialize an empty dictionary to store high scores (attempts) with player names as keys
attempts_dict = {}


def show_score():
    """Display the current high score."""
    if not attempts_dict:
        print("There isn't a high score currently, start playing!")
    else:
        min_attempts = min(attempts_dict.values())
        print(f"The current high score is {min_attempts} attempts")
        print(f"All Scores: {list(attempts_dict.values())}")


print("Welcome to the Number Guessing Game!")
player_name = input("What's your name? ")

while input(f"Hi, {player_name}, would you like to play the guessing game? Enter (Yes/No): ").lower() == "yes":
    guessing_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            user_number = int(input("Enter the guessing number [1-10]: "))
            attempts += 1

            if user_number < 1 or user_number > 10:
                raise ValueError(
                    "Please guess a number within the given range")

            if user_number == guessing_number:
                print(f"You won! The guessing number was {guessing_number}")
                attempts_dict[player_name] = attempts
                print(f"You took {attempts} attempts to win!🔥")
                show_score()
                break

            print("It's greater than the guessing number!" if user_number >
                  guessing_number else "It's smaller than the guessing number!")

        except ValueError as err:
            print(err)

    if input("Would you like to play again? (Yes/No): ").lower() != "yes":
        print("That's cool, have a good day.")
        break

"""
Changes made:

Consolidated repetitive code blocks.
Combined multiple user input prompts into single lines.
Integrated the high score display within the main game loop.
Simplified variable names without compromising readability.
Added docstrings to describe the purpose of the show_score() function.
Maintained the core functionality while reducing unnecessary lines of code.
"""