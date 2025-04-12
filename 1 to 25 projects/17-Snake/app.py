import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i, j = self.pos
        margin = 2
        pygame.draw.ellipse(surface, self.color, (i * dis + margin, j * dis + margin, dis - 2 * margin, dis - 2 * margin))

        if eyes:
            centre_x = i * dis + dis // 2
            centre_y = j * dis + dis // 2
            radius = 4
            offset_x = 6
            offset_y = 6
            left_eye = (centre_x - offset_x, centre_y - offset_y)
            right_eye = (centre_x + offset_x, centre_y - offset_y)
            pygame.draw.circle(surface, (0, 0, 0), left_eye, radius)
            pygame.draw.circle(surface, (0, 0, 0), right_eye, radius)

class snake(object):
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
        self.game_over = False

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT] and self.dirnx != 1:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_RIGHT] and self.dirnx != -1:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP] and self.dirny != 1:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN] and self.dirny != -1:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.dirnx, c.dirny = turn[0], turn[1]
                c.move(c.dirnx, c.dirny)
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                new_x = c.pos[0] + c.dirnx
                new_y = c.pos[1] + c.dirny

                if new_x < 0 or new_x >= c.rows or new_y < 0 or new_y >= c.rows:
                    self.game_over = True
                    return

                c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
        self.game_over = False

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1]), dx, dy))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1]), dx, dy))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1), dx, dy))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1), dx, dy))

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def draw_grid(w, rows, surface):
    size_btwn = w // rows

    for l in range(rows):
        x = l * size_btwn
        y = l * size_btwn

        pygame.draw.line(surface, (40, 40, 40), (x, 0), (x, w))
        pygame.draw.line(surface, (40, 40, 40), (0, y), (w, y))

def redraw_window(surface):
    global rows, width, s, snack
    surface.fill((30, 30, 30))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()

def random_snack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y

def show_message(subject, content):
    try:
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        root.destroy()
    except tk.TclError:
        print(f"{subject}: {content}")

def draw_game_over(surface, score):
    font = pygame.font.SysFont('Arial', 36)
    text = font.render(f'Game Over! Score: {score}', True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, width // 2))
    surface.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    global width, rows, s, snack
    pygame.init()
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption('Snake Game')
    s = snake((255, 0, 0), (10, 10))
    snack = cube(random_snack(rows, s), color=(0, 255, 0))
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(10)
        s.move()
        if s.game_over:
            draw_game_over(win, len(s.body))
            s.reset((10, 10))
            snack = cube(random_snack(rows, s), color=(0, 255, 0))
            continue

        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = cube(random_snack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                draw_game_over(win, len(s.body))
                s.reset((10, 10))
                snack = cube(random_snack(rows, s), color=(0, 255, 0))
                break

        redraw_window(win)

if __name__ == "__main__":
    main()