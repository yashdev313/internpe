import numpy as np

# Creates an empty board
def create_board():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))

# Check for empty places on board
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

# Check if the position is valid
def is_valid_move(board, move):
    if move in possibilities(board):
        return True
    return False

# Place a move on the board
def make_move(board, move, player):
    board[move] = player
    return board

# Checks whether the player has three of their marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
        if win:
            return True
    return False

# Checks whether the player has three of their marks in a vertical row
def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y, x] != player:
                win = False
                break
        if win:
            return True
    return False

# Checks whether the player has three of their marks in a diagonal row
def diag_win(board, player):
    # Check main diagonal
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            break
    if win:
        return True
    
    # Check anti-diagonal
    win = True
    for x in range(len(board)):
        if board[x, len(board) - 1 - x] != player:
            win = False
            break
    return win

# Evaluates whether there is a winner or a tie
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board, player) or
            diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# Function to display the board
def print_board(board):
    print("\n".join(" ".join(str(cell) if cell != 0 else '.' for cell in row) for row in board))
    print()

# Main function to start the game
def play_game():
    board, winner, counter = create_board(), 0, 1
    print_board(board)

    while winner == 0:
        for player in [1, 2]:
            print(f"Player {player}'s turn")
            move = None
            while move is None:
                try:
                    move = tuple(map(int, input(f"Enter your move (row col) for player {player}: ").strip().split()))
                    if len(move) != 2 or not is_valid_move(board, move):
                        print("Invalid move. Please try again.")
                        move = None
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")
            
            board = make_move(board, move, player)
            print(f"Board after move {counter}")
            print_board(board)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner

# Driver Code
winner = play_game()
if winner == -1:
    print("The game is a tie!")
else:
    print(f"Winner is: Player {winner}")
