def display_board(board):
    """Display the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def has_winner(board, player):
    """Check if the current player has won."""
    # Check horizontal, vertical, and diagonal lines
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def board_full(board):
    """Check if the board is full."""
    return all(cell != ' ' for row in board for cell in row)

def place_move(board, row, col, player):
    """Place a move on the board if the cell is empty."""
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    print("Cell already taken! Please choose another.")
    return False

def play_tic_tac_toe():
    """Main function to play the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    moves = 0

    while True:
        display_board(board)
        print(f"Player {current_player}, it's your turn.")
        
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if 0 <= row < 3 and 0 <= col < 3:
                    if place_move(board, row, col, current_player):
                        break
                print("Invalid input. Please enter a valid row and column.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        moves += 1
        
        if has_winner(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        elif board_full(board):
            display_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
