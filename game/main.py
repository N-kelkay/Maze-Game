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