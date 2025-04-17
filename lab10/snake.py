import pygame
import time
import random
import sys
from pygame.locals import QUIT
from db.dbConnector import DBConnector

pygame.init()

# экран
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with DB")

# цвета
white  = (255, 255, 255)
yellow = (255, 255, 102)
black  = (0,   0,   0)
red    = (213, 50,  80)
green  = (0,   255, 0)
blue   = (50,  153, 213)

# параметры змейки
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

# шрифты
score_style = pygame.font.SysFont('comicsansms', 35)
font_style  = pygame.font.SysFont('arial', 25)
font_input  = pygame.font.SysFont('arial', 30)
title_font  = pygame.font.SysFont('arial', 36)

# направления
direct = 'r'
fix    = direct


def your_score(score):
    txt = score_style.render(f"Your Score: {score}", True, yellow)
    screen.blit(txt, [0, 0])


def your_level(level):
    txt = score_style.render(f"Level: {level}", True, yellow)
    screen.blit(txt, [width - 150, 0])


def our_snake(block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, black, [x, y, block, block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


def get_username():
    input_box = pygame.Rect(100, 250, 200, 50)
    color_inactive = pygame.Color(13, 56, 214)
    color_active   = pygame.Color(25, 168, 212)
    color = color_inactive
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill(white)
        title_surf = title_font.render("ENTER YOUR NAME:", True, black)
        screen.blit(title_surf, (40, 150))

        txt_surface = font_input.render(text, True, black)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
        pygame.draw.rect(screen, color, input_box, 3)

        pygame.display.flip()
        clock.tick(30)


def gameLoop(username, level):
    global snake_speed, direct, fix

    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1

    food_eaten = 0
    foods = [(green, 1), (yellow, 2), (red, 3)]
    foood = random.choice(foods)
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    food_time = pygame.time.get_ticks()

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("You lost! Press C-Play Again or Q-Quit", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        db.saveUser(username, level)
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        return gameLoop(level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fix = 'l'
                elif event.key == pygame.K_RIGHT:
                    fix = 'r'
                elif event.key == pygame.K_UP:
                    fix = 'u'
                elif event.key == pygame.K_DOWN:
                    fix = 'd'

        # обновляем направление
        if direct != 'u' and fix == 'd': direct = 'd'
        if direct != 'd' and fix == 'u': direct = 'u'
        if direct != 'l' and fix == 'r': direct = 'r'
        if direct != 'r' and fix == 'l': direct = 'l'

        if direct == 'l':
            x1_change, y1_change = -snake_block, 0
        elif direct == 'r':
            x1_change, y1_change = snake_block, 0
        elif direct == 'u':
            x1_change, y1_change = 0, -snake_block
        elif direct == 'd':
            x1_change, y1_change = 0, snake_block

        x1 += x1_change
        y1 += y1_change

        # проверка столкновений со стеной
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            db.saveUser(username, level)
            game_close = True

        screen.fill(blue)

        # обновляем еду каждые 5 секунд
        now = pygame.time.get_ticks()
        if now - food_time > 5000:
            foood = random.choice(foods)
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            food_time = now

        pygame.draw.rect(screen, foood[0], [foodx, foody, snake_block, snake_block])

        # тело змейки
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        # самопоедание
        for x, y in snake_List[:-1]:
            if [x1, y1] == [x, y]:
                db.saveUser(username, level)
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(length_of_snake - 1)
        your_level(level)
        pygame.display.update()

        # съели еду?
        if x1 == foodx and y1 == foody:
            length_of_snake += foood[1]
            food_eaten += 1
            if food_eaten % 4 == 0:
                level += 1
                snake_speed += 5
            # генерируем новую
            foood = random.choice(foods)
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # 1) ввод имени
    db = DBConnector()
    username = get_username()
    print("Player:", username)

    # 2) работа с БД
    db.createTableForGameUsers()
    if not db.isUserExist(username):
        db.addNewUser(username)
    user = db.getCurrentUser(username)
    level = user.level
    print(f"{username} -> starting at level {level}")

    # 3) запуск игры
    gameLoop(username, level)