import pygame
from gc import get_objects

from data.scripts import settings as s
from data.scripts.button import Button
from data.scripts.menu import Menu
from data.scripts.level import Level


class App:

    def __init__(self):
        pygame.init()                                                              # Initialization PyGame
        self.screen = pygame.display.set_mode((s.SIZE["width"], s.SIZE["height"])) # Set screen (width x height)
        pygame.display.set_caption(s.NAME)                                         # Set name screen
        self.clock = pygame.time.Clock()                                           # In-game clock

        self.scene = "Main Menu"

        self.menu = Menu(self.screen, self)
        self.game = None

    def loop(self):                                                                # Main loop screen
        self.screen.fill((0, 0, 0))                                                # Clear screen

        for event in pygame.event.get():                                           # Main events in PyGame
            if event.type == pygame.QUIT:                                          # If you want to close the program...
                 pygame.quit()
                 exit()
            if event.type == pygame.MOUSEBUTTONDOWN:                               # If you click button mouse...
                [btn.click() for btn in Button.buttons]                           # Click all buttons

                if self.scene == "Game":
                    [light.switch(pygame.mouse.get_pos()) for light in self.game.trafficLighs]

        if self.scene == "Main Menu":
            self.menu.draw(self.screen)
        elif self.scene == "Game":
            self.game.draw(self.screen, s.DEBUG) # debug - False off True on
            self.game.update()

        [btn.draw() for btn in Button.buttons]                                    # Draw all buttons


        pygame.display.update()                                                    # Update display
        self.clock.tick(s.FPS)                                                   # ex. 60 fps