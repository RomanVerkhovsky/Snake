import pygame
import random
import settings


class Snake:
    """class for creation player"""
    def __init__(self):
        self.object = pygame.image.load('images/snake_30_head_right.png')
        self.body_horizont = pygame.image.load('images/snake_30_body_hori.png')
        self.body_vertical = pygame.image.load('images/snake_30_body_vert.png')
        self.body_turn_ur = pygame.image.load('images/snake_30_body_turn_ur.png')
        self.body_turn_ul = pygame.image.load('images/snake_30_body_turn_ul.png')
        self.body_turn_dr = pygame.image.load('images/snake_30_body_turn_dr.png')
        self.body_turn_dl = pygame.image.load('images/snake_30_body_turn_dl.png')
        self.body_tail_right = pygame.image.load('images/snake_30_tail_right.png')
        self.body_tail_left = pygame.image.load('images/snake_30_tail_left.png')
        self.body_tail_up = pygame.image.load('images/snake_30_tail_up.png')
        self.body_tail_down = pygame.image.load('images/snake_30_tail_down.png')

        # current position of snake on map
        self.x = 30
        self.y = 30
        self.body_type = 'h'
        self.arrow_direction = 'right'

        # size of one part of snake:
        self.width = self.object.get_width()
        self.height = self.object.get_height()

        # creation starting body of snake
        self.length = 10    # start size
        self.coordinate_snake = self.create_starting_snake()    # list of parts of snake

    def create_starting_snake(self):
        coordinate_snake = []
        step = 0
        for i in range(self.length):  # creation an initial snake
            coordinate_snake.append([self.x + step, self.y, self.body_type, self.arrow_direction])
            step += self.x
        self.x *= self.length  # change position of head
        coordinate_snake[0][2] = 'tail_r'
        return coordinate_snake

    def update(self, direction: list, step: int, arrow_direction: str):
        """update snake data and moving it"""
        self.arrow_direction = arrow_direction
        if direction == [step, 0]:      # for right direction
            self.object = pygame.image.load("images/snake_30_head_right.png")
            if self.coordinate_snake[-1][3] == 'up':
                self.body_type = 'ul'
            elif self.coordinate_snake[-1][3] == 'down':
                self.body_type = 'dl'
            else:
                self.body_type = 'h'

        elif direction == [-step, 0]:       # for left direction
            self.object = pygame.image.load("images/snake_30_head_left.png")
            if self.coordinate_snake[-1][3] == 'up':
                self.body_type = 'ur'
            elif self.coordinate_snake[-1][3] == 'down':
                self.body_type = 'dr'
            else:
                self.body_type = 'h'

        elif direction == [0, step]:        # for down direction
            self.object = pygame.image.load("images/snake_30_head_down.png")
            if self.coordinate_snake[-1][3] == 'right':
                self.body_type = 'ur'
            elif self.coordinate_snake[-1][3] == 'left':
                self.body_type = 'ul'
            else:
                self.body_type = 'v'

        elif direction == [0, -step]:       # for up direction
            self.object = pygame.image.load("images/snake_30_head_up.png")
            if self.coordinate_snake[-1][3] == 'right':
                self.body_type = 'dr'
            elif self.coordinate_snake[-1][3] == 'left':
                self.body_type = 'dl'
            else:
                self.body_type = 'v'

        if not self.check_game_over(direction):
            self.x += direction[0]
            self.y += direction[1]
            self.coordinate_snake.append([self.x, self.y, 'head', arrow_direction])
            self.coordinate_snake[-2][-2] = self.body_type
            self.coordinate_snake[-2][-1] = self.arrow_direction
            self.coordinate_snake.pop(0)
            if self.coordinate_snake[0][-1] == 'right':
                self.coordinate_snake[0][-2] = 'tail_r'
            elif self.coordinate_snake[0][-1] == 'left':
                self.coordinate_snake[0][-2] = 'tail_l'
            elif self.coordinate_snake[0][-1] == 'down':
                self.coordinate_snake[0][-2] = 'tail_d'
            elif self.coordinate_snake[0][-1] == 'up':
                self.coordinate_snake[0][-2] = 'tail_u'

    def check_game_over(self, direction) -> bool:
        coordinate = []  # list of coordinate for checking collision
        for i in range(len(self.coordinate_snake)):
            coordinate.append([])
            for j in range(len(self.coordinate_snake[i]) - 2):
                coordinate[i].append(self.coordinate_snake[i][j])

        if (settings.resolution[0] - self.width >= self.x + direction[0] >= 0 and
                settings.resolution[1] - self.height >= self.y + direction[1] >= 0 and
                [self.x + direction[0], self.y + direction[1]] not in coordinate):
            return False
        else:
            return True

    def grow(self):
        """grow of snake"""
        new_part = self.coordinate_snake[0]
        self.coordinate_snake.insert(1, new_part)

    def get_place(self):
        """get current position of head"""
        return self.x, self.y


class Meal:
    """ class for creation meal """
    def __init__(self):
        self.object = pygame.image.load('images/meal_30.png')

        # size of meal
        self.width = self.object.get_width()
        self.height = self.object.get_height()

        # current position meal on map
        self.x = random.randrange(0, settings.resolution[0] - self.width, self.width)
        self.y = random.randrange(0, settings.resolution[1] - self.height, self.height)

    def respawn(self, coordinate_snake: list):
        """next position on map"""
        coordinate = []  # list of snake coordinate
        for i in range(len(coordinate_snake)):
            coordinate.append([])
            for j in range(len(coordinate_snake[i]) - 2):
                coordinate[i].append(coordinate_snake[i][j])

        self.x = random.randrange(0, settings.resolution[0] - self.width, self.width)
        self.y = random.randrange(0, settings.resolution[1] - self.height, self.height)
        while [self.x, self.y] in coordinate:
            self.x = random.randrange(0, settings.resolution[0] - self.width, self.width)
            self.y = random.randrange(0, settings.resolution[1] - self.height, self.height)

    def get_place(self):
        """get coordinates of position on map"""
        return self.x, self.y
