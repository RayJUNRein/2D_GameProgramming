from pico2d import *
import random


# 적군
class Goblin:
    speed_data_file = open('Data\Speed_Data.txt', 'r')
    speed_data = json.load(speed_data_file)
    speed_data_file.close()

    # 1 pixel = 1cm
    PIXEL_PER_METER = (10.0 / 0.1)
    # 달리기 속도 = 6km/h
    RUN_SPEED_KMPH = speed_data['Enemy']['Goblin']['speed']
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = speed_data['Enemy']['Goblin']['time']
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2

    def __init__(self):
        self.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_LeftGoblin1.png')
        self.x, self.y = random.randint(600, 7000), 300
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = 0
        self.total_frames = 0.0
        self.dir_x = 0
        self.dir_y = 0
        self.clip_width = 158
        self.clip_height = 141

    def set_road(self, road):
        self.road = road

    def set_character(self, character):
        self.character = character

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * self.clip_width, 0, self.clip_width, self.clip_height, self.x - self.road.window_left, self.y - self.road.window_bottom)

    def get_bb(self):
        return self.x - self.clip_width / 2 - self.road.window_left, self.y - self.clip_height / 2 - self.road.window_bottom, self.x + self.clip_width / 2 - self.road.window_left, self.y + self.clip_height / 2 - self.road.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        enemy_data_file = open('Data\Enemy_Data.txt', 'r')
        enemy_data = json.load(enemy_data_file)
        enemy_data_file.close()

        distance = Goblin.RUN_SPEED_PPS * frame_time
        self.x += self.dir_x * distance
        self.y += self.dir_y * distance

        if self.character.x < self.x:
            self.dir_x = -1
            self.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_LeftGoblin2.png')
        else:
            if self.character.x - self.x < 400:
                self.dir_x = 1
                self.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_RightGoblin2.png')
