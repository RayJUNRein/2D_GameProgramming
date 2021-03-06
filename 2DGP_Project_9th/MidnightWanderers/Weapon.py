from pico2d import *


# 주인공 무기
class Weapon:
    def __init__(self):
        self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightArrow1.png')
        self.x, self.y = 0, 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = 0
        self.total_frames = 0.0
        self.dir_x = 0
        self.dir_y = 0
        self.clip_width = 93
        self.clip_height = 21

    def set_character(self, character):
        self.character = character

        if self.character.state == self.character.LEFT_SHOT_STAND:
            self.dir_x = -1
            self.x, self.y = self.character.x - self.clip_width, self.character.y - self.clip_height + 20
        elif self.character.state == self.character.LEFT_SHOT_SIT:
            self.dir_x = -1
            self.x, self.y = self.character.x - self.clip_width, self.character.y - self.clip_height + 5
        elif self.character.state == self.character.RIGHT_SHOT_STAND:
            self.dir_x = 1
            self.x, self.y = self.character.x + self.clip_width, self.character.y - self.clip_height + 20
        elif self.character.state == self.character.RIGHT_SHOT_SIT:
            self.dir_x = 1
            self.x, self.y = self.character.x + self.clip_width, self.character.y - self.clip_height + 5
        elif self.character.state == self.character.LEFT_SHOT_LOOKUP or self.character.state == self.character.RIGHT_SHOT_LOOKUP:
            self.dir_y = 1
            self.x, self.y = self.character.x, self.character.y + self.character.clip_height / 2

    def set_road(self, road):
        self.road = road

    def update(self, frame_time):
        pass

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * self.clip_width, 0, self.clip_width, self.clip_height, self.x - self.road.window_left, self.y - self.road.window_bottom)

    def get_bb(self):
        return self.x - self.clip_width / 2 - self.road.window_left, self.y - self.clip_height / 2 - self.road.window_bottom, self.x + self.clip_width / 2 - self.road.window_left, self.y + self.clip_height / 2 - self.road.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Arrow(Weapon):
    speed_data_file = open('Data\Speed_Data.txt', 'r')
    speed_data = json.load(speed_data_file)
    speed_data_file.close()

    # 1 pixel = 1cm
    PIXEL_PER_METER = (10.0 / 0.1)
    # 날아가는 속도 = 25km/h
    RUN_SPEED_KMPH = speed_data['Weapon']['Arrow']['speed']
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = speed_data['Weapon']['Arrow']['time']
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    def update(self, frame_time):
        distance = Arrow.RUN_SPEED_PPS * frame_time
        self.x += self.dir_x * distance
        self.y += self.dir_y * distance

        self.total_frames += Arrow.FRAMES_PER_ACTION * Arrow.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % Arrow.FRAMES_PER_ACTION

        if self.dir_x == -1:
            self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftArrow1.png')
            self.clip_width = 93
            self.clip_height = 21

        elif self.dir_x == 1:
            self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightArrow1.png')
            self.clip_width = 93
            self.clip_height = 21

        elif self.dir_y == 1:
            self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_UpArrow1.png')
            self.clip_width = 21
            self.clip_height = 93
