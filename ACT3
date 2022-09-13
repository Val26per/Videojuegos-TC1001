from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

#Cºambio de tablero -Emilio F
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('blue')
    path.color('green')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            option1 = vector(5, 0)
            option2 = vector(-5, 0)
            option3 = vector(0, 5)
            option4 = vector(0, -5)

            #diferencia de pacman y punto en 'x' son mas grande que las de 'y'
            if abs(pacman.x - point.x) > abs(pacman.y - point.y):
                #si la 'x' del punto es mas grande que la 'x' del pacman, se mueve hacia -5 en 'x'
                if pacman.x < point.x:
                    plan = option2
                #si la 'x' del punto es mas chico que la 'x' del pacman, se mueve hacia 5 en 'x'
                elif pacman.x > point.x:
                    plan = option1
                
                course.x = plan.x
                course.y = plan.y
                
                if valid(point + course):
                    point.move(course)
                else:
                    if pacman.y < point.y:
                        plan = option4
                    #si la 'y' del punto es mas chico que la 'y' del pacman, se mueve hacia 5 en 'y'
                    elif pacman.y > point.y:
                        plan = option3

                    
            #diferencia de pacman y punto en 'y' son mas grande que las de 'x'
            elif abs(pacman.x - point.x) < abs(pacman.y - point.y):
                #si la 'y' del punto es mas grande que la 'y' del pacman, se mueve hacia -5 en 'y'
                if pacman.y < point.y:
                    plan = option4
                #si la 'y' del punto es mas chico que la 'y' del pacman, se mueve hacia 5 en 'y'
                elif pacman.y > point.y:
                    plan = option3
                
                course.x = plan.x
                course.y = plan.y
                
                if valid(point + course):
                    point.move(course)
                else:
                    #si la 'x' del punto es mas grande que la 'x' del pacman, se mueve hacia -5 en 'x'
                    if pacman.x < point.x:
                        plan = option2
                    #si la 'x' del punto es mas chico que la 'x' del pacman, se mueve hacia 5 en 'x'
                    elif pacman.x > point.x:
                        plan = option1
                    

            
            #si 'x' en pacman y en el punto son iguales
            elif pacman.x == point.x:
                #si la 'y' de punto es mas grande que la 'y' de pacman
                if pacman.y < point.y:
                    plan = option4
                #si la 'y' de pacman es mas grande que la 'y' de el punto
                elif pacman.y > point.y:
                    plan = option3
                    
            #si 'y' en pacman y en el punto son iguales    
            elif pacman.y == point.y:
                #si la 'x' del punto es mas grande que la 'x' de pacman
                if pacman.x < point.x:
                    plan = option2
                #si la 'x' de pacman es mas grande que la 'x' del punto
                elif pacman.x > point.x:
                    plan = option1
                    
            course.x = plan.x
            course.y = plan.y

        up()
        
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 5:
            return

    ontimer(move, 50)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
