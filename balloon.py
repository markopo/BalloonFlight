from fileinput import filename

import pgzrun
from random import randint

from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600

bird_up = True
up = False
game_over = False
sum = 0
no_updates = 0
sums = []

balloon = Actor ("balloon")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)

tree = Actor("tree")
tree.pos = randint (800, 1600) , 450

house = Actor("house")
house.pos = randint(800, 1600), 460

def draw():
    screen.blit("background", (0, 0))

    if not game_over:
        balloon.draw()
        bird.draw()
        tree.draw()
        house.draw()
    else:
        show_record()

def update():
    global game_over, sum, no_updates

    if not up:
        balloon.y += 1

    if bird.x > 0:
        bird.x -= 4
        if no_updates == 5:
            flap()
            no_updates = 0
        else:
            no_updates += 1
    else:
        bird.x = randint(800, 1600)
        bird.y = randint(10, 200)
        sum += 1
        no_updates = 0


    if house.right > 0:
        house.x -= 2
    else:
        house.x = randint(800, 1600)
        sum += 1

    if tree.right > 0:
        tree.x -= 2

    else:
        tree.x = randint(800, 1600)
        sum += 1

    if balloon.collidepoint(bird.x, bird.y) or \
       balloon.collidepoint(house.x, house.y) or \
       balloon.collidepoint(tree.x, tree.y):
       game_over = True
       update_record()



def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

def update_record():
    global sum, sums
    file_name = "Record.txt"
    sums = []
    with open(file_name, "r") as file:
        row = file.readline()
        record = row.split()
        for r in record:
            if sum > int(r):
                sums.append(str(sum) + " ")
                sum = int(r)
            else:
                sums.append(str(r) + " ")

    with open(file_name, "w") as f:
        for record in sums:
            f.write(record)

def show_record():
    screen.draw.text("RECORD", (350, 150), color="black")
    y = 175
    position = 1
    for record in sums:
        screen.draw.text(str(position) + ". " + record, (350, y), color="black")
        y += 25
        position += 1

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True


pgzrun.go()
