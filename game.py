import pygame
import game_objects
import settings


class Game:
    """class for creation game session"""
    def __init__(self, window) -> None:

        # window setup
        self.window = window    # window for rendering

        # game status
        self.check_notQUIT = True
        self.status = 'play'
        self.scores = 0

        # control settings
        self.input_device = settings.control

        # direct moving
        self.first_start = True
        self.direction = [0, 0]
        self.step = 30
        self.arrow_direction = 'right'

        # creating entities in the game
        self.player = game_objects.Snake()
        self.meal = game_objects.Meal()

    def event(self):
        """event handling"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.check_notQUIT = False
            # change direction moving
            elif event.type == pygame.KEYDOWN and self.status == 'play':
                # direction right
                if event.key == self.input_device.right and self.arrow_direction != 'left':
                    self.direction = [self.step, 0]
                    self.arrow_direction = 'right'
                    self.first_start = False
                # direction left
                elif event.key == self.input_device.left and self.arrow_direction != 'right':
                    self.direction = [-self.step, 0]
                    self.arrow_direction = 'left'
                    self.first_start = False
                # direction down
                elif event.key == self.input_device.down and self.arrow_direction != 'up':
                    self.direction = [0, self.step]
                    self.arrow_direction = 'down'
                    self.first_start = False
                # direction up
                elif event.key == self.input_device.up and self.arrow_direction != 'down':
                    self.direction = [0, -self.step]
                    self.arrow_direction = 'up'
                    self.first_start = False
                break

    def update(self):
        """update state game"""
        if self.status == 'play':
            if self.player.get_place() == self.meal.get_place():    # check eating and next actions
                self.meal.respawn(self.player.coordinate_snake)
                self.player.grow()
            if not self.first_start:
                if not self.player.check_game_over(self.direction):
                    self.player.update(self.direction, self.step, self.arrow_direction)
                else:
                    self.status = 'game over'

    def render(self):
        """display state game"""
        # display background
        self.window.blit(pygame.image.load('images/grass.jpg'), (0, 0))

        # display game objects
        self.window.blit(self.meal.object, (self.meal.x, self.meal.y))  # display meal

        for i in range(len(self.player.coordinate_snake)):    # display snake
            if 0 < i < len(self.player.coordinate_snake) - 1:
                if self.player.coordinate_snake[i][2] == 'h':
                    self.window.blit(self.player.body_horizont, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'v':
                    self.window.blit(self.player.body_vertical, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'ur':
                    self.window.blit(self.player.body_turn_ur, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'ul':
                    self.window.blit(self.player.body_turn_ul, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'dr':
                    self.window.blit(self.player.body_turn_dr, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'dl':
                    self.window.blit(self.player.body_turn_dl, self.player.coordinate_snake[i][:2])
            elif i == len(self.player.coordinate_snake) - 1:
                self.window.blit(self.player.object, self.player.coordinate_snake[i][:2])
            else:
                if self.player.coordinate_snake[i][2] == 'tail_r':
                    self.window.blit(self.player.body_tail_right, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'tail_l':
                    self.window.blit(self.player.body_tail_left, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'tail_d':
                    self.window.blit(self.player.body_tail_down, self.player.coordinate_snake[i][:2])
                elif self.player.coordinate_snake[i][2] == 'tail_u':
                    self.window.blit(self.player.body_tail_up, self.player.coordinate_snake[i][:2])

        pygame.display.update()
