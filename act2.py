from turtle import *
import random
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ["yellow","pink","purple","light blue","green"]
cb = random.choice(colors)
cf = random.choice(colors)
places = ['left', 'right', 'up', 'down']
while cb == cf:
    cf = random.choice(colors)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def dentro(food):
    return -200 < food.x < 190 and -200 < food.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        for i in range (1):
            square(head.x, head.y, 9,'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        ##food.goto(food.x, food.y)
    else:
        snake.pop(0)
        
    pos = random.choice(places)
    if not dentro(food):
        food.x = randrange(-15, 15) * 10 
        food.y = randrange(-15, 15) * 10
    elif pos == 'left':
        food.x -=10
    elif pos == 'right':
        food.x +=10
    elif pos == 'up':
        food.y += 10
    else:
        food.y -= 10
    
    clear()
            
             
    for body in snake:
        square(body.x, body.y, 9,cb)

    ##square(food.x, food.y, 9, 'green')
    square(food.x, food.y, 9,cf)
    
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
