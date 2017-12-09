from pico2d import *



# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672

class Font:
    def __init__(self):
        self.name = 'noname'
        self.image = load_image('Resources\ThreeWonders_Miscellaneous1.png')
        self.x, self.y = 100, height - 15
        self.frame_w = 0
        self.frame_h = 0
        self.draw_width = 24
        self.draw_height = 25

    def draw(self, frame_time):
        self.image.clip_draw(self.frame_w * self.draw_width, self.frame_h * self.draw_height, self.draw_width, self.draw_height, self.x, self.y)

