from pico2d import *


# 스테이지 1 보스 Golem Wood 출현하는 맵1
class GWoodBackground:
    image = None

    def __init__(self):
        if GWoodBackground.image == None:
            GWoodBackground.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road33.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = GWoodBackground.image.w
        self.h = GWoodBackground.image.h

    def set_center_object(self, character):
        self.center_object = character

    def draw(self, frame_time):
        GWoodBackground.image.clip_draw_to_origin(self.q31, self.q3b, self.q3w, self.q3h, 0, 0)
        GWoodBackground.image.clip_draw_to_origin(self.q21, self.q2b, self.q2w, self.q2h, 0, self.q3h)
        GWoodBackground.image.clip_draw_to_origin(self.q41, self.q4b, self.q4w, self.q4h, self.q3w, 0)
        GWoodBackground.image.clip_draw_to_origin(self.q11, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)

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


# 스테이지 1 보스 Golem Wood 출현하는 맵2 (애니메이션 적용 예정)
class GWoodRoad:
    speed_data_file = open('Data\Speed_Data.txt', 'r')
    speed_data = json.load(speed_data_file)
    speed_data_file.close()

    # 1 pixel = 1 cm / 10 pixel = 0.1 m
    PIXEL_PER_METER = (10.0 / 0.1)
    # Running Speed = 10 km/h
    RUN_SPEED_KMPH = speed_data['Map']['GWood']['speed']
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = speed_data['Character']['time']
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 12

    image = None

    def __init__(self):
        if GWoodRoad.image == None:
            GWoodRoad.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road_GolemWood.png')
        self.x, self.y = 7166, 40
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = GWoodRoad.image.w
        self.h = GWoodRoad.image.h
        self.window_left = 0
        self.window_bottom = 0
        self.frame = 0
        self.total_frames = 0.0
        self.clip_width, self.clip_height = 16, 35
        self.draw_status = False

    def set_center_object(self, character):
        self.center_object = character

    def draw(self, frame_time):
        if self.draw_status == True:
            GWoodRoad.image.clip_draw(self.frame * self.clip_width, 0, self.clip_width, self.clip_height, self.x - self.window_left, self.y - self.window_bottom)


    def get_bb(self):
        return self.x - self.clip_width / 2 - self.window_left, self.y - self.clip_height / 2 - self.window_bottom, self.x + self.clip_width / 2 - self.window_left, self.y + self.clip_height / 2 - self.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        if self.center_object.x > self.center_object.road.w - 200:
            self.draw_status = True
        else:
            self.draw_status = False
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.h - self.canvas_height)
        self.total_frames += GWoodRoad.FRAMES_PER_ACTION * GWoodRoad.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % GWoodRoad.FRAMES_PER_ACTION