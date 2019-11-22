# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
# gives access to commands in mac like afplay for audio-file play
# import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
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
ball.dx = .3
ball.dy = .3

# Pen -> used to draw the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
# penup hides the initial turtle line-draw
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Helvetica", 24, "normal"))


# Functions
def paddle_a_up():
  if paddle_a.ycor() <= 240:
    y = paddle_a.ycor()
    y += 55
    paddle_a.sety(y)


def paddle_a_down():
  if paddle_a.ycor() >= -240:
    y = paddle_a.ycor()
    y -= 55
    paddle_a.sety(y)


def paddle_b_up():
  if paddle_b.ycor() <= 240:
    y = paddle_b.ycor()
    y += 55
    paddle_b.sety(y)


def paddle_b_down():
  if paddle_b.ycor() >= -240:
    y = paddle_b.ycor()
    y -= 55
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

# Main game loop
while True:
  wn.update()

  # Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # Border checking

  # Top and bottom
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
    # os.system("afplay bounce.wav&")

  elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    # os.system("afplay bounce.wav&")

  # Left and right
  if ball.xcor() > 380:
    score_a += 1
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Helvetica", 24, "normal"))
    ball.goto(0, 0)
    ball.dx *= -1

  elif ball.xcor() < -380:
    score_b += 1
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Helvetica", 24, "normal"))
    ball.goto(0, 0)
    ball.dx *= -1

  # Paddle and ball collisions
  if (ball.xcor() < -340 and ball.xcor < -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
    ball.dx *= -1
      # os.system("afplay bounce.wav&")

  elif (ball.xcor() < 340 and ball.xcor < 350)  and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
    ball.dx *= -1
      # os.system("afplay bounce.wav&")

  # Notes I've learned:
    # AttributeError: '_Screen' object has no attribute 'onkeypress'
    # Python can't recognize keypress, it's onkey() which activates on release
  # Amperstand at the end of a sound file eliminates the stutter when aud occurs, it's aplay in linux
  # For windoes sound manipulaiton ==>
  #import winsound 
  # ...
  # winsound.PlaySound("file1.wav", winsound.SND_ASYNC)