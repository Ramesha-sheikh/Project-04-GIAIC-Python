from pprint import pprint  # Yeh module data ko readable format mai print karne ke liye hai
import time  # Time calculate karne ke liye use hota hai

# Empty cell dhoondhne ka function (-1 ki form mai)
def find_next_empty(puzzle):
    """
    Yeh function agla khali (empty) cell dhoondhta hai
    Jo bhi pehla -1 mile ga, uski position (row, col) return karega
    Agar koi empty cell na mile to (None, None) return hoga
    """
    for r in range(9):  # Row check karne ke liye
        for c in range(9):  # Column check karne ke liye
            if puzzle[r][c] == -1:  # Agar cell khali hai to return kardo
                return r, c
    return None, None  # Koi khali cell nahi mila

# Check karna ke guess valid hai ya nahi
def is_valid(puzzle, guess, row, col):
    """
    Yeh function check karta hai ke guess valid hai ya nahi
    Sudoku rules ke mutabiq: row, column, ya 3x3 grid mai repeat nahi hona chahiye
    """

    # Row mai check karna
    if guess in puzzle[row]:  # Agar guess row mai hai to invalid
        return False

    # Column mai check karna
    if guess in [puzzle[i][col] for i in range(9)]:  # Column check
        return False

    # 3x3 grid ka start point nikaalna
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # 3x3 grid mai check karna
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True  # Agar sab check pass ho jaye to valid hai

# Backtracking algorithm se Sudoku solve karna
def solve_sudoku(puzzle):
    """
    Backtracking ka use karke Sudoku ko solve karne wala function
    Agar solve ho jaye to True return karega warna False
    """
    # Pehla empty cell dhoondo
    row, col = find_next_empty(puzzle)

    # Agar koi empty cell nahi mila, matlab puzzle solve ho gaya
    if row is None:
        return True

    # Guess lagana 1 se 9 tak
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):  # Valid guess check karna
            puzzle[row][col] = guess  # Guess ko daal do temporary

            # Recursion se agay solve karne ki koshish karo
            if solve_sudoku(puzzle):
                return True

            # Agar guess galat ho jaye to wapis -1 kar do (backtrack)
            puzzle[row][col] = -1

    return False  # Agar koi guess nahi chala to puzzle unsolvable hai

# Sudoku board ko achay se print karne ka function
def print_board(board):
    """
    Board ko readable format mai print karne ka function
    """
    print("-------------------------")  # Top border
    for i in range(9):
        row_str = "| "  # Row start
        for j in range(9):
            cell = " " if board[i][j] == -1 else board[i][j]  # Empty cells ko space show karna
            row_str += str(cell) + " "  # Cell ko add karna
            if (j + 1) % 3 == 0:  # Har 3rd cell ke baad | dalna
                row_str += "| "
        print(row_str)  # Row print karna
        if (i + 1) % 3 == 0:  # Har 3rd row ke baad bottom border dalna
            print("-------------------------")

# Board ka deep copy banane ka function
def copy_board(board):
    """
    Board ka copy create karna taake original board safe rahe
    """
    return [row[:] for row in board]  # Deep copy of the board

if __name__ == '__main__':
    # Example Sudoku board jisme -1 empty cells hain
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]

    print("Original Sudoku Board:")
    print_board(example_board)

    # Copy banake solve karna
    board_copy = copy_board(example_board)

    print("\nSolving the Sudoku puzzle...\n")
    start_time = time.time()  # Start time
    if solve_sudoku(board_copy):
        print("Sudoku solved successfully!")
        print_board(board_copy)  # Board ko print karna
    else:
        print("Yeh puzzle unsolvable hai.")
    end_time = time.time()  # End time

    print(f"Solved in {(end_time - start_time) * 1000:.2f} ms")  # Time calculation

    # pprint se solution print karna
    print("\nSolution using pprint:")
    pprint(board_copy)
