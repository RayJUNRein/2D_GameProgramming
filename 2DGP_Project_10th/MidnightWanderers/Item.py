from pico2d import *
import random


name = "Font"


speed_data_file = open('Data\Speed_Data.txt', 'r')
speed_data = json.load(speed_data_file)
speed_data_file.close()

item_data_file = open('Data\Item_Data.txt', 'r')
item_data = json.load(item_data_file)
item_data_file.close()


# 스테이지 1 지형 맵 크기 지정 (가로 7166 x 세로 448 pixel)
road_w = 7166


class Card:
    TIME_PER_ACTION = speed_data['Item']['Card']['time']
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = item_data['Card']['frames_per_action']

    image = None

    def __init__(self):
        self.name = name
        self.x, self.y = random.randint(500, road_w), 300
        self.canvas_width, self.canvas_height = get_canvas_width(), get_canvas_height()
        self.frame_x, self.frame_y = random.randint(0, 3), 0
        self.total_frames = 0.0
        self.clip_width, self.clip_height = 0, 0
        if Card.image == None:
            Card.image = load_image('Resources\Items\ThreeWonders_Items_Card.png')

    def set_road(self, road):
        self.road = road

    def draw(self, frame_time):
        Card.image.clip_draw(self.frame_x * self.clip_width, self.frame_y * self.clip_height, self.clip_width, self.clip_height, self.x - self.road.window_left, self.y - self.road.window_bottom)

    def get_bb(self):
        return self.x - self.clip_width / 2 - self.road.window_left, self.y - self.clip_height / 2 - self.road.window_bottom, self.x + self.clip_width / 2 - self.road.window_left, self.y + self.clip_height / 2 - self.road.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        self.clip_width, self.clip_height = item_data['Card']['clip_width'], item_data['Card']['clip_height']
        self.total_frames += Card.FRAMES_PER_ACTION * Card.ACTION_PER_TIME * frame_time
        self.frame_y = int(self.total_frames) % Card.FRAMES_PER_ACTION

    def create_cards(self):
        cards = []

        for name in item_data:
            card = Card()
            card.name = name
            card.frame_h = item_data[name]['h']
            card.x = item_data[name]['x']
            cards.append(card)

        return cards


class Bound:
    TIME_PER_ACTION = speed_data['Item']['Bound']['time']
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = item_data['Bound']['frames_per_action']

    image = None

    def __init__(self):
        self.name = name
        self.x, self.y = random.randint(500, road_w), 300
        self.canvas_width, self.canvas_height = get_canvas_width(), get_canvas_height()
        self.frame = 0
        self.total_frames = 0.0
        self.clip_width, self.clip_height = 0, 0
        if Bound.image == None:
            Bound.image = load_image('Resources\Items\ThreeWonders_Items_Bound.png')

    def set_road(self, road):
        self.road = road

    def draw(self, frame_time):
        Bound.image.clip_draw(self.frame * self.clip_width, 0, self.clip_width, self.clip_height, self.x - self.road.window_left, self.y - self.road.window_bottom)

    def get_bb(self):
        return self.x - self.clip_width / 2 - self.road.window_left, self.y - self.clip_height / 2 - self.road.window_bottom, self.x + self.clip_width / 2 - self.road.window_left, self.y + self.clip_height / 2 - self.road.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        self.clip_width, self.clip_height = item_data['Bound']['clip_width'], item_data['Bound']['clip_height']
        self.total_frames += Bound.FRAMES_PER_ACTION * Bound.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % Bound.FRAMES_PER_ACTION
