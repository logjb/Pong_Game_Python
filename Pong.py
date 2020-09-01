#pong game

import turtle
#mess with os using calls
#mac
import os
#windows
#import winsound

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800,height=600)

#have you manually update the window
window.tracer(0)

#score
score_one, score_two =0,0

#paddle 1
paddle_one = turtle.Turtle()
#sets speed of animation to maximum possible speed
paddle_one.speed(0)
#give the paddle a shape
paddle_one.shape("square")
#stretch the width by a factor of 5
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
#paddle color
paddle_one.color("white")
#turtles by definition draw a line while they move, we dont want that
paddle_one.penup()
paddle_one.goto(-350,0)



#paddle 2
paddle_two = turtle.Turtle()
#sets speed of animation to maximum possible speed
paddle_two.speed(0)
#give the paddle a shape
paddle_two.shape("square")
#stretch the width by a factor of 5
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
#paddle color
paddle_two.color("white")
#turtles by definition draw a line while they move, we dont want that
paddle_two.penup()
paddle_two.goto(350,0)

#ball
ball = turtle.Turtle()
#sets speed of animation to maximum possible speed
ball.speed(0)
#give the paddle a shape
ball.shape("square")
#stretch the width by a factor of 5
#ball.shapesize(stretch_wid=5, stretch_len=1)
#paddle color
ball.color("white")
#turtles by definition draw a line while they move, we dont want that
ball.penup()
ball.goto(0,0)

ball.dx = 2
ball.dy = -2

# Pen?

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"player A: {score_one} Player B : {score_two}", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_one_up():
    #returns y coordinate
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_down():
    #returns y coordinate
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

def paddle_two_up():
    #returns y coordinate
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

def paddle_two_down():
    #returns y coordinate
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

#listen for keyboard input
window.listen()
window.onkeypress(paddle_one_up, "w")
window.onkeypress(paddle_one_down, "s")
window.onkeypress(paddle_two_up, "Up")
window.onkeypress(paddle_two_down, "Down")

while True:
    window.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound(bounce.wav", winsound.SND_ASYNC)
        #plays sound, & has it do it in its own thread
        #os.system("afplay bounce.wav&")

        # border checking
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write(f"player A: {score_one} Player B : {score_two}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_two += 1
        pen.clear()
        pen.write(f"player A: {score_one} Player B : {score_two}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_two.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
