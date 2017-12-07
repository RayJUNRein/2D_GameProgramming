from pico2d import *

# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672
# 피벗으로 인한 객체 위치 지정 (피벗 : 객체 중앙)
center = height / 2
# 스테이지 1 지형 맵 크기 지정 (가로 7166 x 세로 448 pixel)
road_w = 7166
# 보스 Golem Wood 출현 맵 크기 지정 (가로 576 pixel x 5)
gwroad_w = 576
gwroad_h = 171

# 스테이지 1 보스 Golem Wood 출현하는 맵1
class GWoodBackground:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road33.png')
        self.x = road_w + (1872 / 2)
        self.y = center

    def draw(self, frame_time):
        self.image.draw(self.x, self.y)


# 스테이지 1 보스 Golem Wood 출현하는 맵2 (애니메이션 적용 예정)
class GWoodRoad:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road_GolemWood.png')
        self.x = road_w + (gwroad_w / 2)
        self.y = center

    def draw(self, frame_time, i):
        global move_w
#        if move_w > road_w:
#            self.image.draw(self.x * i, self.y)

    def get_bb(self):
        return self.x - gwroad_w / 2, self.y - gwroad_h / 2, self.x + gwroad_w / 2, self.y + gwroad_h / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
