import pygame
from math import sin, cos, acos, pi
from time import time
from data.scripts import settings as s
from data.scripts.sprite import Sprite

class Car:
    CARS = [
        Sprite("data\\graphics\\cars\\car1.png"),
        Sprite("data\\graphics\\cars\\car2.png"),
        Sprite("data\\graphics\\cars\\car3.png"),
        Sprite("data\\graphics\\cars\\car4.png"),
        Sprite("data\\graphics\\cars\\car5.png"),
        Sprite("data\\graphics\\cars\\car6.png"),
        Sprite("data\\graphics\\cars\\car7.png"),
        Sprite("data\\graphics\\cars\\car8.png"),
        Sprite("data\\graphics\\cars\\car9.png"),
        Sprite("data\\graphics\\cars\\car10.png"),
        Sprite("data\\graphics\\cars\\car11.png"),
        Sprite("data\\graphics\\cars\\car12.png"),
        Sprite("data\\graphics\\cars\\car13.png"),
        Sprite("data\\graphics\\cars\\car14.png"),
        Sprite("data\\graphics\\cars\\car15.png"),

    ]

    def __init__(self, indexCar, turns, startPos, queue, roads):
        self.index = indexCar
        self.sprite = Car.CARS[self.index]

        self.indexWay = 1
        self.way = []

        self.speed = s.CAR_SPEED
        self.position = [0, 0]
        self.angle = 0

        self.car_collider = [[0, 0], [0, 0]]
        self.check_collider = [0, 0]

        self.stop = False
        self.finish = False
        self.start = False

        self.get_direction(turns, startPos, queue, roads)

        #self.position = [256*4+150, 256*2]

        self.clock = time()




    def draw(self, screen, show_way = False):
        if self.finish == False:
            self.sprite.draw(screen, [self.position[0]-30, self.position[1]-15], self.angle+10)

        if show_way:
            pygame.draw.circle(screen, (255, 128, 0), self.way[self.indexWay], 6)

            for a in range(len(self.way)-1):
               pygame.draw.line(screen, (255, 0, 0), self.way[a], self.way[a+1], 3)

            pygame.draw.circle(screen, (0, 255, 0), self.position, 3)

            for a in range(len(self.car_collider)):
                pygame.draw.circle(screen, (255, 0, 0), self.car_collider[a], 15)

            if self.stop:
                pygame.draw.circle(screen, (255, 255, 0), self.check_collider, 5)
            else:
                pygame.draw.circle(screen, (0, 255, 0), self.check_collider, 5)




    def collision_detect(self, others, lights):
        if self.stop:
            self.stop = False


        for a in range(len(others)):

            if others[a] == self or others[a].finish:
                continue

            for b in range(2):
                if (abs(self.check_collider[0] - others[a].car_collider[b][0]) < 15 and abs(self.check_collider[1] - others[a].car_collider[b][1]) < 15):
                    self.stop = True
                    break


            if self.stop:
                break

        for a in range(len(lights)):
            if len(lights[a].stop_collider) > 0:
                if (abs(self.check_collider[0] - lights[a].stop_collider[0]) < 15) and (abs(self.check_collider[1] - lights[a].stop_collider[1]) < 15):
                    self.stop = True
                    break



    def speed_control(self, diffAngle, dt):
        if self.stop == False:
            if self.speed < diffAngle*4:
                self.speed += 5 * dt
            else:
                self.speed -= 5 * dt
        else:
            if self.speed > 0:
                self.speed -= 150 * dt
            if self.speed < 0:
                self.speed = 0

    def change_angle(self, dt, scalar = 5):
        self.angle -= 1

        a = [self.way[self.indexWay][0]-self.position[0], -(self.way[self.indexWay][1]-self.position[1])]
        cosAlfa = a[0]/((a[0]**2 + a[1]**2)**(1/2))
        alfa = (acos(cosAlfa))*180/pi

        if (self.position[1] < self.way[self.indexWay][1]):
            alfa = 360 - alfa

        if alfa > self.angle:
            diffLeft = alfa - self.angle
            diffRight = 360 - alfa + self.angle
        else:
            diffLeft = 360 - self.angle + alfa
            diffRight = self.angle - alfa

        diff = min(diffLeft, diffRight)

        if diffLeft < diffRight:
            self.angle += scalar * dt * diffLeft
        else:
            self.angle -= scalar * dt * diffRight

        self.speed_control(diff, dt)

        if self.angle < 0:
            self.angle += 360
        if self.angle > 360:
            self.angle -= 360

    def change_position(self, dt):
        degree = 270 - self.angle*pi/180
        self.position[0] += self.speed * dt * cos(degree)
        self.position[1] += self.speed * dt * sin(degree)

    def checkpoint(self):
        if abs(self.position[0] - self.way[self.indexWay][0]) < 10 and abs(self.position[1] - self.way[self.indexWay][1]) < 10:
            if self.indexWay < len(self.way)-1:
                self.indexWay += 1
            else:
                self.finish = True

    def update_position_collider(self):# przesuniecie kolajedera do pozycji samochodu
        self.car_collider[0] = [15*sin((self.angle+100)*pi/180)+self.position[0], 15*cos((self.angle+100)*pi/180)+self.position[1]]
        self.car_collider[1] = [15*sin((self.angle-80)*pi/180)+self.position[0], 15*cos((self.angle-80)*pi/180)+self.position[1]]

        self.check_collider = [50*sin((self.angle+100)*pi/180)+self.position[0], 40*cos((self.angle+100)*pi/180)+self.position[1]]

    def update(self):
        if self.start:
            self.change_angle(time()-self.clock)
            self.change_position(time()-self.clock)
            self.checkpoint()

            self.update_position_collider()

            self.clock = time()




    def get_direction(self, turns, startPos, queue, roads):
        indexTurns = 0

        if startPos[0] == -1:
            self.position = [-120*queue, 256*startPos[1]+150]
            startPos[0] = 0
            nowTurn = "left"
            self.angle = 0
        elif startPos[0] == 5:
            self.position = [1280+120*queue, 256*startPos[1]+150]
            startPos[0] = 4
            nowTurn = "right"
            self.angle = 180

        if startPos[1] == -1:
            self.position = [256*startPos[0]+106, -120*queue]
            startPos[1] = 0
            nowTurn = "up"
            self.angle = 90
        elif startPos[1] == 3:
            self.position = [256*startPos[0]+106, 768+120*queue]
            startPos[1] = 2
            nowTurn = "down"
            self.angle = 270

        self.way.append(self.position.copy())

        while (0 <= startPos[0] <= 4 and 0 <= startPos[1] <= 2):
            if roads[startPos[1]][startPos[0]].way["crossroad"]:
                for key in roads[startPos[1]][startPos[0]].way[nowTurn]:
                    if key == turns[indexTurns]:
                        for a in range(len(roads[startPos[1]][startPos[0]].way[nowTurn][key])):
                            self.way.append([256*startPos[0]+roads[startPos[1]][startPos[0]].way[nowTurn][key][a][0], 256*startPos[1]+roads[startPos[1]][startPos[0]].way[nowTurn][key][a][1]])
                        nowTurn = key
                indexTurns += 1
            else:
                for key in roads[startPos[1]][startPos[0]].way[nowTurn]:
                    for a in range(len(roads[startPos[1]][startPos[0]].way[nowTurn][key])):
                        self.way.append([256*startPos[0]+roads[startPos[1]][startPos[0]].way[nowTurn][key][a][0], 256*startPos[1]+roads[startPos[1]][startPos[0]].way[nowTurn][key][a][1]])
                    nowTurn = key

            if 3 <= roads[startPos[1]][startPos[0]].index <= 6:
                break

            if nowTurn == "up":
                startPos[1] -= 1
                nowTurn = "down"
            elif nowTurn == "down":
                startPos[1] += 1
                nowTurn = "up"
            elif nowTurn == "left":
                startPos[0] -= 1
                nowTurn = "right"
            elif nowTurn == "right":
                startPos[0] += 1
                nowTurn = "left"

        index = 0
        while index < len(self.way)-1:
            if self.way[index] == self.way[index+1]:
                del self.way[index]

            index += 1