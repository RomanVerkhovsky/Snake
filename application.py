import pygame
import settings
from game import Game


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

        # game status
        self.running = True
        self.game = None

    def run(self) -> None:
        """main game loop"""
        while self.running:
            # enter in game
            if self.game is None:
                self.game = Game(self.window)    # creation game session

            # events
            self.game.event()
            self.running = self.game.check_notQUIT    # check QUIT

            # update game state
            self.game.update()

            # rendering
            self.game.render()

            self.running = self.game.check_notQUIT  # check QUIT
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = App()
    app.run()
    pygame.quit()
