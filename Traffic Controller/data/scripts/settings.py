from random import randint

NAME = "Traffic Controller"
SIZE = {"width": 1280, "height": 768}
FPS = 60
DEBUG = False
CAR_SPEED = 100

LEVELS = [
    [
        [0, 0, 1, 0, 0],
        [2, 12, 14, 2, 7], # level 1
        [0, 1, 0, 0, 1]
    ],
    [
        [1, 0, 10, 2, 7],
        [9, 7, 1, 10, 13], # level 2
        [2, 14, 8, 1, 1]
    ],
    [
        [1, 0, 10, 13, 0],
        [9, 2, 15, 8, 0], #level 3
        [0, 0, 1, 0, 0]
    ]
]

CARS_IN_LEVELS = [
    [
        [randint(0, 14), ["right", "right"], [-1, 1], 1],
        [randint(0, 14), ["right", "up"], [-1, 1], 2],
        [randint(0, 14), ["down"], [-1, 1], 3],
        [randint(0, 14), ["right", "right"], [-1, 1], 4],
        [randint(0, 14), ["down"], [-1, 1], 5],
        [randint(0, 14), ["right", "right"], [-1, 1], 6],
        [randint(0, 14), ["down"], [-1, 1], 7],
        [randint(0, 14), ["right", "right"], [-1, 1], 8],

        [randint(0, 14), ["left", "down"], [2, -1], 1],
        [randint(0, 14), ["right"], [2, -1], 2],

        [randint(0, 14), ["left", "left"], [4, 3], 1],
        [randint(0, 14), ["left", "down"], [4, 3], 2],
        [randint(0, 14), ["up"], [4, 3], 3],
        [randint(0, 14), ["up"], [4, 3], 4],
        [randint(0, 14), ["left", "down"], [4, 3], 5],
        [randint(0, 14), ["up"], [4, 3], 6],
        [randint(0, 14), ["up"], [4, 3], 7],
        [randint(0, 14), ["left", "left"], [4, 3], 8],

        [randint(0, 14), ["right", "up"], [1, 3], 1],
        [randint(0, 14), ["right", "right"], [1, 3], 2],
        [randint(0, 14), ["left"], [1, 3], 3],
        [randint(0, 14), ["right", "up"], [1, 3], 4],
        [randint(0, 14), ["right", "up"], [1, 3], 5],
        [randint(0, 14), ["right", "up"], [1, 3], 6],
        [randint(0, 14), ["left"], [1, 3], 7]
    ],
    [
        [randint(0, 14), ["up"], [-1, 2], 1],
        [randint(0, 14), ["up"], [-1, 2], 2],
        [randint(0, 14), ["up"], [-1, 2], 3],
        [randint(0, 14), ["up"], [-1, 2], 4],
        [randint(0, 14), ["up"], [-1, 2], 5],

        [randint(0, 14), ["right", "down"], [0, -1], 1],
        [randint(0, 14), ["right", "down"], [0, -1], 2],
        [randint(0, 14), ["left"], [0, -1], 3],
        [randint(0, 14), ["left"], [0, -1], 4],
        [randint(0, 14), ["left"], [0, -1], 5],
        [randint(0, 14), ["left"], [0, -1], 6],
        [randint(0, 14), ["right", "left"], [0, -1], 7],
        [randint(0, 14), ["right", "down"], [0, -1], 8],

        [randint(0, 14), ["up", "left"], [4, 3], 1],
        [randint(0, 14), ["right"], [4, 3], 2],
        [randint(0, 14), ["right"], [4, 3], 3],
        [randint(0, 14), ["right"], [4, 3], 4],

        [randint(0, 14), ["down"], [3, 3], 1],
        [randint(0, 14), ["up", "left"], [3, 3], 2],
        [randint(0, 14), ["down"], [3, 3], 3],
        [randint(0, 14), ["up", "up"], [3, 3], 4],
        [randint(0, 14), ["down"], [3, 3], 5],
        [randint(0, 14), ["up", "left"], [3, 3], 6],
        [randint(0, 14), ["down"], [3, 3], 7],
        [randint(0, 14), ["up", "left"], [3, 3], 8],
        [randint(0, 14), ["up", "up"], [3, 3], 9],
        [randint(0, 14), ["down"], [3, 3], 10]

    ],
    [
        [randint(0, 14), ["up", "up"], [0, -1], 1],
        [randint(0, 14), ["up", "up"], [0, -1], 2],
        [randint(0, 14), ["up", "up"], [0, -1], 3],

        [randint(0, 14), ["left", "left"], [3, -1], 1],
        [randint(0, 14), ["down", "up", "up"], [3, -1], 2],
        [randint(0, 14), ["left", "right", "left", "left"], [3, -1], 3],
        [randint(0, 14), ["left", "left"], [3, -1], 4],
        [randint(0, 14), ["down", "up", "up"], [3, -1], 5],
        [randint(0, 14), ["down", "left"], [3, -1], 6],
        [randint(0, 14), ["left", "right", "left", "left"], [3, -1], 7],
        [randint(0, 14), ["down", "up", "down", "left"], [3, -1], 8],
        [randint(0, 14), ["down", "down"], [3, -1], 9],
        [randint(0, 14), ["left", "left"], [3, -1], 10],

        [randint(0, 14), ["right", "up"], [2, 3], 1],
        [randint(0, 14), ["up", "up"], [2, 3], 2]
    ]



]