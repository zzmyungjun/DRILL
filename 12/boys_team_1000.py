import sys
import random
import game_framework
from pico2d import *

# 새의 실제 크기는 33cm 정도 되고 시속 30km 정도 된다.
# 10 pixel 당 33cm의 크기로 설정하였다.
PIXEL_PER_METER = (10.0 / 0.33)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 1400), 90
        self.frame = 0
        self.dir = 0
        self.velocity = 0
        self.image = load_image('bird100x100x14.png')


    def update(self):
        if self.dir == 1:
            self.velocity += RUN_SPEED_PPS
        else:
            self.velocity -= RUN_SPEED_PPS

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)
        if self.x > 1500:
            self.dir = -1
        elif self.x < 100:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

team = [Bird() for i in range(10)]

running = True;
while running:
    handle_events()

    for bird in team:
        bird.update()

    clear_canvas()
    for bird in team:
        bird.draw()
    update_canvas()

    delay(0.05)

close_canvas()
