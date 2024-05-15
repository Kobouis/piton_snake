from pygame import *

# Размеры экрана

width = 600
height = 600

window = display.set_mode((width, height))
display.set_caption('Python snake')

clock = time.Clock()

play = True
while play:
    for e in event.get():
        if e.type == QUIT:
            play = False
    window.fill((255,0,230))
    display.update()
    clock.tick(60)

