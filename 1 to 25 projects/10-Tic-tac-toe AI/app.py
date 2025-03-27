import time
from player import HumanPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Board ka initial state
        self.current_winner = None  # Winner ka tracker
        self.scores = {'X': 0, 'O': 0, 'Tie': 0}  # Score track karne ke liye

    def print_board(self):
        # Dynamic board display for better visibility
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Numbered board for guidance
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print("Choose a number (0-8) to place your move:")
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':  # Agar cell khaali hai
            self.board[square] = letter
            if self.winner(square, letter):  # Agar winner hai toh update kar do
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row-wise
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        # Check column-wise
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal1]) or all([s == letter for s in diagonal2]):
                return True

        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

def play(game, x_player, o_player, print_game=True):
    if print_game:
        print("Welcome to the Enhanced Tic Tac Toe!")
        game.print_board_nums()

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} ne move kiya square {square} pe:")
                game.print_board()
                print('')

            if game.current_winner:
                print(f"🎉 {letter} jeet gaya! Mubarak ho!")
                game.scores[letter] += 1
                break

            letter = 'O' if letter == 'X' else 'X'  # Turn switch
            time.sleep(0.5)
        else:
            print("Invalid move! Try again.")

    if game.current_winner is None:
        print("Match tie hogaya! Dono ne acha khela!")
        game.scores['Tie'] += 1

    # Score Display
    print("\n📊 Current Scores:")
    print(f"X: {game.scores['X']} | O: {game.scores['O']} | Tie: {game.scores['Tie']}")

    # Replay Option
    replay = input("Kya aap dobara khelna chahte hain? (y/n): ").lower()
    if replay == 'y':
        game.board = [' ' for _ in range(9)]
        game.current_winner = None
        play(game, x_player, o_player, print_game)

if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
