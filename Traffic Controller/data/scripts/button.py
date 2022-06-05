import pygame

class Button:
    buttons = []

    def __init__(self, screen, function, pos, size, color_background, homing_color, text = None):
        self.function = function
        self.screen = screen
        self.pos = pos
        self.size = size
        self.color_background = color_background
        self.homing_color = homing_color
        self.text = text
        self.activity = False

        Button.buttons.append(self)

    def not_active(self):
        self.activity = False

    def active(self):
        self.activity = True

    def draw(self):
        if self.activity:
            pos_mos = pygame.mouse.get_pos()
            if self.pos[0] <= pos_mos[0] <= self.size[0]+self.pos[0] and self.pos[1] <= pos_mos[1] <= self.size[1]+self.pos[1]:
                pygame.draw.rect(self.screen, self.homing_color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
            else:
                pygame.draw.rect(self.screen, self.color_background, (self.pos[0], self.pos[1], self.size[0], self.size[1]))

            if self.text != None:
                self.text.print(self.screen, [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2])

    def click(self):
        if self.activity:
            pos_mos = pygame.mouse.get_pos()
            if self.pos[0] <= pos_mos[0] <= self.size[0] + self.pos[0] and self.pos[1] <= pos_mos[1] <= self.size[1] + self.pos[1]:
                self.function[0](*self.function[1:])