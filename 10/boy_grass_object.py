from pico2d import *
import random
# Game object class here

class Grass:
    def __init__(self): #생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0

    def update(self):
        self.x += 5 # 속성값을 바꿈으로써 오른쪽으로 이동
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        if random.randint(0, 10) < 5:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(1, 800), 599
        self.frame = 0

    def update(self):
        if self.y <= 60:
            self.y = 60
        else:
            self.y -= random.randint(1, 8)
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()

balls = [Ball() for i in range(20)]

team = [Boy() for i in range(11)]

running = True

de = True

# game main loop code
while running:
    handle_events()

    if de == True:
        delay(5)
        de = False
    # Game logic
    # Grass에 대한 상호작용
    for boy in team:
        boy.update() #소년 상호작용
    for ball in balls:
        ball.update()

    # Game Drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()
    delay(0.05)
# finalization code