from pygame import *

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((200, 255, 255))

game = True
finish = False 
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
