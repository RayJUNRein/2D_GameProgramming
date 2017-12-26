from pico2d import *


class Road:
    # 1 pixel = 1 cm / 10 pixel = 0.1 m
    PIXEL_PER_METER = (10.0 / 0.1)

    image = None

    def __init__(self):
        if Road.image == None:
            Road.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = Road.image.w
        self.h = Road.image.h
        self.bb_x_start = 0
        self.bb_x_width = 0
        self.bb_y = 0
        self.bb_dir = 0
        self.bb_move_x = 20
        self.bb_move_y = 5
        self.window_left = 0
        self.window_bottom = 0

    def set_center_object(self, character):
        self.center_object = character

    def draw(self):
        Road.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)

    def get_bb(self, object):
        road_data_file = open('Data\Road_Data.txt', 'r')
        road_data = json.load(road_data_file)
        road_data_file.close()

        if 0 < object.x and object.x < 1240:
            self.bb_x_start = road_data['Flat']['0']['x']['start']
            self.bb_x_width = road_data['Flat']['0']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['0']['y']
            self.bb_dir = 0

        elif 1240 < object.x and object.x < 1260:
            self.bb_x_start = road_data['Down']['1']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y']
            self.bb_dir = -1
        elif 1260 < object.x and object.x < 1280:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 1
        elif 1280 < object.x and object.x < 1300:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 2
        elif 1300 < object.x and object.x < 1320:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 3
        elif 1320 < object.x and object.x < 1340:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 4
        elif 1340 < object.x and object.x < 1360:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 5
        elif 1360 < object.x and object.x < 1380:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 6
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 6
        elif 1380 < object.x and object.x < 1400:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 7
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 7
        elif 1400 < object.x and object.x < 1430:
            self.bb_x_start = road_data['Down']['1']['x']['start'] + self.bb_move_x * 8
            self.bb_x_width = self.bb_move_x + 10
            self.bb_y = road_data['Down']['1']['y'] - self.bb_move_y * 8
            self.bb_dir = -1

        elif 1430 < object.x and object.x < 1700:
            self.bb_x_start = road_data['Flat']['2']['x']['start']
            self.bb_x_width = road_data['Flat']['2']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['2']['y']
            self.bb_dir = 0

        elif 1700 < object.x and object.x < 1720:
            self.bb_x_start = road_data['Down']['3']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['3']['y']
            self.bb_dir = -1
        elif 1720 < object.x and object.x < 1740:
            self.bb_x_start = road_data['Down']['3']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['3']['y'] - self.bb_move_y * 1
        elif 1740 < object.x and object.x < 1760:
            self.bb_x_start = road_data['Down']['3']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['3']['y'] - self.bb_move_y * 2
        elif 1760 < object.x and object.x < 1780:
            self.bb_x_start = road_data['Down']['3']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['3']['y'] - self.bb_move_y * 3
        elif 1780 < object.x and object.x < 1800:
            self.bb_x_start = road_data['Down']['3']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['3']['y'] - self.bb_move_y * 4
        elif 1800 < object.x and object.x < 1820:
            self.bb_x_start = road_data['Down']['3']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['3']['y'] - self.bb_move_y * 5
            self.bb_dir = -1

        elif 1820 < object.x and object.x < 2290:
            self.bb_x_start = road_data['Flat']['4']['x']['start']
            self.bb_x_width = road_data['Flat']['4']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['4']['y']
            self.bb_dir = 0

        elif 2290 < object.x and object.x < 2310:
            self.bb_x_start = road_data['Up']['5']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['5']['y']
            self.bb_dir = 1
        elif 2310 < object.x and object.x < 2330:
            self.bb_x_start = road_data['Up']['5']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['5']['y'] + self.bb_move_y * 1
        elif 2330 < object.x and object.x < 2350:
            self.bb_x_start = road_data['Up']['5']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['5']['y'] + self.bb_move_y * 2
        elif 2350 < object.x and object.x < 2370:
            self.bb_x_start = road_data['Up']['5']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['5']['y'] + self.bb_move_y * 3
        elif 2370 < object.x and object.x < 2390:
            self.bb_x_start = road_data['Up']['5']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['5']['y'] + self.bb_move_y * 4
        elif 2390 < object.x and object.x < 2420:
            self.bb_x_start = road_data['Up']['5']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x + 10
            self.bb_y = road_data['Up']['5']['y'] + self.bb_move_y * 5
            self.bb_dir = 1

        elif 2420 < object.x and object.x < 3290:
            self.bb_x_start = road_data['Flat']['6']['x']['start']
            self.bb_x_width = road_data['Flat']['6']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['6']['y']
            self.bb_dir = 0

        elif 3290 < object.x and object.x < 3310:
            self.bb_x_start = road_data['Down']['7']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y']
            self.bb_dir = -1
        elif 3310 < object.x and object.x < 3330:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 1
        elif 3330 < object.x and object.x < 3350:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 2
        elif 3350 < object.x and object.x < 3370:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 3
        elif 3370 < object.x and object.x < 3390:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 4
        elif 3390 < object.x and object.x < 3410:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 5
        elif 3410 < object.x and object.x < 3430:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 6
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 6
        elif 3430 < object.x and object.x < 3450:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 7
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 7
        elif 3450 < object.x and object.x < 3470:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 8
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 8
        elif 3470 < object.x and object.x < 3490:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 9
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 9
        elif 3490 < object.x and object.x < 3510:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 10
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 10
        elif 3510 < object.x and object.x < 3530:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 11
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 11
        elif 3530 < object.x and object.x < 3560:
            self.bb_x_start = road_data['Down']['7']['x']['start'] + self.bb_move_x * 12
            self.bb_x_width = self.bb_move_x + 10
            self.bb_y = road_data['Down']['7']['y'] - self.bb_move_y * 12
            self.bb_dir = -1

        elif 3560 < object.x and object.x < 3615:
            self.bb_x_start = road_data['Flat']['8']['x']['start']
            self.bb_x_width = road_data['Flat']['8']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['8']['y']
            self.bb_dir = 0

        elif 3615 < object.x and object.x < 4550:
            self.bb_x_start = road_data['Flat']['9']['x']['start']
            self.bb_x_width = road_data['Flat']['9']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['9']['y']
            self.bb_dir = 0

        elif 4550 < object.x and object.x < 4570:
            self.bb_x_start = road_data['Up']['10']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y']
            self.bb_dir = 1
        elif 4570 < object.x and object.x < 4590:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 1
        elif 4590 < object.x and object.x < 4610:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 3
        elif 4610 < object.x and object.x < 4630:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 4
        elif 4630 < object.x and object.x < 4650:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 6
        elif 4650 < object.x and object.x < 4670:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 7
        elif 4670 < object.x and object.x < 4690:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 6
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 9
        elif 4690 < object.x and object.x < 4710:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 7
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 10
        elif 4710 < object.x and object.x < 4730:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 8
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 12
        elif 4730 < object.x and object.x < 4750:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 9
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 13
        elif 4750 < object.x and object.x < 4770:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 10
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 15
        elif 4770 < object.x and object.x < 4790:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 11
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 16
        elif 4790 < object.x and object.x < 4810:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 12
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 18
        elif 4810 < object.x and object.x < 4830:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 13
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 19
        elif 4830 < object.x and object.x < 4850:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 14
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 21
        elif 4850 < object.x and object.x < 4870:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 15
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 22
        elif 4870 < object.x and object.x < 4890:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 16
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 24
        elif 4890 < object.x and object.x < 4910:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 17
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 25
        elif 4910 < object.x and object.x < 4950:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 18
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 27
        elif 4910 < object.x and object.x < 4950:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 19
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 28
        elif 4950 < object.x and object.x < 4970:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 20
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 30
        elif 4970 < object.x and object.x < 4990:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 21
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 31
        elif 4990 < object.x and object.x < 5010:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 22
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 33
        elif 5010 < object.x and object.x < 5030:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 23
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 34
        elif 5030 < object.x and object.x < 5050:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 24
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 36
        elif 5050 < object.x and object.x < 5070:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 25
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 37
        elif 5070 < object.x and object.x < 5090:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 26
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 39
        elif 5090 < object.x and object.x < 5110:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 27
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 40
        elif 5110 < object.x and object.x < 5130:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 28
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 42
        elif 5130 < object.x and object.x < 5150:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 29
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 43
        elif 5150 < object.x and object.x < 5170:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 30
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 45
        elif 5170 < object.x and object.x < 5190:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 31
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 46
        elif 5190 < object.x and object.x < 5210:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 32
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 48
        elif 5210 < object.x and object.x < 5230:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 33
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 49
        elif 5230 < object.x and object.x < 5250:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 34
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 51
        elif 5250 < object.x and object.x < 5270:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 35
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 52
        elif 5270 < object.x and object.x < 5290:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 36
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 54
        elif 5290 < object.x and object.x < 5310:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 37
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 55
        elif 5310 < object.x and object.x < 5330:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 38
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 57
        elif 5330 < object.x and object.x < 5350:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 39
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 58
        elif 5350 < object.x and object.x < 5370:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 40
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 60
        elif 5370 < object.x and object.x < 5390:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 41
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 61
        elif 5390 < object.x and object.x < 5410:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 42
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 63
        elif 5410 < object.x and object.x < 5430:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 43
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 64
        elif 5430 < object.x and object.x < 5450:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 44
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 66
        elif 5450 < object.x and object.x < 5470:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 45
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 67
        elif 5470 < object.x and object.x < 5490:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 46
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 69
        elif 5490 < object.x and object.x < 5510:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 47
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 70
        elif 5510 < object.x and object.x < 5530:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 48
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 72
        elif 5530 < object.x and object.x < 5550:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 49
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 73
        elif 5550 < object.x and object.x < 5570:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 50
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 75
        elif 5570 < object.x and object.x < 5590:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 51
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 76
        elif 5590 < object.x and object.x < 5610:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 52
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 78
        elif 5610 < object.x and object.x < 5630:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 53
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 79
        elif 5630 < object.x and object.x < 5650:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 54
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 81
        elif 5650 < object.x and object.x < 5670:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 55
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 82
        elif 5670 < object.x and object.x < 5690:
            self.bb_x_start = road_data['Up']['10']['x']['start'] + self.bb_move_x * 56
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['10']['y'] + self.bb_move_y * 83
            self.bb_dir = 1

        elif 5690 < object.x and object.x < 5850:
            self.bb_x_start = road_data['Flat']['11']['x']['start']
            self.bb_x_width = road_data['Flat']['11']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['11']['y']
            self.bb_dir = 0

        elif 5850 < object.x and object.x < 5870:
            self.bb_x_start = road_data['Down']['12']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y']
            self.bb_dir = -1
        elif 5870 < object.x and object.x < 5890:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 1
        elif 5890 < object.x and object.x < 5910:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 3
        elif 5910 < object.x and object.x < 5930:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 4
        elif 5930 < object.x and object.x < 5950:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 6
        elif 5950 < object.x and object.x < 5970:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 7
        elif 5970 < object.x and object.x < 5990:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 6
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 9
        elif 5990 < object.x and object.x < 6010:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 7
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 10
        elif 6010 < object.x and object.x < 6030:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 8
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 12
        elif 6030 < object.x and object.x < 6050:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 9
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 13
        elif 6050 < object.x and object.x < 6070:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 10
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 15
        elif 6070 < object.x and object.x < 6090:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 11
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 16
        elif 6090 < object.x and object.x < 6110:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 12
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 18
        elif 6110 < object.x and object.x < 6130:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 13
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 19
        elif 6130 < object.x and object.x < 6150:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 14
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 21
        elif 6150 < object.x and object.x < 6170:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 15
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 22
        elif 6170 < object.x and object.x < 6190:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 16
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 24
        elif 6190 < object.x and object.x < 6210:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 17
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 25
        elif 6210 < object.x and object.x < 6230:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 18
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 27
        elif 6230 < object.x and object.x < 6250:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 19
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 28
        elif 6250 < object.x and object.x < 6270:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 20
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 30
        elif 6270 < object.x and object.x < 6290:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 21
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 31
        elif 6290 < object.x and object.x < 6310:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 22
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 33
        elif 6310 < object.x and object.x < 6330:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 23
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 34
        elif 6330 < object.x and object.x < 6350:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 24
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 36
        elif 6350 < object.x and object.x < 6370:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 25
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 37
        elif 6370 < object.x and object.x < 6390:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 26
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 39
        elif 6390 < object.x and object.x < 6410:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 27
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 40
        elif 6410 < object.x and object.x < 6430:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 28
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 42
        elif 6430 < object.x and object.x < 6450:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 29
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 43
        elif 6450 < object.x and object.x < 6470:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 30
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 45
        elif 6470 < object.x and object.x < 6490:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 31
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 46
        elif 6490 < object.x and object.x < 6510:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 32
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 48
        elif 6510 < object.x and object.x < 6530:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 33
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 49
        elif 6530 < object.x and object.x < 6550:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 34
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 51
        elif 6550 < object.x and object.x < 6570:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 35
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 52
        elif 6570 < object.x and object.x < 6590:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 36
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 54
        elif 6590 < object.x and object.x < 6610:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 37
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 55
        elif 6610 < object.x and object.x < 6630:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 38
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 57
        elif 6630 < object.x and object.x < 6650:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 39
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 58
        elif 6650 < object.x and object.x < 6670:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 40
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 60
        elif 6670 < object.x and object.x < 6690:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 41
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 61
        elif 6690 < object.x and object.x < 6710:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 42
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 63
        elif 6710 < object.x and object.x < 6730:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 43
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 64
        elif 6730 < object.x and object.x < 6750:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 44
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 66
        elif 6750 < object.x and object.x < 6770:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 45
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 67
        elif 6770 < object.x and object.x < 6790:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 46
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 69
        elif 6790 < object.x and object.x < 6810:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 47
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 70
        elif 6810 < object.x and object.x < 6830:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 48
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 72
        elif 6830 < object.x and object.x < 6850:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 49
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 73
        elif 6850 < object.x and object.x < 6880:
            self.bb_x_start = road_data['Down']['12']['x']['start'] + self.bb_move_x * 50
            self.bb_x_width = self.bb_move_x + 10
            self.bb_y = road_data['Down']['12']['y'] - self.bb_move_y * 75
            self.bb_dir = -1

        elif 6880 < object.x and object.x < 7166:
            self.bb_x_start = road_data['Flat']['13']['x']['start']
            self.bb_x_width = road_data['Flat']['13']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['13']['y']
            self.bb_dir = 0


        elif 1820 < object.x and object.x < 1980:
            self.bb_x_start = road_data['Flat']['stair1']['x']['start']
            self.bb_x_width = road_data['Flat']['stair1']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair1']['y']
            self.bb_dir = 0

        elif 1980 < object.x and object.x < 2120:
            self.bb_x_start = road_data['Flat']['stair2']['x']['start']
            self.bb_x_width = road_data['Flat']['stair2']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair2']['y']
            self.bb_dir = 0

        elif 2105 < object.x and object.x < 2300:
            self.bb_x_start = road_data['Flat']['stair3']['x']['start']
            self.bb_x_width = road_data['Flat']['stair3']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair3']['y']
            self.bb_dir = 0

        elif 2375 < object.x and object.x < 2505:
            self.bb_x_start = road_data['Flat']['stair4']['x']['start']
            self.bb_x_width = road_data['Flat']['stair4']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair4']['y']
            self.bb_dir = 0

        elif 3700 < object.x and object.x < 4250:
            self.bb_x_start = road_data['Flat']['stair5']['x']['start']
            self.bb_x_width = road_data['Flat']['stair5']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair5']['y']
            self.bb_dir = 0

        elif 4250 < object.x and object.x < 4270:
            self.bb_x_start = road_data['Up']['stair6']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair6']['y']
            self.bb_dir = 1
        elif 4270 < object.x and object.x < 4290:
            self.bb_x_start = road_data['Up']['stair6']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair6']['y'] + self.bb_move_y * 1
        elif 4290 < object.x and object.x < 4310:
            self.bb_x_start = road_data['Up']['stair6']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair6']['y'] + self.bb_move_y * 2
        elif 4310 < object.x and object.x < 4330:
            self.bb_x_start = road_data['Up']['stair6']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair6']['y'] + self.bb_move_y * 3
        elif 4330 < object.x and object.x < 4350:
            self.bb_x_start = road_data['Up']['stair6']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair6']['y'] + self.bb_move_y * 4
        elif 4350 < object.x and object.x < 4370:
            self.bb_x_start = road_data['Up']['stair6']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair6']['y'] + self.bb_move_y * 5
        elif 4370 < object.x and object.x < 4385:
            self.bb_x_start = road_data['Up']['stair6']['x']['start'] + self.bb_move_x * 6
            self.bb_x_width = self.bb_move_x - 5
            self.bb_y = road_data['Up']['stair6']['y'] + self.bb_move_y * 6
            self.bb_dir = 1

        elif 4385 < object.x and object.x < 4660:
            self.bb_x_start = road_data['Flat']['stair7']['x']['start']
            self.bb_x_width = road_data['Flat']['stair7']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair7']['y']
            self.bb_dir = 0

        elif 4660 < object.x and object.x < 4680:
            self.bb_x_start = road_data['Up']['stair8']['x']['start']
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y']
            self.bb_dir = 1
        elif 4680 < object.x and object.x < 4700:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 1
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 1
        elif 4700 < object.x and object.x < 4720:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 2
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 2
        elif 4720 < object.x and object.x < 4740:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 3
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 3
        elif 4740 < object.x and object.x < 4760:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 4
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 4
        elif 4760 < object.x and object.x < 4780:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 5
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 5
        elif 4780 < object.x and object.x < 4800:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 6
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 6
        elif 4800 < object.x and object.x < 4820:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 7
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 7
        elif 4820 < object.x and object.x < 4840:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 8
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 8
        elif 4840 < object.x and object.x < 4860:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 9
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 9
        elif 4860 < object.x and object.x < 4880:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 10
            self.bb_x_width = self.bb_move_x
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 10
        elif 4880 < object.x and object.x < 4895:
            self.bb_x_start = road_data['Up']['stair8']['x']['start'] + self.bb_move_x * 11
            self.bb_x_width = self.bb_move_x - 5
            self.bb_y = road_data['Up']['stair8']['y'] + self.bb_move_y * 11
            self.bb_dir = 1

        elif 4895 < object.x and object.x < 5060:
            self.bb_x_start = road_data['Flat']['stair9']['x']['start']
            self.bb_x_width = road_data['Flat']['stair9']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair9']['y']
            self.bb_dir = 0

        elif 5140 < object.x and object.x < 5370:
            self.bb_x_start = road_data['Flat']['stair10']['x']['start']
            self.bb_x_width = road_data['Flat']['stair10']['x']['end'] - self.bb_x_start
            self.bb_y = road_data['Flat']['stair10']['y']
            self.bb_dir = 0

        return self.bb_x_start - self.window_left, self.bb_y - self.window_bottom, self.bb_x_start + self.bb_x_width - self.window_left, self.bb_y + 70 - self.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def set_center_object(self, character):
        self.center_object = character

    def update(self, frame_time):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.h - self.canvas_height)
