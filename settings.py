import pygame


class InputDevice:
    """ class for settings of input """
    def __init__(self):
        self.right = pygame.K_d
        self.left = pygame.K_a
        self.down = pygame.K_s
        self.up = pygame.K_w
        self.start = pygame.K_SPACE
        self.back = pygame.K_ESCAPE

    def set_control(self, keymap: int):
        """1 - arrows, 2 - w a s d"""
        if keymap == 1:
            self.right = pygame.K_RIGHT
            self.left = pygame.K_LEFT
            self.down = pygame.K_DOWN
            self.up = pygame.K_UP
            self.start = pygame.K_SPACE
            self.back = pygame.K_ESCAPE

        if keymap == 2:
            self.right = pygame.K_d
            self.left = pygame.K_a
            self.down = pygame.K_s
            self.up = pygame.K_w
            self.start = pygame.K_SPACE
            self.back = pygame.K_ESCAPE


resolution = 900, 900    # size of window
control = InputDevice()    # creating a management module
