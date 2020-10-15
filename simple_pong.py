# Multi player game where a ball bounces back and forth
# Players have to stop the ball from crossing the boundary
# If unable opponent gets points

import turtle
import winsound


win=turtle.Screen()
win.title("Classic Pong")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

# Scores
score_a = 0
score_b = 0


#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
#ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.2
ball.dy=0.2

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",20,"normal"))


#Function to move the paddle
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

#Main Game Loop
while True:
    win.update()

    # Move the Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border Checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))
        winsound.PlaySound("game_b.wav", winsound.SND_ASYNC)


    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
        winsound.PlaySound("game_a.wav", winsound.SND_ASYNC)


    # Paddle and ball Collision
    if (340 < ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 48) and (ball.ycor() > paddle_b.ycor() - 48):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("grunt.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 48) and (ball.ycor() > paddle_a.ycor() - 48):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("grunt.wav", winsound.SND_ASYNC)

    if paddle_b.ycor()>250:
        paddle_b.sety(250)

    if paddle_b.ycor()<-250:
        paddle_b.sety(-250)

    if paddle_a.ycor()>250:
        paddle_a.sety(250)

    if paddle_a.ycor()<-250:
        paddle_a.sety(-250)