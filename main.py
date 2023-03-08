# Maksim, Surain, Elias, Mitch
# SNAKE GAME
# FEATURES = Colour palette for snake, Crowns, Music/sound effects, Game Over Screen, restartable game, high score
# March 7 2023

# import required modules
# YOU NEED TO DOWNLOAD PLAYSOUND ON PIP OR ON YOUR IDE
import turtle
import time
import random
from playsound import playsound
from tkinter import *
from threading import Thread

# window for buttons
root = Tk()
root.geometry('900x700')
root.configure(bg='light blue')
####

# Buttons for colours
colours = []


def green_click():
    global colours
    colours.append('green')
    root.destroy()


def orange_click():
    colours.append('orange')
    root.destroy()


def purple_click():
    colours.append('purple')
    root.destroy()


# Button Creation
x, y = 50, 500

label = Label(root, text="Choose which colour you want your snake to be", bg='light blue', fg='Black',
              font=('Calibri', 30, 'normal'))
label.pack()
label.place(x=x, y=y)
Green = Button(root, text="Green Snake", padx=50, pady=50, command=green_click, bg='green', fg='white')
Green.pack()
Orange = Button(root, text="Orange Snake", padx=50, pady=50, command=orange_click, bg='orange', fg='white')
Orange.pack()
Purple = Button(root, text="Purple Snake", padx=50, pady=50, command=purple_click, bg='purple', fg='white')
Purple.pack()

root.mainloop()


# AUDIO
def game_over_sound():
    playsound(r"snake_death.mp3")


def play_sound():
    playsound(r"snakepickup.mp3")


# CONSTANTS
MAINCOLOUR = colours[0]

delay = 0.1
score = 0
high_score = 0

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
wn = turtle.Screen()

# Window creation for turtle
wn.title("Snake Game")
wn.bgcolor("black")

# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape('square')
head.color(MAINCOLOUR)
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()

food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.shape('square')
game_over_pen.color('white')
game_over_pen.penup()
game_over_pen.hideturtle()


# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y1 = head.ycor()
        head.sety(y1 + 20)
    if head.direction == "down":
        y1 = head.ycor()
        head.sety(y1 - 20)
    if head.direction == "left":
        x1 = head.xcor()
        head.setx(x1 - 20)
    if head.direction == "right":
        x1 = head.xcor()
        head.setx(x1 + 20)


wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []

# Main Gameplay
while True:
    wn.update()
    if score == 0:
        head.color(MAINCOLOUR)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        thread = Thread(target=game_over_sound)
        thread.start()
        game_over_pen.showturtle()
        game_over_pen.write("GAME OVER", align="center", font=("candara", 60, "bold"))
        time.sleep(3)
        game_over_pen.clear()
        game_over_pen.hideturtle()
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = MAINCOLOUR
        shapes = 'square'
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    if head.distance(food) < 20:
        thread = Thread(target=play_sound)
        thread.start()
        x = random.randint(-270, 270)
        y = random.randint(-270, 250)  # y = (-270,250) so apple doesnt spawn an high score turtle
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(MAINCOLOUR)  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 15:
            thread = Thread(target=game_over_sound)
            thread.start()
            game_over_pen.showturtle()
            game_over_pen.write("GAME OVER", align="center", font=("candara", 60, "bold"))
            time.sleep(3)
            game_over_pen.clear()
            game_over_pen.hideturtle()
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = MAINCOLOUR
            shapes = 'square'
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

    if score > 30:
        head.color('white')

    if score > 50:
        head.color('light blue')
    if score > 100:
        head.color('red')
