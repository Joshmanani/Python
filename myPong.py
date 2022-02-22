import turtle
import winsound
import time
window = turtle.Screen()
window.title('pong by manani from tokyotech')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0) # stops windoow from automatically updating

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # prevents paddle from drawing line while moving
paddle_a.goto(-345, 0)

# paddle b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # prevents paddle from drawing line while moving
paddle_b.goto(345, 0)


# ball

ball= turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup() # prevents paddle from drawing line while moving
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = 1.5

#pen to draw score
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player 1: 0  Player 2: 0', align='center', font=('Courier', 24, 'normal'))


# score
score_1 = 0
score_2 = 0

# Function to move ball

def paddl_a_up():
    y= paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddl_a_down():
    y= paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddl_b_up():
    y= paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddl_b_down():
    y= paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

window.listen()
window.onkeypress(paddl_a_up, 'w')
window.onkeypress(paddl_a_down, 's')
window.onkeypress(paddl_b_up, 'Up')
window.onkeypress(paddl_b_down, 'Down')

# Main game loop
while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.color('Purple')
        ball.dy *= -1 
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.color('red')
        ball.dy *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC) 
    if ball.xcor() > 390 :
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        time.sleep(0.5)
        ball.color('green')
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1 
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)
        
        ball.goto(0,0)
        time.sleep(0.5)
        ball.color('yellow')
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))