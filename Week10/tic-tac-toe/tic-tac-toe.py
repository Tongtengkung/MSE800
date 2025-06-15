import random

def new_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def get_O_or_X():                                                                   # Function to get the player's choice of symbol
    while True:
        choice = input("Choose your symbol, X always start first ('O' or 'X'): ").upper()
        if choice in ['O', 'X']:
            return choice
        else:
            print("Invalid choice. Please enter 'O' or 'X'.")

def display(board):
    print("   0   1   2 (Column)")                                                          # Print column headers
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))                                           # Print row number followed by row contents
        if i < 2:
            print("  " + "-" * 11)
    print("(Row)")

def game_over(board):
    return check_winner(board, 'X') or check_winner(board, 'O') or not empty_squares(board)

def check_winner(board, player):                                                    # Rows and columns
    lines = []
    for i in range(3):
        lines.append(board[i])                                                      # rows
        lines.append([board[0][i], board[1][i], board[2][i]])                       # columns

                                                                                    # Diagonals                                     
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    return any(all(cell == player for cell in line) for line in lines)

def empty_squares(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def other_player(player):
    return 'O' if player == 'X' else 'X'

def play_game(board, human_player):
    current_player = 'X'                                                            # X always starts
    while not game_over(board):
        display(board)

        if current_player == human_player:
            make_human_move(board, current_player)
        else:
            make_computer_move(board, current_player)

        if check_winner(board, current_player):
            display(board)
            print(f"Player {current_player} wins!")
            return current_player
        current_player = other_player(current_player)
    display(board)
    print("It's a draw!")
    return "Draw"

def make_human_move(board, current_player):
    while True:
        try:
            move = input("Enter your move as 'row column' (0-2): ")
            row_str, col_str = move.strip().split()
            row, col = int(row_str), int(col_str)
            if (row, col) in empty_squares(board):
                board[row][col] = current_player
                return
            else:
                print("That square is not empty or invalid. Try again.")
        except (ValueError, IndexError):
            print("Invalid input format. Please enter two numbers separated by a space.")

def make_computer_move(board, current_player):
    candidates = empty_squares(board)
    choice = random.randint(0, len(candidates) - 1)
    row, col = candidates[choice]
    print(f"Computer chooses ({row}, {col})")
    board[row][col] = current_player

def print_result(outcome):
    if outcome == "Draw":
        print("The game ended in a draw.")
    else:
        print(f"Congratulations! {outcome} wins!")

def main():
    board = new_board()
    human_player = get_O_or_X()
    outcome = play_game(board, human_player)
    print_result(outcome)

if __name__ == "__main__":
    main()
