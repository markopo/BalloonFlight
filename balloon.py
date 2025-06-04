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



def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

def update_record():
    pass

def show_record():
    pass

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True


pgzrun.go()
