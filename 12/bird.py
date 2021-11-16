import game_framework
from pico2d import *
from random import randint
import game_world

# 비둘기의 실제 크기는 33cm 정도 되고 시속 30km 정도 된다.
# 10 pixel 당 33cm의 크기로 설정하였다.
# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.33)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
SPACE = range(1)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    def enter(bird, event):
        pass

    def exit(bird, event):
        if event == SPACE:
            pass


    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)


class RunState:

    def enter(bird, event):
        if bird.dir == 1:
            bird.velocity += RUN_SPEED_PPS
        else:
            bird.velocity -= RUN_SPEED_PPS

    def exit(bird, event):
        pass

    def do(bird):
        #boy.frame = (boy.frame + 1) % 8
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)
        if bird.x > 1500:
            bird.dir = -1
        elif bird.x < 100:
            bird.dir = 1

    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)





next_state_table = {
    IdleState: {SPACE: RunState},
    RunState: {SPACE: RunState},
}

class Bird:

    def __init__(self):
        self.x, self.y = randint(10,1000), 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 0
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0


    # def fire_ball(self):
    #     ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
    #     game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #fill here


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

