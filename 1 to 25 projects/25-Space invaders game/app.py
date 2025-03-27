

import pygame
import random
import math

# Pygame initialize karein
pygame.init()

# ----------------------
# Screen Settings
# ----------------------
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Space Shooter")

# ----------------------
# Background Image
# ----------------------
background = pygame.image.load("a.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# ----------------------
# Player Settings
# ----------------------
player_img = pygame.image.load("q.png")
player_img = pygame.transform.scale(player_img, (80, 80))
player_x = screen_width // 2 - 40
player_y = screen_height - 100
player_x_change = 0

def draw_player(x, y):
    screen.blit(player_img, (x, y))

# ----------------------
# Enemy Settings
# ----------------------
num_of_enemies = 5
enemy_imgs = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
for i in range(num_of_enemies):
    enemy_img = pygame.image.load("q.png")
    enemy_img = pygame.transform.scale(enemy_img, (60, 60))
    enemy_imgs.append(enemy_img)
    enemy_x.append(random.randint(0, screen_width - 60))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(3)
    enemy_y_change.append(40)

def draw_enemy(x, y, index):
    screen.blit(enemy_imgs[index], (x, y))

# ----------------------
# Bullet Settings
# ----------------------
bullet_img = pygame.image.load("q.png")
bullet_img = pygame.transform.scale(bullet_img, (20, 20))
bullet_x = 0
bullet_y = player_y
bullet_y_change = 7
bullet_state = "ready"  # "ready" = bullet not visible; "fire" = bullet moving

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # Bullet ko player ke center se fire karein
    screen.blit(bullet_img, (x + 30, y))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance < 27

# ----------------------
# Score Settings
# ----------------------
score = 0
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# ----------------------
# Game Loop
# ----------------------
running = True
while running:
    # Background draw karein
    screen.blit(background, (0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Keyboard control: Left, Right, Space (bullet fire)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x  # Bullet ka x-coordinate player se match hoga
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    
    # Update player position
    player_x += player_x_change
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - 80:
        player_x = screen_width - 80
    draw_player(player_x, player_y)
    
    # Enemy movement aur collision detection
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= screen_width - 60:
            enemy_x_change[i] = -3
            enemy_y[i] += enemy_y_change[i]
        
        # Bullet se collision check karein
        if bullet_state == "fire":
            if is_collision(enemy_x[i], enemy_y[i], bullet_x + 30, bullet_y):
                bullet_y = player_y
                bullet_state = "ready"
                score += 1
                # Enemy ki position reset kar dein
                enemy_x[i] = random.randint(0, screen_width - 60)
                enemy_y[i] = random.randint(50, 150)
        
        draw_enemy(enemy_x[i], enemy_y[i], i)
    
    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y < 0:
        bullet_y = player_y
        bullet_state = "ready"
    
    # Score display
    show_score()
    
    # Screen update karein
    pygame.display.update()

pygame.quit()





# import pygame
# pygame.init()

# # Game window banane ka example
# screen = pygame.display.set_mode((900, 400))
# pygame.display.set_caption("Space Invaders Game")

# # Title and Icon
# pygame.display.set_caption("Space Invaders Game Pygame.....")
# icon = pygame.image.load('q.png')  # Ensure that q.png exists in the project folder
# pygame.display.set_icon(icon)

# # Players
# playersimg = pygame.image.load('q.png')  
# # Resize image; yahaan hum image ko 50x50 pixels ka bana rahe hain
# playersimg = pygame.transform.scale(playersimg, (100, 100))

# playerx = 370
# playery = 30

# def player():
#     screen.blit(playersimg, (playerx, playery))

# running = True
# while running:
#     screen.fill((0, 0, 0))  # Screen ko black color se fill kar rahe hain
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
   
#     player()
#     pygame.display.update()

# pygame.quit()
