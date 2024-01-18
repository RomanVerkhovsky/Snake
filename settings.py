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


#                                     DRAFTS
#
# # menu level 0
# self.text_1 = self.font_menu.render('START GAME', True, pygame.Color('orange'))
# self.text_2 = self.font_menu.render('  SETTINGS', True, pygame.Color('orange'))
#
# # menu level 1
# self.text_3 = self.font_menu.render('Input settings', True, pygame.Color('orange'))
# self.text_4 = self.font_menu.render('Info', True, pygame.Color('orange'))
#
# # list contain menu levels to rendering
# self.level_menu_1 = [(self.text_1, (settings.resolution[0] / 2 - 150, settings.resolution[1] / 2)),
#                      (self.text_2, (settings.resolution[0] / 2 - 150, settings.resolution[1] / 2 + 50))]
#
# self.level_menu_2 = [(self.text_3, (settings.resolution[0] / 2 - 150, settings.resolution[1] / 2))]
#
# # current level menu and position of cursor
# self.menu_selection = 1
# self.dict_levels_menu = {1: self.level_menu_1,
#                          2: self.level_menu_2}

# FROM RANDER
# for i in range(len(self.dict_levels_menu[self.menu_selection])):
#     self.window.blit(self.dict_levels_menu[self.menu_selection][i][0],
#                      self.dict_levels_menu[self.menu_selection][i][1])
