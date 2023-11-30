import tkinter as tk
import random


def check_winner(board, player):
    # Check for a winning combination in rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    # Check for a tie game
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        return True
    return False


def place_X(row, col):
    # Place X on the board and check for game result
    if board[row][col] == '':
        buttons[row][col].config(
            text='X', state=tk.DISABLED, disabledforeground='black')
        board[row][col] = 'X'
        # handle_game_result()
        place_O()  # Add this line to call place_O() after placing 'X'


def place_O():
    # Place O randomly and check for game result
    available = [(i, j) for i in range(3)
                 for j in range(3) if board[i][j] == '']
    if available:
        row, col = random.choice(available)
        buttons[row][col].config(
            text='O', state=tk.DISABLED, disabledforeground='orange')
        board[row][col] = 'O'
        handle_game_result()


def handle_game_result():
    global user_score, pc_score
    for player in ['X', 'O']:
        if check_winner(board, player):
            result_lbl.config(text="You win!" if player ==
                              'X' else "Computer wins!")
            update_scores(player)
            disable_buttons()
            return
    if check_tie(board):
        result_lbl.config(text="Tie, No winner!")
        disable_buttons()


def disable_buttons():
    # Disable all buttons at the end of the game
    for row in range(3):
        for col in range(3):
            buttons[row][col].configure(state=tk.DISABLED)


def restart_game():
    # Reset the game board and result label
    global board
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL, bg="#eee")
            board[i][j] = ''
    result_lbl.config(text="")


def update_scores(winner):
    # Update scores and display them
    global user_score, pc_score
    if winner == 'X':
        user_score += 1
    else:
        pc_score += 1
    print(f"user_score: {user_score}, pc_score: {pc_score}")  # Add this line for debugging
    score_lbl.config(text=f"You: {user_score}     Computer: {pc_score}")


def reset_scores():
    # Reset scores to zero
    global user_score, pc_score
    user_score = 0
    pc_score = 0
    score_lbl.config(text=f"You: {user_score}     Computer: {pc_score}")


root = tk.Tk()
root.title("Tic-Tac-Toe Game")

board = [['' for _ in range(3)] for _ in range(3)]
buttons = [[tk.Button(root, width=5, height=2, font=("Arial", 30), relief="sunken", bd=1,
            command=lambda row=i, col=j: place_X(row, col)) for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

user_score = 0
pc_score = 0
score_lbl = tk.Label(root, text=f"You: {user_score}     Computer: {
                     pc_score}", font=("Arial", 15))
score_lbl.grid(row=4, column=0, columnspan=3, pady=15)

result_lbl = tk.Label(root, text="", font=("Arial", 12))
result_lbl.grid(row=5, column=0, columnspan=3, pady=15)

restart_btn = tk.Button(root, text="Restart", font=(
    "Arial", 12), command=restart_game)
restart_btn.grid(row=3, column=2, pady=15)

reset_btn = tk.Button(root, text="Reset Scores",
                      font=("Arial", 12), command=reset_scores)
reset_btn.grid(row=3, column=0, pady=15)

root.mainloop()
