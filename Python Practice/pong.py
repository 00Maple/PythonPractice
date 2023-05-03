import turtle as t
playerAscore=0
playerBscore=0

# Create a window and call a screen
window=t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)

# Left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

# Right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

# Ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ballxdirection=0.2
ballydirection=0.2

# Scorecard update pen
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('arial',24,'normal'))

# moving the left paddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

# moving the right paddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

# Control keys
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddleup, 'Down')

while True:
    window.update()
    
    # moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballxdirection)
    
    # Game border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        #ball_dx = ball_dx * -1
        playerAscore = playerAscore +1
        pen.clear
        pen.write("Player A: {}                     Player B: {}".format(playerAscore,playerBscore),align="center",font=('monaco',24,'normal'))
        os.system("afplay wallhit.wav&")
        
    if (ball.xcor()) < -390: 
        ball.goto(0,0)
        #ball_dx = ball_dx * -1
        playerBscore = playerBscore +1
        pen.clear
        pen.write("Player A: {}                     Player B: {}".format(playerAscore,playerBscore),align="center",font=('monaco',24,'normal'))
        os.system("afplay wallhit.wav&")

    # Paddle collision
    if (ball.xcor() >340) and (ball.xcor()< 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        #ball_dx = ball_dx * -1 
        os.system("afplay paddle.wav&")
    
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() < leftpaddle.ycor() - 40):
        ball.setx(-340)
        #ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")