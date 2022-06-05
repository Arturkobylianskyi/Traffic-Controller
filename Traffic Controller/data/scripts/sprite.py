import pygame

class Sprite:

    def __init__(self, name, angle = 0):
        self.surface = pygame.image.load(name)
        self.surface = pygame.transform.rotate(self.surface, angle)

    def draw(self, screen, pos, angle = 0):
        w, h  = self.surface.get_size()

        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]

        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        pivot = pygame.math.Vector2(w/2, -h/2)

        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot

        origin = (pos[0] + min_box[0] - pivot_move[0], pos[1] - max_box[1] + pivot_move[1])

        rotated_image = pygame.transform.rotate(self.surface, angle)
        screen.blit(rotated_image, origin)