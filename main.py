# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("dark green")
screen.setup(width=600,height=600)
screen.tracer(0)

#making snakes head
head = turtle.Turtle()
head.shape("square")
head.color("gold")
head.penup()
head.goto(0,0)
head.direction = "Stop"


#making score post
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
screen_size = screen.window_height() /2
y = screen_size * 0.8
pen.goto(0,y)
pen.write("Score : 0 High Score : 0", align="center",font=("candara", 24, "bold"))

#making snakes food
best_food = turtle.Turtle()
best_food.hideturtle()
def make_bonus():

	best_food.penup()
	best_food.color("red")
	best_food.shapesize(0.5,0.5)
	best_food.shape("circle")
	best_food.goto(x=random.randint(-200,200), y = random.randint(-200,200))
	best_food.hideturtle()
	best_food.showturtle()
	best_food.speed(0)
	screen.ontimer(make_bonus,2500)

make_bonus()

# assigning key directions
def group():
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
		y = head.ycor()
		head.sety(y+20)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y-20)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x-20)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x+20)


screen.listen()
screen.onkeypress(group, "Up")
screen.onkeypress(godown, "Down")
screen.onkeypress(goleft, "Left")
screen.onkeypress(goright, "Right")

segments = []

# Main Gameplay
while True:
	screen.update()
	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))


	if head.distance(best_food) < 15:
		x = random.randint(-200, 200)
		y = random.randint(-200, 200)
		best_food.goto(x, y)
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("gold") # tail colour
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("candara", 24, "bold"))

	# Checking for head collisions with body segments
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	move()
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			for segment in segments:
				segment.goto(1000, 1000)
			segments.clear()

			score = 0
			delay = 0.1
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(
				score, high_score), align="center", font=("candara", 24, "bold"))
	time.sleep(delay)

screen.mainloop()
