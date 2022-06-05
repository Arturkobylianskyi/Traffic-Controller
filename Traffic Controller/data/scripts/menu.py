import pygame

from data.scripts import settings as s
from data.scripts.button import Button
from data.scripts.text import Text
from data.scripts.level import Level
from data.scripts.sprite import Sprite

def ButtonBack(obj):
    obj.b_back.not_active()

    obj.b_level1.not_active()
    obj.b_level2.not_active()
    obj.b_level3.not_active()
    obj.b_level4.not_active()
    obj.b_level5.not_active()
    obj.b_level6.not_active()
    obj.b_level7.not_active()
    obj.b_level8.not_active()
    obj.b_level9.not_active()
    obj.b_level10.not_active()

    obj.b_levels.active()
    obj.b_settings.active()
    obj.b_exit.active()

def ButtonLevel(obj):
    obj.b_levels.not_active()
    obj.b_settings.not_active()
    obj.b_exit.not_active()
    obj.b_back.active()

    obj.b_level1.active()
    obj.b_level2.active()
    obj.b_level3.active()
    obj.b_level4.active()
    obj.b_level5.active()
    obj.b_level6.active()
    obj.b_level7.active()
    obj.b_level8.active()
    obj.b_level9.active()
    obj.b_level10.active()

def ButtonSettings(obj):
    obj.b_levels.not_active()
    obj.b_settings.not_active()
    obj.b_exit.not_active()

    obj.b_back.active()

def ButtonStartGame(obj, numberLevel, app):
    app.scene = "Game"
    app.game = Level(app, numberLevel)

    obj.b_back.not_active()

    obj.b_level1.not_active()
    obj.b_level2.not_active()
    obj.b_level3.not_active()
    obj.b_level4.not_active()
    obj.b_level5.not_active()
    obj.b_level6.not_active()
    obj.b_level7.not_active()
    obj.b_level8.not_active()
    obj.b_level9.not_active()
    obj.b_level10.not_active()

def ButtonExit(obj):
    pygame.quit()
    exit()

class Menu:
    def __init__(self, screen, app):
        self.wallpaper = Sprite("data/graphics/background.png")
        self.t_trafficController = Text("Traffic Controller", (90, 180, 216), 60, "Mukta-Regular")
        self.t_createdBy = Text("Good Game", (255, 255, 255), 15)

        # Button for Main Menu
        self.b_levels = Button(screen, [ButtonLevel, self], [25, 25], [200, 50], (255, 128, 0), (255, 148, 20), Text("Levels", (255, 255, 255), 25, "Mukta-Regular"))
        self.b_settings = Button(screen, [ButtonSettings, self], [25, 125], [200, 50], (0, 128, 255), (20, 148, 255), Text("Settings", (255, 255, 255), 25, "Mukta-Regular"))
        self.b_exit = Button(screen, [ButtonExit, self], [25, 225], [200, 50], (200, 50, 20), (220, 70, 40), Text("Exit", (255, 255, 255), 25, "Mukta-Regular"))

        # Button for levels and settings

        self.b_back = Button(screen, [ButtonBack, self], [s.SIZE["width"]-125, 25], [100, 25], (100, 100, 255), (120, 120, 255), Text("Back", (255, 255, 255), 20, "Mukta-Regular"))



        # Buttons for levels
        self.b_level1 = Button(screen, [ButtonStartGame, self, 1, app], [100, 100], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 1", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level2 = Button(screen, [ButtonStartGame, self, 2, app], [100, 200], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 2", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level3 = Button(screen, [ButtonStartGame, self, 3, app], [100, 300], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 3", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level4 = Button(screen, [ButtonStartGame, self, 4, app], [200, 300], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 4", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level5 = Button(screen, [ButtonStartGame, self, 5, app], [300, 300], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 5", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level6 = Button(screen, [ButtonStartGame, self, 6, app], [300, 200], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 6", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level7 = Button(screen, [ButtonStartGame, self, 7, app], [400, 200], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 7", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level8 = Button(screen, [ButtonStartGame, self, 8, app], [500, 200], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 8", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level9 = Button(screen, [ButtonStartGame, self, 9, app], [500, 300], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 9", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_level10 = Button(screen, [ButtonStartGame, self, 10, app], [600, 300], [50, 50], (0, 128, 235), (20, 148, 255), Text("Lv. 10", (255, 255, 255), 20, "Mukta-Regular"))



        self.b_levels.active()
        self.b_settings.active()
        self.b_exit.active()

    def draw(self, screen):
        self.wallpaper.draw(screen, [0, 0])
        self.t_createdBy.print(screen, [s.SIZE["width"]*0.5, s.SIZE["height"]-20])
        self.t_trafficController.print(screen, [s.SIZE["width"]*0.5, s.SIZE["height"]*0.05])