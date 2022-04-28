import turtle
import time
import random

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#Player 1
p_left = turtle.Turtle()
p_left.speed(0)
p_left.shape("square")
p_left.shapesize(stretch_len=1, stretch_wid=5)
p_left.color("white")
p_left.penup()
p_left.goto(-350, 0)


#Player 2
p_right = turtle.Turtle()
p_right.speed(0)
p_right.shape("square")
p_right.shapesize(stretch_len=1, stretch_wid=5)
p_right.color("white")
p_right.penup()
p_right.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
(ball.dx, ball.dy) =(0.05, 0.05)


#Score
score_left = 0
score_right = 0
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.goto(0, 250)
text.write("Player 1: {}       Player 2: {}".format(score_left, score_right), align = "center", font = ("Verdana", 24, "bold"))
text.hideturtle()


def p_left_up():
    y = p_left.ycor()
    y += 20
    p_left.sety(y)

def p_left_down():
    y = p_left.ycor()
    y -= 20
    p_left.sety(y)

def p_right_up():
    y = p_right.ycor()
    y += 20
    p_right.sety(y)

def p_right_down():
    y = p_right.ycor()
    y -= 20
    p_right.sety(y)

def quit_game():
    time.sleep(0.5)
    turtle.bye()


pause = False
def pause_unpause():
    global pause

    if pause:
        ball.dx = random.choice([0.05, -0.05])
        ball.dy = random.choice([0.05, -0.05])
        pause = False
        
    else:

        ball.dx = 0
        ball.dy = 0
        pause = True
    print(pause)

window.listen()
window.onkeypress(p_left_up, 'w')
window.onkeypress(p_left_down, 's')
window.onkeypress(p_right_up, 'Up')
window.onkeypress(p_right_down, 'Down')
window.onkeypress(quit_game, 'q')
window.onkeypress(pause_unpause, 'p')

print(p_right.turtlesize())
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Borders
    if ball.ycor() >= 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        text.clear()
        text.write("Player 1: {}       Player 2: {}".format(score_left, score_right), align = "center", font = ("Verdana", 24, "bold"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        text.clear()
        text.write("Player 1: {}       Player 2: {}".format(score_left, score_right), align = "center", font = ("Verdana", 24, "bold"))


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < p_right.ycor() + 40 and ball.ycor() > p_right.ycor() - 40):
        ball.dx *= -1
        
    if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < p_left.ycor() + 40 and ball.ycor() > p_left.ycor() - 40):
        ball.dx *= -1
        
    