from pico2d import *

name = "Font"


class Font:
    def __init__(self):
        self.name = name
        self.image = load_image('Resources\Fonts\Font_Credit.png')
        self.canvas_width, self.canvas_height = get_canvas_width(), get_canvas_height()
        self.x, self.y = 100, 657
        self.frame_x = 0
        self.frame_y = 0
        self.draw_width = 24
        self.draw_height = 25

    def draw(self, frame_time):
        self.image.clip_draw(self.frame_x * self.draw_width, self.frame_y * self.draw_height, self.draw_width, self.draw_height, self.x, self.y)
