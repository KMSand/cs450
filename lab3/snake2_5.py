import pygame
import time
import random

# Initialize the game
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
dis_width = 600
dis_height = 400

# Create the display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Qwen')

# Define the clock
clock = pygame.time.Clock()

# Define snake block size and initial speed
snake_block = 10
initial_snake_speed = 15

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    powerup_x = random.randrange(0, dis_width - snake_block, snake_block)
    powerup_y = random.randrange(0, dis_height - snake_block, snake_block)
    powerup_type = random.choice(['speed', 'invincibility'])

    obstacle_x = random.randrange(0, dis_width - snake_block, snake_block)
    obstacle_y = random.randrange(0, dis_height - snake_block, snake_block)

    # Initialize snake speed
    snake_speed = initial_snake_speed

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, yellow, [powerup_x, powerup_y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [obstacle_x, obstacle_y, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        # Check for collisions with food
        if abs(x1 - foodx) < snake_block and abs(y1 - foody) < snake_block:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Check for collisions with power-ups
        if abs(x1 - powerup_x) < snake_block and abs(y1 - powerup_y) < snake_block:
            if powerup_type == 'speed':
                snake_speed += 5
            elif powerup_type == 'invincibility':
                pygame.time.set_timer(pygame.USEREVENT, 2000)
                pygame.event.clear(pygame.USEREVENT)
            powerup_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            powerup_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        # Check for collisions with obstacles
        if (abs(x1 - obstacle_x) < snake_block or abs(x1 + snake_block - obstacle_x) < snake_block) and \
           (abs(y1 - obstacle_y) < snake_block or abs(y1 + snake_block - obstacle_y) < snake_block):
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()