from pico2d import *


name = "Credit"


class Credit:
    image = None

    def __init__(self):
        self.canvas_width, self.canvas_height = get_canvas_width(), get_canvas_height()
        self.x, self.y = 0, 0
        self.frame_x = 0
        self.frame_y = 0
        self.draw_width = 24
        self.draw_height = 25
        self.credit_num = 0
        if Credit.image == None:
            Credit.image = load_image('Resources\Fonts\Font_Credit.png')

    def update(self, frame_time, credit_num):
        self.credit_num = credit_num
        self.credit_num = clamp(0, self.credit_num, 9)

    def draw(self, frame_time):
        font_data_file = open('Data\Font_Data.txt', 'r')
        font_data = json.load(font_data_file)
        font_data_file.close()

        self.draw_width = font_data['Credit']['C']['w']
        self.draw_height = font_data['Credit']['C']['h']
        self.frame_x = font_data['Credit']['C']['x'] * self.draw_width
        self.frame_y = font_data['Credit']['C']['y'] * self.draw_height
        Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 275, 10)

        self.draw_width = font_data['Credit']['R']['w']
        self.draw_height = font_data['Credit']['R']['h']
        self.frame_x = font_data['Credit']['R']['x'] * self.draw_width
        self.frame_y = font_data['Credit']['R']['y'] * self.draw_height
        Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 250, 10)

        self.draw_width = font_data['Credit']['E']['w']
        self.draw_height = font_data['Credit']['E']['h']
        self.frame_x = font_data['Credit']['E']['x'] * self.draw_width
        self.frame_y = font_data['Credit']['E']['y'] * self.draw_height
        Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 225, 10)

        self.draw_width = font_data['Credit']['D']['w']
        self.draw_height = font_data['Credit']['D']['h']
        self.frame_x = font_data['Credit']['D']['x'] * self.draw_width
        self.frame_y = font_data['Credit']['D']['y'] * self.draw_height
        Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 200, 10)

        self.draw_width = font_data['Credit']['I']['w']
        self.draw_height = font_data['Credit']['I']['h']
        self.frame_x = font_data['Credit']['I']['x'] * self.draw_width
        self.frame_y = font_data['Credit']['I']['y'] * self.draw_height
        Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 175, 10)

        self.draw_width = font_data['Credit']['T']['w']
        self.draw_height = font_data['Credit']['T']['h']
        self.frame_x = font_data['Credit']['T']['x'] * self.draw_width
        self.frame_y = font_data['Credit']['T']['y'] * self.draw_height
        Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 150, 10)

        if self.credit_num == 0:
            self.draw_width = font_data['Credit']['0']['w']
            self.draw_height = font_data['Credit']['0']['h']
            self.frame_x = font_data['Credit']['0']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['0']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 1:
            self.draw_width = font_data['Credit']['1']['w']
            self.draw_height = font_data['Credit']['1']['h']
            self.frame_x = font_data['Credit']['1']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['1']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 2:
            self.draw_width = font_data['Credit']['2']['w']
            self.draw_height = font_data['Credit']['2']['h']
            self.frame_x = font_data['Credit']['2']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['2']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 3:
            self.draw_width = font_data['Credit']['3']['w']
            self.draw_height = font_data['Credit']['3']['h']
            self.frame_x = font_data['Credit']['3']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['3']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 4:
            self.draw_width = font_data['Credit']['4']['w']
            self.draw_height = font_data['Credit']['4']['h']
            self.frame_x = font_data['Credit']['4']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['4']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 5:
            self.draw_width = font_data['Credit']['5']['w']
            self.draw_height = font_data['Credit']['5']['h']
            self.frame_x = font_data['Credit']['5']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['5']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 6:
            self.draw_width = font_data['Credit']['6']['w']
            self.draw_height = font_data['Credit']['6']['h']
            self.frame_x = font_data['Credit']['6']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['6']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 7:
            self.draw_width = font_data['Credit']['7']['w']
            self.draw_height = font_data['Credit']['7']['h']
            self.frame_x = font_data['Credit']['7']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['7']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 8:
            self.draw_width = font_data['Credit']['8']['w']
            self.draw_height = font_data['Credit']['8']['h']
            self.frame_x = font_data['Credit']['8']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['8']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)

        elif self.credit_num == 9:
            self.draw_width = font_data['Credit']['9']['w']
            self.draw_height = font_data['Credit']['9']['h']
            self.frame_x = font_data['Credit']['9']['x'] * self.draw_width
            self.frame_y = font_data['Credit']['9']['y'] * self.draw_height
            Credit.image.clip_draw(self.frame_x, self.frame_y, self.draw_width, self.draw_height, self.canvas_width - 100, 10)
