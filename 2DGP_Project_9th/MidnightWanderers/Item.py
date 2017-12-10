from pico2d import *
import random


name = "Font"


speed_data_file = open('Data\Speed_Data.txt', 'r')
speed_data = json.load(speed_data_file)
speed_data_file.close()

card_data_file = open('Data\Card_Data.txt', 'r')
card_data = json.load(card_data_file)
card_data_file.close()


# 스테이지 1 지형 맵 크기 지정 (가로 7166 x 세로 448 pixel)
road_w = 7166

class Card:
    TIME_PER_ACTION = speed_data['Item']['Card']['time']
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = card_data['Card']['frames_per_action']

    def __init__(self):
        self.name = name
        self.image = load_image('Resources\Items\ThreeWonders_Items_Card.png')
        self.x, self.y = random.randint(200, road_w), 300
        self.canvas_width, self.canvas_height = get_canvas_width(), get_canvas_height()
        self.frame_x, self.frame_y = random.randint(0, 3), 0
        self.total_frames = 0.0
        self.clip_width, self.clip_height = 0, 0

    def set_road(self, road):
        self.road = road

    def draw(self, frame_time):
        self.image.clip_draw(self.frame_x * self.clip_width, self.frame_y * self.clip_height, self.clip_width, self.clip_height, self.x - self.road.window_left, self.y - self.road.window_bottom)

    def get_bb(self):
        return self.x - self.clip_width / 2 - self.road.window_left, self.y - self.clip_height / 2 - self.road.window_bottom, self.x + self.clip_width / 2 - self.road.window_left, self.y + self.clip_height / 2 - self.road.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        self.clip_width, self.clip_height = card_data['Card']['clip_width'], card_data['Card']['clip_height']
        self.total_frames += Card.FRAMES_PER_ACTION * Card.ACTION_PER_TIME * frame_time
        self.frame_y = int(self.total_frames) % Card.FRAMES_PER_ACTION

    def create_cards(self):
        cards = []

        for name in card_data:
            card = Card()
            card.name = name
            card.frame_h = card_data[name]['h']
            card.x = card_data[name]['x']
            cards.append(card)

        return cards