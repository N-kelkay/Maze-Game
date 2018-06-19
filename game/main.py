import turtle


# Top left block of maze is (-288, 288), top right (288,288), bottom left (-288, -288), bottom right (288, -288)

win = turtle.scree()

win.bgcolor("black")

win.title("A Maze Game")

win.setup(700, 700)


# create Pen
class pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# Create levels list
levels = [""]


# Define first level
level_1 = [
        "XXXXXXXXXXXXXXXXXXXXXXXXX"
        "X  XXXXXXX          XXXXX"
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
