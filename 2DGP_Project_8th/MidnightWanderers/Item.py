from pico2d import *
import random

# 스테이지 1 지형 맵 크기 지정 (가로 7166 x 세로 448 pixel)
road_w = 7166

class Card:
    def __init__(self):
        self.name = 'noname'
        self.image = load_image('Resources\Items\ThreeWonders_Items_Card.png')
        self.x, self.y = random.randint(200, road_w), 300
        self.frame_num = 4
        self.frame_w = 0
        self.frame_h = 0
        self.draw_width = 90
        self.draw_height = 160

    def draw(self, frame_time):
        self.image.clip_draw(self.frame_w * self.draw_width, self.frame_h * self.draw_height, self.draw_width, self.draw_height, self.x, self.y)

    def get_bb(self):
        return self.x - self.draw_width / 2, self.y - self.draw_height / 2 + 30, self.x + self.draw_width / 2, self.y + self.draw_height / 2 - 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        self.frame_h = (self.frame_h + 1) % self.frame_num
