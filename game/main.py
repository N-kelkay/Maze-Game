import turtle
import math
import random

# Top left block of maze is (-288, 288), top right (288,288), bottom left (-288, -288), bottom right (288, -288)

win = turtle.Screen()
win.bgcolor("black")
win.title("A Maze Game")
win.setup(700, 700)
win.tracer(0)

# Register shapes

images = ["Red-brick-wall.gif", "TreasureBox.gif",
          "MainCharacterR.gif", "MainCharacterL.gif", "EnemyPlayer.gif"]
for image in images:
    turtle.register_shape(image)


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
        self.shape("MainCharacterR.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        # self.goto(self.xcor,self.ycor+16)
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # self.goto(self.xcor,self.ycor-16)
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # self.goto(self.xcor-16,self.ycor)
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape("MainCharacterL.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # self.goto(self.xcor+16,self.ycor)
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape("MainCharacterR.gif")

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
        self.shape("TreasureBox.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("EnemyPlayer.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Create levels list
levels = [""]

# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXX XXXXXX       XX    X",
    "XXX P XXXX       XXX    X",
    "XX    XX        XXXT    X",
    "XXX     X    XXXXXXX    X",
    "XXXE        XXXXXXX     X",
    "XXXX    X     XXXX      X",
    "XXX    XX     XXX    XXXX",
    "XX    XXX     XXX     XXX",
    "X     XXX     XXXXX     X",
    "XX    XXXXX   XXXXXX    X",
    "XXX  XXXX     XXX       X",
    "X   XXXXX     XXXXE     X",
    "X    XXXXXXXXXXXXXXX    X",
    "XX      XXXXXXXXXXXX    X",
    "XXX              XXXX   X",
    "XXXX             XXXX   X",
    "XXXXXXXXXXXXX    XXX    X",
    "XXXXXXXXXXXXX    XXX    X",
    "XXX       XXX    XXX    X",
    "XE               XXX    X",
    "XXXX       XXXXXXXX     X",
    "XXXXXX   XXXXXXXX      XX",
    "X                     XXX",
    "X                   XXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XX          XXXXXXXXX",
    "X  XX E        XXXXXXXXX",
    "X      XXXXXX  XXXXXXXXX",
    "XXX    XXXXXX  XXXXXXXXX",
    "XX   XXXX      XXXXXXXXX",
    "X    XXXX  E   XXXXXXXXX",
    "X  XXXXXXXXXXXXXXXXXXXXX",
    "X  X           XXXXXXXXX",
    "X  XXXXX XXXX  XXXXXXXXX",
    "X E      X  X  XXXXXXXXX",
    "XXXXXXX  X     XXXXXXXXX",
    "X        XXXXXXXXXXXXXXX",
    "X  XX          XXXXXXXXX",
    "X  XXXX   T    XXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXX"
  ]
level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXX          XXX",
    "X          EXXXXXX  XXXX",
    "X  XXXXXXX          XXXX",
    "X  XXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXXXXXXXXXXXXXXXX",
    "X          E           X",
    "XXXXXXX  XXXXXXXXXXXXXXX",
    "XXXXXX   XXXXXXXXXXXXXXX",
    "XXXXXX                 X",
    "XXXXXX   XXXXXXXXXXXXX X",
    "XXXXXX   XXXXXXXXXXXXX X",
    "X         E            X",
    "XXXXX    XXXXXXXXXX    X",
    "X        XXXXXXXXXXX XXX",
    "XXXXXX   XXXXXXXXXXX XXX",
    "X                      X",
    "XXXXXX   XXXX   XXXXXXXX",
    "XXXXXX   XXXX   XXXXXXXX",
    "XXXXX    XXXX   E      X",
    "X               X      X",
    "XXXXXXX   XXXXXXX  XXXXX",
    "XXXXXX    XXXXXXX  XXXXX",
    "XXXXXXXX    T      XXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add a treasure list
treasures = []

enemies = []

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

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))


pen = Pen()
player = Player()

walls = []

setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left,'Left')
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')
win.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

while True:

    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player Dies!")

    win.update()
