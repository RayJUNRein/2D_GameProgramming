from pico2d import *
import random

# 스테이지 1 지형 맵 크기 지정 (가로 7166 x 세로 448 pixel)
road_w = 7166

# 적군
class Goblin:
    # 1 pixel = 1cm
    PIXEL_PER_METER = (10.0 / 0.1)
    # 달리기 속도 = 6km/h
    RUN_SPEED_KMPH = 6.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        global width
        self.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin2.png')
        self.x, self.y = random.randint(600, road_w), 300
        self.frame = 0
        self.frame_num = 6
        self.draw_width = 158
        self.draw_height = 141
        self.dir = -1

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * self.draw_width, 0, self.draw_width, self.draw_height, self.x, self.y)

    def get_bb(self):
        return self.x - self.draw_width / 2, self.y - self.draw_height / 2, self.x + self.draw_width / 2, self.y + self.draw_height / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Goblin.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % self.frame_num
        self.x += self.dir * distance
