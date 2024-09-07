import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Catch the Target Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the target turtle
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)

# Create obstacles
obstacles = []
colors = ["black", "brown", "darkgray"]
for _ in range(5):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color(random.choice(colors))
    obstacle.penup()
    obstacle.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    obstacle.goto(x, y)
    obstacles.append(obstacle)

# Create a turtle for displaying messages
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.color("black")

# Function to display game over message
def display_game_over():
    message_turtle.clear()
    message_turtle.goto(0, 0)
    message_turtle.write("Game Over!", align="center", font=("Arial", 24, "bold"))
    wn.update()
    turtle.done()

# Move the target to a random position
def move_target():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    target.goto(x, y)

move_target()

# Move player up
def move_up():
    player.setheading(90)
    y = player.ycor()
    y += 20
    player.sety(y)

# Move player down
def move_down():
    player.setheading(270)
    y = player.ycor()
    y -= 20
    player.sety(y)

# Move player left
def move_left():
    player.setheading(180)
    x = player.xcor()
    x -= 20
    player.setx(x)

# Move player right
def move_right():
    player.setheading(0)
    x = player.xcor()
    x += 20
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Check for collision with the target
def check_collision():
    if player.distance(target) < 20:
        move_target()

# Check for collision with obstacles
def check_obstacle_collision():
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            display_game_over()
            break

# Main game loop
while True:
    wn.update()
    check_collision()
    check_obstacle_collision()
