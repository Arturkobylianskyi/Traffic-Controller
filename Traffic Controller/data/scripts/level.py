import pygame
from time import time

import data.scripts.settings as s
from data.scripts.button import Button
from data.scripts.text import Text
from data.scripts.road import Road
from data.scripts.car import Car
from data.scripts.light import TraficLight

def ButtonBack(obj, app):
    obj.b_back.not_active()
    obj.b_start.not_active()
    app.menu.b_levels.active()
    app.menu.b_settings.active()
    app.menu.b_exit.active()
    app.scene = "Main Menu"

def ButtonStart(obj):
    obj.b_start.not_active()

    for a in range(len(obj.cars)):
        obj.cars[a].start = True
        obj.cars[a].clock = time()
        obj.timer = time()

class Level:

    def __init__(self, app, level):
        self.level = level
        self.indexRoads = s.LEVELS[level-1]
        self.indexCars = s.CARS_IN_LEVELS[level-1]
        self.roads = []
        self.cars = []
        self.trafficLighs = []

        self.winner = False


        self.timer = 0
        self.finishTime = 0

        self.b_back = Button(app.screen, [ButtonBack, self, app], [s.SIZE["width"]-125, 25], [100, 25], (100, 100, 255), (120, 120, 255), Text("Back", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_start = Button(app.screen, [ButtonStart, self], [s.SIZE["width"]-125, 75], [100, 25], (100, 150, 100), (120, 170, 120), Text("Start", (255, 255, 255), 20, "Mukta-Regular"))
        self.b_back.active()
        self.b_start.active()

        for a in range(len(self.indexRoads)):
            self.roads.append([])
            for b in range(len(self.indexRoads[a])):
                self.roads[a].append(Road(self.indexRoads[a][b]))

                if self.indexRoads[a][b] == 11:
                    self.trafficLighs.append(TraficLight([b * 256 + 45, a * 256 + 150], 90))
                    self.trafficLighs.append(TraficLight([b * 256 + 200, a * 256], 180))
                    self.trafficLighs.append(TraficLight([b * 256 + 45, a * 256 - 150], 270))
                elif self.indexRoads[a][b] == 12:
                    self.trafficLighs.append(TraficLight([b * 256 - 110, a * 256], 0))
                    self.trafficLighs.append(TraficLight([b * 256 + 45, a * 256 + 150], 90))
                    self.trafficLighs.append(TraficLight([b * 256 + 200, a * 256], 180))
                elif self.indexRoads[a][b] == 13:
                    self.trafficLighs.append(TraficLight([b * 256 - 110, a * 256], 0))
                    self.trafficLighs.append(TraficLight([b * 256 + 45, a * 256 + 150], 90))
                    self.trafficLighs.append(TraficLight([b * 256 + 45, a * 256 - 150], 270))
                elif self.indexRoads[a][b] == 14:
                    self.trafficLighs.append(TraficLight([b*256-110, a*256], 0))
                    self.trafficLighs.append(TraficLight([b * 256+200, a * 256], 180))
                    self.trafficLighs.append(TraficLight([b * 256+45, a * 256-150], 270))
                elif self.indexRoads[a][b] == 15:
                    self.trafficLighs.append(TraficLight([b * 256 - 110, a * 256], 0))
                    self.trafficLighs.append(TraficLight([b * 256 + 45, a * 256 + 150], 90))
                    self.trafficLighs.append(TraficLight([b * 256 + 200, a * 256], 180))
                    self.trafficLighs.append(TraficLight([b * 256 + 45, a * 256 - 150], 270))


        for a in range(len(self.indexCars)):
                self.cars.append(Car(self.indexCars[a][0], self.indexCars[a][1], self.indexCars[a][2], self.indexCars[a][3], self.roads))



    def draw(self, screen, DEBUG):
        for a in range(len(self.roads)):
            for b in range(len(self.roads[a])):
                self.roads[a][b].draw(screen, b, a, s.DEBUG)

        for a in range(len(self.cars)):
            self.cars[a].draw(screen, s.DEBUG)

        for a in range(len(self.trafficLighs)):
            self.trafficLighs[a].draw(screen, s.DEBUG)

        if s.DEBUG:
            for a in range(3):
                pygame.draw.line(screen, (0, 0, 0), [0, a*256], [256*5, a*256])

            for a in range(5):
                pygame.draw.line(screen, (0, 0, 0), [a*256, 0], [a*256, 256*3])

        if self.timer != 0 and self.winner == False:
            pygame.draw.rect(screen, (23, 23, 23), [0, 0, 100, 50])
            Text(str(round(time() - self.timer, 2)), (255, 255, 255), 30, "Mukta-Regular").print(screen, [15, 0], False)

        if self.winner:
            pygame.draw.rect(screen, (23, 23, 23), [0, 284, 1280, 200])
            Text("You win. Your time: " + str(round(self.timer, 2)), (255, 128, 0), 60, "Mukta-Regular").print(screen, [640, 384])


    def update(self):
        if self.winner == False:
            self.winner = True
            for a in range(len(self.cars)):
                if self.cars[a].finish:
                    continue
                else:
                    self.winner = False

                self.cars[a].collision_detect(self.cars, self.trafficLighs)
                self.cars[a].update()

            if self.winner:
                self.timer = time() - self.timer

            for a in range(len(self.trafficLighs)):
                self.trafficLighs[a].update()