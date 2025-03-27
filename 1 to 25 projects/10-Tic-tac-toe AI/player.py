import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            try:
                square = int(input(f"{self.letter}'s turn. Input move (0-8): "))
                if square not in game.available_moves():
                    print("⚠️ Invalid move! Square already taken or out of range. Try again.")
                else:
                    valid_square = True
                    val = square
            except ValueError:
                print("⚠️ Invalid input! Please enter a number between 0 and 8.")
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = random.choice(game.available_moves())
        print(f"🤖 {self.letter} (Random Computer) chose square {move}")
        return move

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
            print(f"🤖 {self.letter} (Smart Computer) starts randomly with square {square}")
        else:
            result = self.minimax(game, self.letter)
            square = result['position']
            print(f"🤖 {self.letter} (Smart Computer) chooses square {square} for the best outcome")
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}

        if not state.empty_squares():
            return {'position': None, 'score': 0}

        # Initializing best scores for max and min players
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # Simulate move
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            # Undo move (backtracking)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # Maximizing or Minimizing the score based on the player
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
