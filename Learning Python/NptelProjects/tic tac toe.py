import math

# Constants representing player symbols
X = 'X'
O = 'O'
EMPTY = ' '

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to generate all possible moves
def generate_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

# Function to evaluate the score of the board
def evaluate(board):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    else:
        return 0

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in generate_moves(board):
            row, col = move
            board[row][col] = X
            eval = minimax(board, depth+1, False)
            board[row][col] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in generate_moves(board):
            row, col = move
            board[row][col] = O
            eval = minimax(board, depth+1, True)
            board[row][col] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

# Function to find the optimal move for the current player
def find_optimal_move(board):
    best_move = None
    best_eval = -math.inf
    for move in generate_moves(board):
        row, col = move
        board[row][col] = X
        eval = minimax(board, 0, False)
        board[row][col] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Main function to run the game
def main():
    board = [[EMPTY]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)

        # Player X's turn
        row, col = find_optimal_move(board)
        board[row][col] = X
        if check_winner(board, X):
            print_board(board)
            print("Player X wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Player O's turn
        print("Player O's turn:")
        while True:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == EMPTY:
                board[row][col] = O
                break
            else:
                print("Invalid move! Try again.")

        if check_winner(board, O):
            print_board(board)
            print("Player O wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
