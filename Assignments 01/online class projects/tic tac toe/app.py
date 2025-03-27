# Simple Tic-Tac-Toe Game in Python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Horizontal, Vertical, and Diagonal checks
    return (
        any(all(cell == player for cell in row) for row in board) or
        any(all(row[i] == player for row in board) for i in range(3)) or
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2 - i] == player for i in range(3))
    )


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Simple Tic-Tac-Toe!\n")
    print_board(board)

    for _ in range(9):  # Maximum 9 moves possible
        try:
            print(f"Player {current_player}'s turn:")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if board[row][col] == " ":
                board[row][col] = current_player
                print_board(board)

                if check_winner(board, current_player):
                    print(f"🎉 Player {current_player} wins! 🎉")
                    break

                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("⚠️ Cell already taken! Try again.")
        except (ValueError, IndexError):
            print("⚠️ Invalid input! Enter numbers between 0 and 2.")

    else:
        print("It's a draw! 🤝")


if __name__ == "__main__":
    tic_tac_toe()
