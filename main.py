import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []

# creating a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600, height=600)
s.tracer(0)   # turn off auto screen updates

# creating a head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# creating food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.goto(150, 200)

# scoreboard
sb = turtle.Turtle()
sb.penup()
sb.hideturtle()
sb.goto(-250, 250)
sb.write("Score:0   |   Highest Score:0", font=("Arial", 14, "normal"))

# movement functions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# keyboard bindings
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# main game loop
while True:
    s.update()

    # border collision
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # food collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add body
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.penup()
        bodies.append(body)

        sc += 100
        delay -= 0.001

        if sc > hs:
            hs = sc

        sb.clear()
        sb.write("Score:{}   |   Highest Score:{}".format(sc, hs),
                 font=("Arial", 14, "normal"))

    # move body segments
    for i in range(len(bodies)-1, 0, -1):
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        bodies[0].goto(head.xcor(), head.ycor())

    move()

    # body collision
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in bodies:
                segment.hideturtle()
            bodies.clear()

            sc = 0
            delay = 0.1

            sb.clear()
            sb.write("Score:{}   |   Highest Score:{}".format(sc, hs),
                     font=("Arial", 14, "normal"))

    time.sleep(delay)

s.mainloop()
