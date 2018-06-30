import turtle
import math

# Top left block of maze is (-288, 288), top right (288,288), bottom left (-288, -288), bottom right (288, -288)

win = turtle.Screen()
win.bgcolor("black")
win.title("A Maze Game")
win.setup(700, 700)


# create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

def go_up(self):
    #self.goto(self.xcor,self.ycor+16)
    move_to_x=player.xcor()
    move_to_y=player.ycor()+24



# Create levels list
levels = [""]

# Define first level
level_1 = [
        "XXXXXXXXXXXXXXXXXXXXXXXXX"
        "XP XXXXXXX          XXXXX"
        "X  XXXXXXX  XXXXXX  XXXXX"
        "X       XX  XXXXXX  XXXXX"
        "X       XX  XXX        XX"
        "XXXXXX  XX  XXX        XX"
        "XXXXXX  XX  XXXXXX  XXXXX"
        "XXXXXX  XX    XXXX  XXXXX"
        "X  XXX        XXXX  XXXXX"
        "X  XXX  XXXXXXXXXXXXXXXXX"
        "X         XXXXXXXXXXXXXXX"
        "X                XXXXXXXX"
        "XXXXXXXXXXXX     XXXXX  X"
        "XXXXXXXXXXXXXXX  XXXXX  X"
        "XXX  XXXXXXXXXX         X"
        "XXX                     X"
        "XXX         XXXXXXXXXXXXX"
        "XXXXXXXXXX  XXXXXXXXXXXXX"
        "XXXXXXXXXX              X"
        "XX   XXXXX              X"
        "XX   XXXXXXXXXXXXX  XXXXX"
        "XX    XXXXXXXXXXXX  XXXXX"
        "XX           XXXX       X"
        "XXXX                    X"
        "XXXXXXXXXXXXXXXXXXXXXXXXX"
        ]


levels.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

            if character == "P":
                player.goto(screen_x, screen_y)


pen = Pen()
player = Player()

setup_maze(levels[1])

while True:
    pass
