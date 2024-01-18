import pygame
import objects
import settings


class Menu:
    """class for creation and display menu"""
    def __init__(self, window):
        self.window = window    # window for rendering

        # menu status
        self.check_notQUIT = True
        self.status = 'menu'

        # static inscription
        self.font_name = pygame.font.SysFont('Comic Sans MS', 164, bold=True, italic=True)
        self.font_other = pygame.font.SysFont('Comic Sans MS', 40, bold=True, italic=True)

        self.title = self.font_name.render('SNAKE', True, pygame.Color(252, 200, 12))
        self.info = self.font_other.render('>> enter for start <<', True, pygame.Color(252, 200, 12))
        self.settings = self.font_other.render('settings in develop...', True, pygame.Color('orange'))

        # interactive inscriptions
        self.inscriptions_positions = {
            1: (settings.resolution[0] / 2 - 150, settings.resolution[1] / 2),
            2: (settings.resolution[0] / 2 - 150, settings.resolution[1] / 2 + 50),
            3: (settings.resolution[0] / 2 - 150, settings.resolution[1] / 2 + 50)
        }

        self.inscriptions = {
            'start game': objects.Inscription('START GAME', 'orange'),
            'settings': objects.Inscription('  SETTINGS', 'orange'),
            'controls': objects.Inscription('  CONTROLS', 'orange'),
            'speed': objects.Inscription('   SPEED', 'orange'),
            'info': objects.Inscription('   INFO', 'orange')
        }

        # level menu - settings
        self.inscriptions['settings'].add_link(self.inscriptions['controls'])
        self.inscriptions['settings'].add_link(self.inscriptions['speed'])
        self.inscriptions['settings'].add_link(self.inscriptions['info'])

        # level menu - controls

        # level menu - speed

        # level menu - info

        self.current_level = [
            self.inscriptions['start game']
        ]

        container_inscriptions = objects.ContainerInscription()
        self.current_menu = objects.LevelMenu()

        # cursor
        self.cursor_position = 1
        self.dict_position = {1: (settings.resolution[0] / 2 - 200, settings.resolution[1] / 2 + 15),
                              2: (settings.resolution[0] / 2 - 200, settings.resolution[1] / 2 + 65)}

    def event(self):
        """event handling"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.check_notQUIT = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.status = 'game'

                if event.key == pygame.K_DOWN:
                    if self.cursor_position == len(self.current_level):
                        self.cursor_position = 1
                    else:
                        self.cursor_position += 1

                if event.key == pygame.K_UP:
                    if self.cursor_position == 1:
                        self.cursor_position = len(self.current_level)
                    else:
                        self.cursor_position -= 1

    def update(self):
        """update state menu"""
        self.current_menu.choice_menu(self.cursor_position)

    def render(self):
        """display state menu"""
        # display background
        self.window.blit(pygame.image.load('images/grass.jpg'), (0, 0))
        self.window.blit(pygame.image.load('images/snake_menu.png'), (settings.resolution[0] / 2 - 300, 30))
        self.window.blit(pygame.image.load('images/meal_30.png'), self.dict_position[self.cursor_position])

        # display inscriptions
        self.window.blit(self.title, (settings.resolution[0] / 2 - 300, 30))    # title
        self.window.blit(self.settings, (settings.resolution[0] / 2 - 180, 520))
        self.window.blit(self.info, (settings.resolution[0] / 2 - 210, 700))

        for i in range(len(self.current_level)):                   # interactive inscription
            self.window.blit(self.current_level[i].inscription,
                             self.inscriptions_positions[i + 1])

        pygame.display.update()

    def run(self):
        self.event()
        self.update()
        self.render()


class Game:
    """class for creation game session"""
    def __init__(self, window) -> None:

        # window setup
        self.window = window    # window for rendering

        # game status
        self.mode = 'game'
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
        self.player = objects.Snake()
        self.meal = objects.Meal()

        # fonts
        self.font_score = pygame.font.SysFont('Comic Sans MS', 40)
        self.font_pause = pygame.font.SysFont('Comic Sans MS', 64)
        self.font_over = pygame.font.SysFont('Comic Sans MS', 64)
        self.font_other = pygame.font.SysFont('Comic Sans MS', 32)

        # inscriptions
        self.score = self.font_score.render(f'SCORE: {self.scores}', True, pygame.Color('orange'))
        self.pause = self.font_pause.render('PAUSE', True, pygame.Color('orange'))
        self.game_over = self.font_over.render('GAME OVER', True, pygame.Color(220, 20, 60))
        self.text_1 = self.font_other.render('ESC      -   start menu', True, pygame.Color('orange'))
        self.text_2 = self.font_other.render('SPACE  -   restart', True, pygame.Color('orange'))

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
                # pause
                elif event.key == pygame.K_ESCAPE:
                    self.status = 'pause'
                break
            # events in pause
            elif event.type == pygame.KEYDOWN and self.status == 'pause':
                if event.key == pygame.K_ESCAPE:
                    self.status = 'play'
            # events in game over
            elif event.type == pygame.KEYDOWN and self.status == 'game over':
                if event.key == self.input_device.back:
                    self.mode = 'menu'
                if event.key == self.input_device.start:
                    self.mode = 'reset'

    def update(self):
        """update state game"""
        if self.status == 'play':
            if self.player.get_place() == self.meal.get_place():    # check eating and next actions
                self.scores += 1
                self.score = self.font_score.render(f'SCORE: {self.scores}', True, pygame.Color('orange'))
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

        # display inscriptions
        self.window.blit(self.score, (settings.resolution[0] - 300, 0))    # display score

        if self.status == 'pause':    # display pause
            self.window.blit(self.pause, (settings.resolution[0]/2 - 100, settings.resolution[1]/2 - 100))

        if self.status == 'game over':    # display game over menu
            self.window.blit(self.game_over, (settings.resolution[0] / 2 - 200, settings.resolution[1] / 2 - 100))
            self.window.blit(self.text_1, (settings.resolution[0] / 2 - 180, settings.resolution[1] / 2))
            self.window.blit(self.text_2, (settings.resolution[0] / 2 - 180, settings.resolution[1] / 2 + 50))

        pygame.display.update()

    def run(self):
        self.event()
        self.update()
        self.render()
