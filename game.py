import pygame
import settings


class Game:
    """class for creation game session"""
    def __init__(self) -> None:
        pygame.init()  # initialization of pygame

        # window setup
        self.resolution = settings.resolution
        self.window = pygame.display.set_mode(self.resolution)  # creating window
        pygame.display.set_caption("Snake")  # set title
        self.clock = pygame.time.Clock()  # control frame rate
        self.fps = 10

        # game status
        self.running = True
        self.scores = 0

        # control settings
        self.input_device = settings.control

        # direct moving
        self.first_start = True
        self.direction = [0, 0]
        self.step = 30
        self.arrow_direction = 'right'

    def event(self):
        """event handling"""
        for event in pygame.event.get():
            # change direction moving
            if event.type == pygame.KEYDOWN:
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

    def update(self): pass

    def render(self): pass

    def run(self):
        self.event()

        self.clock.tick(self.fps)
