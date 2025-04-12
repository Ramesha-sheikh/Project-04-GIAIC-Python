import turtle
import pygame
import time
from dataclasses import dataclass

# Initialize Pygame mixer for sound effects
pygame.mixer.init()
try:
    ball_sound = pygame.mixer.Sound("bounce.wav")
except:
    # Fallback if sound file is missing
    ball_sound = None

game_duration = 30  # Game lasts 30 seconds
start_time = time.time()

def remaining_time():
    return max(0, int(game_duration - (time.time() - start_time)))

@dataclass
class Paddle:
    turtle_obj: turtle.Turtle
    x: int
    y: int

    def __post_init__(self):
        self.turtle_obj.speed(0)
        self.turtle_obj.shape("square")
        self.turtle_obj.color("white")
        self.turtle_obj.shapesize(stretch_wid=5, stretch_len=1)
        self.turtle_obj.penup()
        self.turtle_obj.goto(self.x, self.y)

    def move_up(self):
        if self.turtle_obj.ycor() < 250:
            self.turtle_obj.sety(self.turtle_obj.ycor() + 20)

    def move_down(self):
        if self.turtle_obj.ycor() > -240:
            self.turtle_obj.sety(self.turtle_obj.ycor() - 20)

class Ball:
    def __init__(self):
        self.turtle_obj = turtle.Turtle()
        self.turtle_obj.speed(0)
        self.turtle_obj.shape("circle")
        self.turtle_obj.color("yellow")
        self.turtle_obj.penup()
        self.turtle_obj.goto(0, 0)
        self.dx = 2
        self.dy = 2

    def move(self):
        try:
            # Check if window still exists
            if not wn._root or not wn._root.winfo_exists():
                return
                
            self.turtle_obj.setx(self.turtle_obj.xcor() + self.dx)
            self.turtle_obj.sety(self.turtle_obj.ycor() + self.dy)
            
            if self.turtle_obj.ycor() > 290 or self.turtle_obj.ycor() < -290:
                self.dy *= -1
                if ball_sound:
                    pygame.mixer.Sound.play(ball_sound)
        except (turtle.Terminator, tkinter.TclError):
            # Handle the case where turtle window is closed
            return False
        return True

    def reset_position(self):
        try:
            self.turtle_obj.goto(0, 0)
            self.dx *= -1
        except (turtle.Terminator, tkinter.TclError):
            return False
        return True

# Import tkinter for better error handling
import tkinter

# Create the screen and set it up
wn = turtle.Screen()
wn.title("Advanced Pong")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer(0)

# Create a function to check if window is still valid
def is_window_valid():
    try:
        return wn._root and wn._root.winfo_exists()
    except:
        return False

time.sleep(1)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)

for i in range(3, 0, -1):
    if not is_window_valid():
        break
    pen.clear()
    pen.write(f"Game starts in {i}", align="center", font=("Courier", 24, "normal"))
    wn.update()
    time.sleep(1)

if is_window_valid():
    pen.clear()
    pen.write("Game Start!", align="center", font=("Courier", 24, "normal"))
    wn.update()
    time.sleep(1)
    pen.clear()

score_a, score_b = 0, 0
paddle_a = Paddle(turtle.Turtle(), -350, 0)
paddle_b = Paddle(turtle.Turtle(), 350, 0)
ball = Ball()

pen.goto(0, 260)

def update_score():
    try:
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}  Time: {remaining_time()}s", 
                 align="center", font=("Courier", 24, "normal"))
    except (turtle.Terminator, tkinter.TclError):
        return False
    return True

update_score()

wn.listen()
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")

# Main game loop with improved error handling
game_running = True
try:
    while game_running and remaining_time() > 0:
        # Check if window is still valid
        if not is_window_valid():
            break
            
        try:
            wn.update()
        except (turtle.Terminator, tkinter.TclError):
            game_running = False
            break
            
        # Move the ball and check if it was successful
        if not ball.move():
            game_running = False
            break
        
        # Paddle collision detection
        if (-340 < ball.turtle_obj.xcor() < -330 and 
            paddle_a.turtle_obj.ycor() - 50 < ball.turtle_obj.ycor() < paddle_a.turtle_obj.ycor() + 50) or \
           (330 < ball.turtle_obj.xcor() < 340 and 
            paddle_b.turtle_obj.ycor() - 50 < ball.turtle_obj.ycor() < paddle_b.turtle_obj.ycor() + 50):
            ball.dx *= -1
            if ball_sound:
                pygame.mixer.Sound.play(ball_sound)

        # Score handling
        if ball.turtle_obj.xcor() > 390:
            score_a += 1
            if not ball.reset_position() or not update_score():
                game_running = False
                break
        elif ball.turtle_obj.xcor() < -390:
            score_b += 1
            if not ball.reset_position() or not update_score():
                game_running = False
                break
        
        time.sleep(0.01)
except (turtle.Terminator, tkinter.TclError, KeyboardInterrupt):
    game_running = False

# Game over message
if is_window_valid():
    try:
        pen.goto(0, 0)
        pen.clear()
        pen.write("Game Over!", align="center", font=("Courier", 30, "bold"))
        wn.update()
        time.sleep(3)
        wn.bye()
    except:
        # If there's any error during cleanup, just pass
        pass
