import pygame.draw

from data.scripts.sprite import Sprite

class Road:
    ROADS = [
        Sprite("data\\graphics\\roads\\tile0.png"),  # Grass Tile

        Sprite("data\\graphics\\roads\\tile1.png", 90),  # One line road Tile
        Sprite("data\\graphics\\roads\\tile1.png"),

        Sprite("data\\graphics\\roads\\tile2.png"),  # End of the road Tile
        Sprite("data\\graphics\\roads\\tile2.png", 270),
        Sprite("data\\graphics\\roads\\tile2.png", 180),
        Sprite("data\\graphics\\roads\\tile2.png", 90),

        Sprite("data\\graphics\\roads\\tile3.png", 90),  # Not straight road Tile
        Sprite("data\\graphics\\roads\\tile3.png"),
        Sprite("data\\graphics\\roads\\tile3.png", 270),
        Sprite("data\\graphics\\roads\\tile3.png", 180),

        Sprite("data\\graphics\\roads\\tile4.png"),  # Crossroads (3 ways)
        Sprite("data\\graphics\\roads\\tile4.png", 270),
        Sprite("data\\graphics\\roads\\tile4.png", 180),
        Sprite("data\\graphics\\roads\\tile4.png", 90),

        Sprite("data\\graphics\\roads\\tile5.png")  # Crossroads (4 ways)
    ]

    WAY = [{"crossroad": False},

           {"crossroad": False, "up": {"down" : [[106, 0], [106, 256]]}, "down": {"up" : [[150, 256], [150, 0]]}},
           {"crossroad": False, "right": {"left" : [[256, 106], [0, 106]]}, "left": {"right": [[0, 150], [256, 150]]}},

           {"crossroad": False, "left": {"right": [[0, 150], [228, 150]]}},
           {"crossroad": False, "up": {"down":[[106, 0], [106, 228]]}},
           {"crossroad": False, "right": {"left": [[256, 106], [28, 106]]}},
           {"crossroad": False, "down": {"up": [[150, 256], [150, 28]]}},

           {"crossroad": False, "down": {"left": [[150, 256], [150, 166], [140, 133], [116, 116], [90, 106], [0, 106]]}, "left": {"down":[[0, 150], [90, 150], [106, 166], [106, 256]]}},
           {"crossroad": False, "up": {"left": [[106, 0], [106, 90], [90, 106], [0, 106]]}, "left": {"up": [[0, 150], [90, 150], [123, 140], [140, 123], [150, 90], [150, 0]]}},
           {"crossroad": False, "up": {"right": [[106, 0], [106, 90], [116, 123], [133, 140], [166, 150], [256, 150]]}, "right": {"up": [[256, 106], [166, 106], [150, 90], [150, 0]]}},
           {"crossroad": False, "right": {"down": [[256, 106], [166, 106], [133, 116], [116, 133], [106, 166], [106, 256]]}, "down": {"right": [[150, 256], [150, 166], [166, 150], [256, 150]]}},

           {"crossroad": True, "up": {"right": [[106, 0], [106, 90], [116, 123], [133, 140], [166, 150], [256, 150]], "down": [[106, 0], [106, 256]]}, "right": {"up": [[256, 106], [166, 106], [150, 90], [150, 0]], "down": [[256, 106], [166, 106], [133, 116], [116, 133], [106, 166], [106, 256]]}, "down": {"up": [[150, 256], [150, 0]], "right": [[150, 256], [150, 166], [166, 150], [256, 150]]}},
           {"crossroad": True, "right": {"down": [[256, 106], [166, 106], [133, 116], [116, 133], [106, 166], [106, 256]], "left": [[255, 106], [0, 106]]}, "down": {"right": [[150, 256], [150, 166], [166, 150], [256, 150]], "left": [[150, 256], [150, 166], [140, 133], [116, 116], [90, 106], [0, 106]]}, "left": {"right": [[0, 150], [256, 150]], "down": [[0, 150], [90, 150], [106, 166], [106, 256]]}},
           {"crossroad": True, "up": {"down": [[106, 0], [106, 256]], "left": [[106, 0], [106, 90], [90, 106], [0, 106]]}, "down": {"up": [[150, 256], [150, 0]], "left": [[150, 256], [150, 166], [140, 133], [116, 116], [90, 106], [0, 106]]}, "left": {"up": [[0, 150], [90, 150], [123, 140], [140, 123], [150, 90], [150, 0]], "down": [[0, 150], [90, 150], [106, 166], [106, 256]]}},
           {"crossroad": True, "up": {"left": [[106, 0], [106, 90], [90, 106], [0, 106]], "right": [[106, 0], [106, 90], [116, 123], [133, 140], [166, 150], [256, 150]]}, "right": {"up": [[256, 106], [166, 106], [150, 90], [150, 0]], "left": [[256, 106], [0, 106]]}, "left": {"up": [[0, 150], [90, 150], [123, 140], [140, 123], [150, 90], [150, 0]], "right": [[0, 150], [256, 150]]}},

           {"crossroad": True, "up": {"right": [[106, 0], [106, 90], [116, 123], [133, 140], [166, 150], [256, 150]], "down": [[106, 0], [106, 256]], "left": [[106, 0], [106, 90], [90, 106], [0, 106]]}, "right": {"up": [[256, 106], [166, 106], [150, 90], [150, 0]], "down": [[256, 106], [166, 106], [133, 116], [116, 133], [106, 166], [106, 256]], "left": [[256, 106], [0, 106]]}, "down": {"up": [[150, 256], [150, 0]], "right": [[150, 256], [150, 166], [166, 150], [256, 150]], "left": [[150, 256], [150, 166], [140, 133], [116, 116], [90, 106], [0, 106]]}, "left": {"up": [[0, 150], [90, 150], [123, 140], [140, 123], [150, 90], [150, 0]], "right": [[0, 150], [156, 150]], "down": [[0, 150], [90, 150], [106, 166], [106, 256]]}},

           ]

    def __init__(self, index = 0):
        self.index = index
        self.sprite = Road.ROADS[self.index]
        self.way = Road.WAY[self.index]

    def draw(self, screen, tile_x, tile_y, show_way = False):
        self.sprite.draw(screen, (256 * tile_x, 256 * tile_y))

        if show_way:
            for key in self.way:
                if key == "crossroad":
                    continue

                for key2 in self.way[key]:
                    for a in range(len(self.way[key][key2]) - 1):
                        pygame.draw.line(screen, (0, 150, 255), [256 * tile_x + self.way[key][key2][a][0], 256 * tile_y + self.way[key][key2][a][1]], [256 * tile_x + self.way[key][key2][a + 1][0], 256 * tile_y + self.way[key][key2][a + 1][1]])


    def __str__(self):
        return "Index {0}, Way {1}".format(self.index, self.way)