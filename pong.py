

import turtle
import winsound
#import os

wn = turtle.Screen()
wn.title(" Jirikuv Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops windows from updating, it speeds up our games.
#wn.exitonclick()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # turtle is modul name ,Turtle is class name.
paddle_a.speed(0) #sets to maximum possible speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #by default size is 20pixels x 20pixels
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # everytime the ball moves it moves by two pixels up (in total diagonaly
ball.dy = 0.2 # everytime the ball moves it moves by two pixels down (in total diagonaly)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


def players():

    pen.write("Jiri: 0  Paja: 0", align="center", font=("Courier", 24, "normal"))
    #pen.write(turtle.textinput("Player A", "Type Player A Name"), align="left", font=("Courier", 24, "normal"))
    #pen.write(turtle.textinput("Player B", "Type Player B Name"), align="right", font=("Courier", 24, "normal"))


players()

# Functions

def paddle_a_up():
    y = paddle_a.ycor() #current Y coordination(position) paddle_a is name of the object and ycor() is turtle module.
    y += 20 #add 20 pixels to the y coordination
    paddle_a.sety(y) #set y to the new y (calculation of the y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
def quit_game():
    pen.clear()
    #turtle.goto(0, 0)
    pen.write("Do you want to exit game? Click on the screen!",align="center", font=("Courier", 20, "normal"))
    wn.exitonclick()

# Keyboard bindings
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #when user press the W, call the function paddle_a_up().
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(quit_game, "q")
# Main game loop
while True:
    wn.update() #everytime the loops runs it update the screen.

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #in first loop it goes 0(=current koordination)+2 pixels, next loop again +2pixels etc.
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290: #290 because the ball itself has 20x20pixels so 300-10pixels of the size of the ball.
        ball.sety(290) #set back to 290
        ball.dy *= -1 #-1 reverse direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("aplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("aplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Jiri: {} Paja: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("Scores.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Jiri: {} Paja: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("Scores.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("aplay bounce.wav&")

    elif ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("aplay bounce.wav&")
