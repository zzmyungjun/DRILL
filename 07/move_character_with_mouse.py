from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def move_events():
    global x, y
    global direction
    global hx, hy
    if hx != x and hy != y:
        if hx > x:
            direction = 100
            x += 1
            if hy > y:
                y += 1
            elif hy < y:
                y -= 1

        elif hx < x:
            direction = 1
            x -= 1
            if hy > y:
                y += 1
            elif hy < y:
                y -= 1
    elif hx != x and hy == y:
        if hx > x:
            direction = 100
            x += 1
        elif hx < x:
            direction = 1
            x -= 1
    elif hx == x and hy != y:
        if hy > y:
            y += 1
        elif hy < y:
            y -= 1

    pass

open_canvas(KPU_WIDTH,KPU_HEIGHT)

hand = load_image('hand_arrow.png')
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
direction = 1
hide_cursor()
hx, hy = random.randint(0, 1280), random.randint(0, 1024)
hand.draw(hx, hy)

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, direction * 1, 100, 100, x, y)
    if x == hx and y == hy:
        hx, hy = random.randint(0, 1280), random.randint(1, 1024)
    hand.draw(hx, hy)
    update_canvas()
    frame = (frame + 1) % 8

    move_events()


close_canvas()




