import pygame
import random

pygame.init()

# Screen size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_size = 10
snake_speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    # Start position
    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food
    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("Game Over! Press C-Play Again or Q-Quit", red)
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
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        # Boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(white)

        # Draw food
        pygame.draw.rect(
            screen, green, [food_x, food_y, snake_size, snake_size])

        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Collision with itself
        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        for block in snake_List:
            pygame.draw.rect(
                screen, black, [block[0], block[1], snake_size, snake_size])

        pygame.display.update()

        # Eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(
                0, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(
                0, height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
