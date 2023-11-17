import pygame
import settings
from modes import Game, Menu


class App:
    """main class for creation game"""
    def __init__(self) -> None:
        pygame.init()  # initialization of pygame

        # window setup
        self.resolution = settings.resolution
        self.window = pygame.display.set_mode(self.resolution)  # creating window
        pygame.display.set_caption("Snake")  # set title
        self.clock = pygame.time.Clock()  # control frame rate
        self.fps = 10    # speed

        # app status
        self.running = True
        self.mode = 'menu'  # current mode of app
        self.menu = Menu(self.window)   # creating menu session
        self.game = None

    def run(self) -> None:
        """main game loop"""
        while self.running:
            # enter in menu
            if self.mode == 'menu':
                self.game = None    # reset game session
                self.menu.status = 'menu'
                self.menu.run()
                self.running = self.menu.check_notQUIT
                self.mode = self.menu.status  # change game status

            # enter in game
            if self.mode == 'game':
                if self.game is None:
                    self.game = Game(self.window)    # creation game session
                self.game.run()
                self.running = self.game.check_notQUIT  # check QUIT
                self.mode = self.game.mode  # change game status

            # reset game state
            if self.mode == 'reset':
                self.game = None    # reset game session
                self.mode = 'game'

            # frame rate
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = App()
    app.run()
    pygame.quit()
