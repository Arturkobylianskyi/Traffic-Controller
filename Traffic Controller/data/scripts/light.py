import pygame.draw
from time import time

from data.scripts.sprite import Sprite

class TraficLight:
    TRAFFIC_LIGHTS = [
        Sprite("data\\graphics\\trafficLights\\trafficLight.png"), # import światel
        Sprite("data\\graphics\\trafficLights\\redTrafficLight.png"),# import czerwonego światla
        Sprite("data\\graphics\\trafficLights\\yellowTrafficLight.png"),
        Sprite("data\\graphics\\trafficLights\\greenTrafficLight.png")
    ]

    def __init__(self, pos, angle, light = "red"):
        if light == "green":
            self.sprite = TraficLight.TRAFFIC_LIGHTS[3]
            self.nowLight = "green"
        else:
            self.sprite = TraficLight.TRAFFIC_LIGHTS[1]
            self.nowLight = "red"

        self.position = pos
        self.angle = angle

        self.animation = False
        self.startAnimation = 0
        self.timeAnimation = 0

        if angle == 0:
            self.stop_collider = [pos[0]+155, pos[1]+147]
        elif angle == 90:
            self.stop_collider = [pos[0] + 105, pos[1] + 57]
        elif angle == 180:
            self.stop_collider = [pos[0]+18, pos[1]+107]
        elif angle == 270:
            self.stop_collider = [pos[0] + 63, pos[1] + 197]

        self.collider_for_click = self.stop_collider.copy()

    def switch(self, pos):
        if abs(pos[0] - self.collider_for_click[0]) < 20 and abs(pos[1] - self.collider_for_click[1]) < 20 and self.animation == False:
            self.animation = True
            self.startAnimation = time()

    def draw(self, screen, show_way = False):
        self.sprite.draw(screen, self.position, self.angle)

        if show_way:
            for a in range(len(self.stop_collider)):
               pygame.draw.circle(screen, (255, 0, 0), self.stop_collider, 15)

    def update(self):
        self.timeAnimation = time() - self.startAnimation

        if self.animation:
            if self.nowLight == "red":
                if 0 <= self.timeAnimation < 2:
                    self.sprite = TraficLight.TRAFFIC_LIGHTS[1]
                elif 2 <= self.timeAnimation < 4:
                    self.sprite = TraficLight.TRAFFIC_LIGHTS[2]
                    self.stop_collider = []
                else:
                    self.nowLight = "green"
                    self.sprite = TraficLight.TRAFFIC_LIGHTS[3]
                    self.animation = False
                    self.startAnimation = 0
                    self.timeAnimation = 0

            else:
                if 0 <= self.timeAnimation < 2:
                    if (self.timeAnimation % 1) < 0.5:
                        self.sprite = TraficLight.TRAFFIC_LIGHTS[3]
                    else:
                        self.sprite = TraficLight.TRAFFIC_LIGHTS[0]
                elif 2 <= self.timeAnimation < 4:
                    self.sprite = TraficLight.TRAFFIC_LIGHTS[2]
                    self.stop_collider = self.collider_for_click.copy()
                else:
                    self.nowLight = "red"
                    self.sprite = TraficLight.TRAFFIC_LIGHTS[1]
                    self.animation = False
                    self.startAnimation = 0
                    self.timeAnimation = 0