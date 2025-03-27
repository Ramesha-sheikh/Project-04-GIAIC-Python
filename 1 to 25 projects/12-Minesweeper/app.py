import random
import re
import time
from colorama import Fore, Style, init

init(autoreset=True)


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()
        self.flags = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def flag(self, row, col):
        if (row, col) in self.flags:
            self.flags.remove((row, col))
            print(Fore.YELLOW + "Flag removed!")
        else:
            self.flags.add((row, col))
            print(Fore.GREEN + "Flag placed!")

    def __str__(self):
        visible_board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r, c) in self.flags:
                    visible_board[r][c] = Fore.RED + 'F' + Style.RESET_ALL
                elif (r, c) in self.dug:
                    if self.board[r][c] == '*':
                        visible_board[r][c] = Fore.RED + '*' + Style.RESET_ALL
                    else:
                        visible_board[r][c] = str(self.board[r][c])

        string_rep = "   " + " ".join([str(i) for i in range(self.dim_size)]) + "\n"
        for i, row in enumerate(visible_board):
            string_rep += f"{i} |" + " ".join(row) + "\n"
        return string_rep


def play(dim_size=8, num_bombs=10):
    print(Fore.CYAN + "🧨 Welcome to Advanced Minesweeper! 🧨\n")
    print("Choose Difficulty Level:")
    print("1. Easy (8x8, 10 bombs)")
    print("2. Medium (10x10, 20 bombs)")
    print("3. Hard (12x12, 30 bombs)")

    choice = input("Enter 1, 2, or 3: ")
    if choice == '2':
        dim_size, num_bombs = 10, 20
    elif choice == '3':
        dim_size, num_bombs = 12, 30

    board = Board(dim_size, num_bombs)
    safe = True
    start_time = time.time()

    while len(board.dug) < (dim_size ** 2 - num_bombs):
        print(board)
        action = input("Enter action (dig/flag) followed by row,col (e.g., dig 2,3 or flag 1,2): ").strip().lower()

        # 🛡️ Input Validation:
        if len(action.split()) != 2:
            print(Fore.RED + "Invalid input! Use the format: 'dig 2,3' or 'flag 1,2'")
            continue

        try:
            action_type, loc = action.split()[0], action.split()[1]
            row, col = map(int, loc.split(','))

            if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
                print(Fore.RED + "Invalid location. Try again.")
                continue

            if action_type == "dig":
                if (row, col) in board.flags:
                    print(Fore.RED + "Remove the flag first to dig!")
                    continue
                safe = board.dig(row, col)
                if not safe:
                    break
            elif action_type == "flag":
                board.flag(row, col)
            else:
                print(Fore.RED + "Invalid action. Use 'dig' or 'flag'.")
                continue
        except ValueError:
            print(Fore.RED + "Invalid input format! Make sure to enter integers for row and column.")
            continue

    end_time = time.time()
    if safe:
        print(Fore.GREEN + "🎉 Congratulations! You won!")
    else:
        print(Fore.RED + "💥 You hit a bomb! Game Over 💥")
        board.dug = {(r, c) for r in range(dim_size) for c in range(dim_size)}

    print(board)
    print(f"⏱️ Time taken: {round(end_time - start_time, 2)} seconds")

    replay = input("Would you like to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        play()


if __name__ == "__main__":
    play()
