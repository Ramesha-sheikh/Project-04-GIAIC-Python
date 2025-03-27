"""
Tic-Tac-Toe Game
Created by: Rameesha Javed 

Special Features: Friendly messages and personalized design
"""

# --- Required Libraries ---
import tkinter as tk  # Graphical Interface banane ke liye tkinter use ho raha hai
import numpy as np  # Game ka data handle karne ke liye numpy use ho raha hai

# --- Tic Tac Toe Class ---
class TicTacToe:
    def __init__(self):
        # Window create kar rahe hain
        self.window = tk.Tk()
        self.window.title("Create by Ramesha Javed")
        
        # Canvas banaya hai jahan game show hoga
        self.canvas = tk.Canvas(self.window, width=300, height=350, bg='pink')
        self.canvas.pack()

        # 3x3 ka board banaya hai - initially sab 0 hain
        self.board = np.zeros((3, 3))  # 0 ka matlab khali cell
        self.player_turn = 1  # 1 => Player X (First player), -1 => Player O (Second player)

        # Scores ka dictionary - Player X, Player O, aur tie ke liye
        self.scores = {1: 0, -1: 0, 'tie': 0}

        # Board ko initialize kar rahe hain
        self.initialize_board()

        # Mouse click ko handle karne ke liye binding
        self.canvas.bind("<Button-1>", self.click)

        # Game loop start
        self.window.mainloop()

    # --- Board ko initialize karne ka function ---
    def initialize_board(self):
        self.canvas.delete("all")  # Purana board clear kar rahe hain

        # Lines draw kar rahe hain columns aur rows banane ke liye
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, width=3)  # Horizontal lines
            self.canvas.create_line(i * 100, 0, i * 100, 300, width=3)  # Vertical lines

        self.board = np.zeros((3, 3))  # Board reset ho gaya
        self.player_turn = 1  # Pehle player ki turn set ho gayi

        # Score display kar rahe hain
        self.canvas.create_text(150, 325, 
                                text=f"Score - X: {self.scores[1]}  O: {self.scores[-1]}  Tie: {self.scores['tie']}", 
                                font=("Arial", 12))

    # --- X draw karne ka function ---
    def draw_X(self, row, col):
        x1, y1 = col * 100 + 20, row * 100 + 20  # Starting point
        x2, y2 = (col + 1) * 100 - 20, (row + 1) * 100 - 20  # Ending point
        self.canvas.create_line(x1, y1, x2, y2, width=3, fill='darkred')  # Diagonal line 1
        self.canvas.create_line(x1, y2, x2, y1, width=3, fill='darkred')  # Diagonal line 2

    # --- O draw karne ka function ---
    def draw_O(self, row, col):
        x, y = col * 100 + 50, row * 100 + 50  # Center point
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, width=3, outline='darkgreen')  # Circle draw ho gaya

    # --- Jeetne ka check karne ka function ---
    def is_winner(self, player):
        # Horizontal aur vertical check
        for i in range(3):
            if sum(self.board[i, :]) == player * 3 or sum(self.board[:, i]) == player * 3:
                return True

        # Diagonal check
        if sum([self.board[i, i] for i in range(3)]) == player * 3 or \
           sum([self.board[i, 2 - i] for i in range(3)]) == player * 3:
            return True

        return False

    # --- Tie ka check karne ka function ---
    def is_tie(self):
        return not np.any(self.board == 0)  # Agar board mein 0 nahi bacha tou tie

    # --- Game over ka message display karne ka function ---
    def display_gameover(self, result):
        message = ""
        if result == 1:
            message = "Player X (Humaiza ki taraf se Mubarak Ho!) jeet gaya!"  # Player X jeet gaya
        elif result == -1:
            message = "Player O jeet gaya! Next time try karo!"  # Player O jeet gaya
        else:
            message = "Yeh match tie ho gaya! Dono ache khele!"  # Tie ho gaya

        # Score update karna
        self.scores[result if result in [1, -1] else 'tie'] += 1

        # Message display karna
        self.canvas.create_rectangle(20, 120, 280, 180, fill='white', outline='black')  # Message box
        self.canvas.create_text(150, 150, text=message, font=("Arial", 12, "bold"))  # Message text
        self.canvas.create_text(150, 200, text="Phir se khelne ke liye kisi bhi jaga click karein.", font=("Arial", 10))

    # --- Mouse click handle karne ka function ---
    def click(self, event):
        if np.any(self.board == 0):  # Agar board mein khali cell hai tou khelain
            row, col = event.y // 100, event.x // 100  # Click se row aur column calculate karte hain
            if row < 3 and col < 3 and self.board[row, col] == 0:  # Valid click check
                if self.player_turn == 1:
                    self.draw_X(row, col)  # Player X ka turn
                    self.board[row, col] = 1
                else:
                    self.draw_O(row, col)  # Player O ka turn
                    self.board[row, col] = -1

                # Jeet ya tie ka check
                if self.is_winner(self.player_turn):
                    self.display_gameover(self.player_turn)
                elif self.is_tie():
                    self.display_gameover(0)

                # Turn change karna
                self.player_turn *= -1
        else:
            self.initialize_board()  # Game reset kar do

# --- Program start ---
if __name__ == "__main__":
    TicTacToe()  # Game ka object bana kar run kar rahe hain
