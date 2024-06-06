import pygame
import random
import os
import time
import sys

pygame.mixer.init()
pygame.init()

# Colors
BLUE = (0, 0, 255)
color = (120, 9, 38)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
frame_count = 0
frame_rate = 60
start_time = 90
done = False
SNAKE_WIDTH = 15

# Creating window
screen_width = 1080 / 1.2
screen_height = 990 / 1.2
medium_font = pygame.font.SysFont('showcard gothic', 30, True)
gameWindow = pygame.display.set_mode((int(screen_width), int(screen_height)))
snake_img = pygame.image.load('snake2.png')
tail_img = pygame.image.load('tail1.png')

# Background Image
background_images = ["Background4.jpg", "Background11.jpg", "Background3.jpg"]  # Lisa siia kõik taustapildid
start_time = pygame.time.get_ticks()
# Valime juhusliku taustapildi
background_image_path = random.choice(background_images)


# Game over Image
over_image = pygame.image.load("Gameover2.jpg")
over_image = pygame.transform.scale(over_image, (int(screen_width), int(screen_height)))

# Front Image
menu_image = pygame.image.load("Menu3.jpg")
menu_image = pygame.transform.scale(menu_image, (int(screen_width), int(screen_height)))

# Food Image
food_image = pygame.image.load('Food2.png')
food_image = pygame.transform.scale(food_image, (45, 50))

# Cookie Image
cookie_image = pygame.image.load('cookie.png')
cookie_image = pygame.transform.scale(cookie_image, (45, 50))

# Icon
icon_image = pygame.image.load('Icon.png')

# Game Title
pygame.display.set_caption("Snike")
pygame.display.set_icon(icon_image)
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)
large_font = pygame.font.SysFont('chiller', 60, True, True)

# Function to display the food
def display_food(food_x, food_y, is_cookie):
    if is_cookie:
        gameWindow.blit(cookie_image, (food_x, food_y))
    else:
        gameWindow.blit(food_image, (food_x, food_y))

# Function to display the text on the screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Function to plot the snake
def plot_snake(gameWindow, snake_list, direction):
    head = pygame.transform.rotate(snake_img, {'right': 270, 'left': 90, 'up': 0, 'down': 180}[direction])
    tail = pygame.transform.rotate(tail_img, {'right': 270, 'left': 90, 'up': 0, 'down': 180}[direction])
    gameWindow.blit(head, snake_list[-1])
    gameWindow.blit(tail, snake_list[0])

    for XnY in snake_list[1:-1]:
        pygame.draw.rect(gameWindow, BLUE, (XnY[0], XnY[1], SNAKE_WIDTH, SNAKE_WIDTH))

# Function to play the music
def music():
    pygame.mixer.music.load('back.mp3')
    pygame.mixer.music.play()

# Function to play the sound when the snake crashes
def crashed():
    pygame.mixer.music.load('over.mp3')
    pygame.mixer.music.play()

# Function to quit the game
def quit_game():
    pygame.quit()
    sys.exit()

# Function to create a button
def button(x, y, w, h, action, action2):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] and y + h > mouse[1] and click[0] == 1:
        action2()
        action()

# Function to display the game intro
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    music()
                    gameloop()

        gameWindow.fill(0)
        gameWindow.blit(menu_image, (0, 0))
        button(20, int(screen_height - 70), 497 / 2, 135 / 2, gameloop, music)  # Start button on the left side
        button(int(screen_width - 155), int(screen_height - 70), 497 / 2, 135 / 2, quit_game, music)  # Exit button on the right side
        pygame.display.update()
        clock.tick(10)

# Function to display the game paused message
# Funktsioon mängu pausile panemiseks
def game_paused():
    paused_font1 = font.render("Game Paused", True, RED)
    paused_font_rect1 = paused_font1.get_rect()
    paused_font_rect1.center = (screen_width / 2, screen_height / 2)
    gameWindow.blit(paused_font1, paused_font_rect1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    return
        pygame.display.update()


# Function to handle the game loop
def gameloop():
    exit_game = False
    game_over = False
    start_time = pygame.time.get_ticks()  # Get the start time
    snake_x = 55
    snake_y = 55
    snake_list = []
    snake_length = 1
    snake_size = 40
    direction = 'right'
    pause_font = medium_font.render('II', True, RED)
    score = 0
    food_count = 0
    velocity_x = 0
    velocity_y = 0
    init_velocity = 2
    fps = 60
    food_x = random.randint(20, int(screen_width / 2))
    food_y = random.randint(20, int(screen_height / 2))
    is_cookie = False

    if not os.path.exists("high_score.txt"):
        with open("high_score.txt", "w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        high_score = f.read()

    while not exit_game:
    # Värskendage start_time'i iga tsükli iteratsiooni alguses
        
        current_time = pygame.time.get_ticks()  # Get the current time
        elapsed_time = (current_time - start_time) / 1000  # Calculate the elapsed time in seconds
        remaining_time = 80 - elapsed_time  # Calculate the remaining time

        if remaining_time <= 0:  # Check if the time is up
            game_over = True

    # Ülejäänud mänguloogika jääb samaks

    # Lõpuks värskendage algusaega, et hoida ajatähiste värskendamist
    
        gameWindow.blit(pygame.image.load(background_image_path), (0, 0))



        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            crashed()
            game_time = (pygame.time.get_ticks() - start_time) // 1000  # Teisenda millisekundid sekunditeks
    # Kuva gameoveri tekst koos mänguajaga
            gameWindow.fill(0)
            gameWindow.blit(over_image, (0, 0))
            text_screen("Selle " + str(game_time) + " sekundi jooksul on sinu punktide summa " + str(score) , BLACK, 180, screen_height - 140)
            pygame.display.update()
            time.sleep(5)
            game_intro()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if direction != 'left':
                            direction = 'right'
                            velocity_x = init_velocity
                            velocity_y = 0
                    if event.key == pygame.K_p:
                        game_paused()

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if direction != 'right':
                            direction = 'left'
                            velocity_x = -init_velocity
                            velocity_y = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if direction != 'down':
                            direction = 'up'
                            velocity_y = -init_velocity
                            velocity_x = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if direction != 'up':
                            direction = 'down'
                            velocity_y = init_velocity
                            velocity_x = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pause_xy = event.pos
                        if pause_xy[0] > (screen_width - 50) and pause_xy[0] < screen_width:
                            if pause_xy[1] > 0 and pause_xy[1] < 50:
                                game_paused()
                    if event.key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        food_x = random.randrange(5, int(screen_width - seconds0))
                        food_y = random.randrange(5, int(screen_height - 100))
                    if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        init_velocity += 1
                    if event.key == pygame.K_UNDERSCORE or event.key == pygame.K_MINUS and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        if init_velocity > 1:
                            init_velocity -= 1
                    if event.key == pygame.K_p:
                        game_paused()
            
        # Move the snake
        snake_x += velocity_x
        snake_y += velocity_y

        # Check for collision with the food
        if abs(snake_x - food_x) < 35 and abs(snake_y - food_y) < 35:
            food_count += 1
            if food_count % 7 == 0:
                score += 20  # Cookie gives more points
                is_cookie = True
            else:
                score += 10  # Regular food
                is_cookie = False
                
            if food_count % 6 == 0:
                is_cookie = True
            else:
                is_cookie = False

            food_x = random.randint(20, int(screen_width / 2))
            food_y = random.randint(20, int(screen_height / 2))
            snake_length += 10
            init_velocity += 0.3
            if score > int(high_score):
                high_score = score

        # Add the snake's head to the list
        head = [snake_x, snake_y]
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        if head in snake_list[:-1]:
            game_over = True

        if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
            game_over = True

        gameWindow.fill(0)
        gameWindow.blit(pause_font, (screen_width - 45, 10))
        gameWindow.blit(pygame.image.load(background_image_path), (0, 0))
        
        text_screen("Top Score: " + str(high_score) + "         Score: " + str(score), color, screen_width / 2 - 155, 63)
        display_food(food_x, food_y, is_cookie)  # Display cookie if it's the 7th food
        plot_snake(gameWindow, snake_list, direction)
        remaining_seconds = int(remaining_time)
        remaining_text = "Remaining Time: " + str(remaining_seconds) + "s"  # Tekst järelejäänud aja kuvamiseks
        text_screen(remaining_text, color, 10, 10)  # Kuvame järelejäänud aja ekraanil

        pygame.display.update()
        
        clock.tick(fps)

# Kutsuge mänguintro funktsioon käima peale mänguloop funktsiooni defineerimist
game_intro()

pygame.quit()
quit()
