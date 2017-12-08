from pico2d import *


# 배경 이미지
class Background:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Background\MidnightWanderers_Levels_1_Background2.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.q11, self.q1b, self.q1w, self.q1h = 0, 0, 0, 0
        self.q21, self.q2b, self.q2w, self.q2h = 0, 0, 0, 0
        self.q31, self.q3b, self.q3w, self.q3h = 0, 0, 0, 0
        self.q41, self.q4b, self.q4w, self.q4h = 0, 0, 0, 0

    def set_center_object(self, character):
        self.center_object = character

    def draw(self, frame_time):
        self.image.clip_draw_to_origin(self.q31, self.q3b, self.q3w, self.q3h, 0, 0)
        self.image.clip_draw_to_origin(self.q21, self.q2b, self.q2w, self.q2h, 0, self.q3h)
        self.image.clip_draw_to_origin(self.q41, self.q4b, self.q4w, self.q4h, self.q3w, 0)
        self.image.clip_draw_to_origin(self.q11, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)

    def update(self, frame_time):
        #       quadrant 3
        self.q31 = (int(self.center_object.x) - self.canvas_width // 2) % self.w
        self.q3b = (int(self.center_object.y) - self.canvas_height // 2) % self.h
        self.q3w = clamp(0, self.w - self.q31, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        #       quadrant 2
        self.q21 = self.q31
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.canvas_height - self.q3h

        #       quadrant 4
        self.q41 = 0
        self.q4b = self.q3b
        self.q4w = self.canvas_width - self.q3w
        self.q4h = self.q3h

        #       quadrant 1
        self.q11 = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h
