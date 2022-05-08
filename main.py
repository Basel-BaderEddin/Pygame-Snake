import pygame
import sys
import random

pygame.init()

w, h = 600, 400

# game variables
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("SnakeGame")

clock = pygame.time.Clock()

cell_size = 10
snake_velocity = 15

msg_font = pygame.font.SysFont('Consolas', 30)
score_font = pygame.font.SysFont('Consolas', 25)


def score(score):
    text = score_font.render("Score:"+str(score), True, (255, 165, 0))
    screen.blit(text, [0, 0])

# snake_p is the snake pixels


def draw_snake(cell_size, snake_p):
    for x in snake_p:
        pygame.draw.rect(screen, (255, 255, 255), [
                         x[0], x[1], cell_size, cell_size])


def main():
    # game variables
    game_over = False
    running = True

    x = w/2
    y = h/2

    delta_x = 0
    delta_y = 0

    snake_p = []
    snake_len = 1

    food_x = round(random.randrange(0, w-cell_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, h-cell_size) / 10.0) * 10.0

    # main loop
    while not game_over:

        while not running:
            screen.fill((50, 50, 50))
            game_over_msg = msg_font.render("Game Over!", True, (255, 0, 0))
            screen.blit(game_over_msg, [w/3, h/3])
            score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        running = True
                        game_over = True
                        sys.exit()
                    if event.key == pygame.K_2:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -cell_size
                if event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = cell_size
                if event.key == pygame.K_LEFT:
                    delta_x = -cell_size
                    delta_y = 0
                if event.key == pygame.K_RIGHT:
                    delta_x = cell_size
                    delta_y = 0
        # game_over if the snake bumps into the walls
        if x >= w or x < 0 or y >= h or y < 0:
            running = False

        x += delta_x
        y += delta_y

        screen.fill((50, 50, 50))
        pygame.draw.rect(screen, (255, 160, 0), [
                         food_x, food_y, cell_size, cell_size])

        # remove last block each movement
        snake_p.append([x, y])
        if len(snake_p) > snake_len:
            del snake_p[0]
        # end game if snake bumps into self
        for pixel in snake_p[:-1]:
            if pixel == [x, y]:
                running = False

        draw_snake(cell_size, snake_p)
        score(snake_len - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, w-cell_size) / 10.0) * 10
            food_y = round(random.randrange(0, h-cell_size) / 10.0) * 10
            snake_len += 1

        clock.tick(snake_velocity)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
