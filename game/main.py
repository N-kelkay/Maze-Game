import turtle
import math

# Top left block of maze is (-288, 288), top right (288,288), bottom left (-288, -288), bottom right (288, -288)

win = turtle.Screen()
win.bgcolor("black")
win.title("A Maze Game")
win.setup(700, 700)

# Register shapes
turtle.register_shape("Red-brick-wall.gif")
turtle.register_shape("CatGifLeft.gif")
turtle.register_shape("CatGifRight.gif")


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
        self.shape("CatGifLeft.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        # self.goto(self.xcor,self.ycor+16)
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # self.goto(self.xcor,self.ycor-16)
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # self.goto(self.xcor-16,self.ycor)
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # self.goto(self.xcor+16,self.ycor)
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Create levels list
levels = [""]

# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXX XXXXXX       XX    X",
    "XXX   XXXX       XXX    X",
    "XX  P  XX        XXX    X",
    "XXX     X    XXXXXXX    X",
    "XXX         XXXXXXX     X",
    "XXXX    X    XXXX      TX",
    "XXX    XX     XXX    XXXX",
    "XX    XXX     XXX     XXX",
    "X     XXX     XXXXX     X",
    "XX    XXXXX   XXXXXX    X",
    "XXX  XXXX     XXX       X",
    "X   XXXXX    XXXX       X",
    "X    XXXXXXXXXXXXXXX    X",
    "XX      XXXXXXXXXXXX    X",
    "XXX              XXXX   X",
    "XXXX             XXXX   X",
    "XXXXXXXXXXXXX    XXX    X",
    "XXXXXXXXXXXXX    XXX    X",
    "XXX       XXX    XXX    X",
    "X                XXX    X",
    "XXXX       XXXXXXXX     X",
    "XXXXXX   XXXXXXXX      XX",
    "X                     XXX",
    "X                   XXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_2=[
    "XXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XX          XXXXXXXXX",
    "X  XX          XXXXXXXXX",
    "X      XXXXXX  XXXXXXXXX",
    "XXX  XXXXXXXX  XXXXXXXXX",
    "XX   XXXX      XXXXXXXXX",
    "X    XXXX      XXXXXXXXX",
    "X  XXXXXXXXXXXXXXXXXXXXX",
    "X  X           XXXXXXXXX",
    "X  XXXXX XXXX  XXXXXXXXX",
    "X        X  X  XXXXXXXXX",
    "XXXXXXX  X    TXXXXXXXXX",
    "X        XXXXXXXXXXXXXXX",
    "X  XX          XXXXXXXXX",
    "X  XXXX        XXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXX"
  ]
level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXX          XXX",
    "X           XXXXXX  XXXX",
    "X  XXXXXXX          XXXX",
    "X  XXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXXXXXXXXXXXXXXXX",
    "X                      X",
    "XXXXXXX  XXXXXXXXXXXXXXX",
    "XXXXXX   XXXXXXXXXXXXXXX",
    "XXXXXX                 X",
    "XXXXXX   XXXXXXXXXXXXX X",
    "XXXXXX   XXXXXXXXXXXXX X",
    "X                      X",
    "XXXXX    XXXXXXXXXX    X",
    "X        XXXXXXXXXXX XXX",
    "XXXXXX   XXXXXXXXXXX XXX",
    "X                      X",
    "XXXXXX   XXXX   XXXXXXXX",
    "XXXXXX   XXXX   XXXXXXXX",
    "XXXXX    XXXX          X",
    "X               X     TX",
    "XXXXXXX   XXXXXXX  XXXXX",
    "XXXXXX    XXXXXXX  XXXXX",
    "XXXXXXXX           XXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add a treasure list
treasures = []

levels.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("Red-brick-wall.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))


pen = Pen()
player = Player()

walls = []

setup_maze(levels[1])
print(walls)

turtle.listen()
turtle.onkey(player.go_left,'Left')
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')
win.tracer(0)

while True:

    for treasure in treasures:
        if player.is_collision(treasure):

            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    win.update()
