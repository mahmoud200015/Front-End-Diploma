import tkinter as tk
import random


def check_winner(board, player):
    # Check for a winning combination
    for row in board:
        if all(cell == player for cell in row):
            for c in range(3):
                buttons[board.index(row)][c].configure(bg="#00FFFF")
                # print(buttons[board.index(row)][c])
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            for r in range(3):
                buttons[r][col].configure(bg="#00FFFF")
                # print(buttons[r][col])
            return True

    if all(board[i][i] == player for i in range(3)):
        for i in range(3):
            buttons[i][i].configure(bg="#00FFFF")
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        for i in range(3):
            buttons[i][2-i].configure(bg="#00FFFF")
        return True

    return False


def check_tie(board):
    # Check for a tie
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        for row in range(3):
            for col in range(3):
                buttons[row][col].configure(bg="red")
        return True
    return False


def place_X(row, col):
    global user_score
    global tie_score
    # Check if the cell is empty
    if board[row][col] == '':
        buttons[row][col].config(
            text='X', state=tk.DISABLED, disabledforeground='black')
        board[row][col] = 'X'
        if check_winner(board, 'X'):
            # Update result label
            result_lbl.config(text="You win!")
            # Update label text with the updated scores
            user_score += 1
            score_lbl.config(
                text=f"You: {user_score}     Tie: {tie_score}     Computer: {pc_score}")
            disable_buttons()
        elif check_tie(board):
            # Update result label
            tie_score += 1
            score_lbl.config(
                text=f"You: {user_score}     Tie: {tie_score}     Computer: {pc_score}")
            result_lbl.config(text="Tie, No winner!")
            disable_buttons()

        else:
            place_O()


def place_O():
    global pc_score
    global tie_score
    available = [(i, j) for i in range(3)
                 for j in range(3) if board[i][j] == '']
    # print(available)
    if available:
        row, col = random.choice(available)
        buttons[row][col].config(
            text='O', state=tk.DISABLED, disabledforeground='orange')
        board[row][col] = 'O'
        if check_winner(board, 'O'):
            # Update result label
            result_lbl.config(text="Computer wins!")
            # Update label text with the updated scores
            pc_score += 1
            score_lbl.config(
                text=f"You: {user_score}     Tie: {tie_score}     Computer: {pc_score}")
            disable_buttons()
        elif check_tie(board):
            # Update result label
            tie_score += 1
            score_lbl.config(
                text=f"You: {user_score}     Tie: {tie_score}     Computer: {pc_score}")
            result_lbl.config(text="Tie, No winner!")
            disable_buttons()


def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].configure(state=tk.DISABLED)


def restart_game():
    global board
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL, background="#eee")
            board[i][j] = ''
    # reset result label to default value
    result_lbl.config(text="")
    # reset_scores()


def reset_scores():
    global user_score
    global pc_score
    global tie_score
    user_score = 0
    pc_score = 0
    tie_score = 0
    score_lbl.config(text=f"You: {user_score}     Tie: {tie_score}     Computer: {pc_score}")


root = tk.Tk()
root.title("Tic-Tac-Toe Game")

# Empty board (3x3) stores all (x-o)s in game to hold them easily
board = [['' for _ in range(3)] for _ in range(3)]

buttons = [[tk.Button(root, width=5, height=2, font=(
    "Arial", 30), relief="sunken", bd=1, command=lambda row=i, col=j:
    place_X(row, col)) for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

# Score Label
user_score = 0
pc_score = 0
tie_score = 0
score_lbl = tk.Label(root, text=f"You: {user_score}     Tie: {tie_score}     Computer: {
                     pc_score}", font=("Arial", 15))
score_lbl.grid(row=4, column=0, columnspan=3, pady=15)

# Result Label
result_lbl = tk.Label(root, text="", font=("Arial", 16))
result_lbl.grid(row=5, column=0, columnspan=3, pady=15)


# Restart Button (for game)
restart_btn = tk.Button(root, text="restart", font=(
    "Arial", 12), command=restart_game)
restart_btn.grid(row=3, column=2, pady=15)

# Reset Button (for scores)
reset_btn = tk.Button(root, text="reset scores",
                      font=("Arial", 12), command=reset_scores)
reset_btn.grid(row=3, column=0, pady=15)

root.mainloop()
