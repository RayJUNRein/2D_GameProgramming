import random
import json
from pico2d import *

import Game_Framework


name = "MainState"


background = None
road = None
gwroads = None
gwbackground = None
character = None
weapons = None
goblins = None
fonts = None
cards = None


# 달리는 상태인지 알려주는 변수 선언 (True = 달리는 상태)
run_status = False
# 앉은 상태인지 알려주는 변수 선언 (True = 앉은 상태)
sit_status = False
# 위를 보는 상태인지 알려주는 변수 선언 (True = 위를 보는 상태)
up_status = False
# 사격하는 상태인지 알려주는 변수 선언 (True = 사격하는 상태)
shot_status = False


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
# 맵 이동 위한 이동 위치 저장 변수
move_w = 0
move_tmp = 0
# 주인공 시선 방향 저장 변수
character_dir = 1
# 주인공 무기 위치 저장 변수
character_w = 2000
character_h = 300


# 배경 이미지
class Background:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Background\MidnightWanderers_Levels_1_Background2.png')
        self.x = (width / 2)
        self.y = center

    def draw(self, frame_time):
        self.image.draw(self.x, self.y)


# 스테이지 1 Golem Wood 출현 전까지의 맵
class Road:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road.png')
        self.x = width / 2
        self.y = center

    def draw(self, frame_time):
        global width, height, move_w

        # 맵 이동 시 맵 크기 이내에서 그리도록 함
        if move_w < 0:
            move_w = 0
        elif move_w > (road_w - width):
            move_w = road_w - width

        self.image.clip_draw(move_w, 0, width, height, self.x, self.y)

    def get_bb(self):
        return self.x - road_w / 2, self.y - height / 2, self.x + road_w / 2, self.y + height / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        global move_w

        # 맵 이동을 위한 위치 변화 저장
        if run_status == True:
            #move_w += character.x - move_tmp
            move_w += character.dir_x * 20


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
        if move_w > road_w:
            self.image.draw(self.x * i, self.y)

    def get_bb(self):
        return self.x - gwroad_w / 2, self.y - gwroad_h / 2, self.x + gwroad_w / 2, self.y + gwroad_h / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


# 주인공 캐릭터 (1P : Lou)
class Character:
    # 1 pixel = 1cm
    PIXEL_PER_METER = (10.0 / 0.1)
    # 달리기 속도 = 12km/h
    RUN_SPEED_KMPH = 12.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    # 주인공 액션 상태 구분
    LEFT_STAND, RIGHT_STAND, LEFT_RUN, RIGHT_RUN, LEFT_SIT, RIGHT_SIT, LEFT_UP, RIGHT_UP,    \
    LEFT_JUMP, RIGHT_JUMP, LEFT_SHOT, RIGHT_SHOT = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

    # 왼쪽 보며 대기
    def handle_left_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftStand.png')
        self.draw_width = 156
        self.draw_height = 123
        self.frame_num = 2

    # 오른쪽 보며 대기
    def handle_right_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightStand.png')
        self.draw_width = 156
        self.draw_height = 123
        self.frame_num = 2

    # 왼쪽 보며 달리기
    def handle_left_run(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftRun.png')
        self.draw_width = 156
        self.draw_height = 129
        self.frame_num = 6

    # 오른쪽 보며 달리기
    def handle_right_run(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightRun.png')
        self.draw_width = 156
        self.draw_height = 129
        self.frame_num = 6

    # 왼쪽 보며 앉기
    def handle_left_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftSit.png')
        self.draw_width = 147
        self.draw_height = 96
        self.frame_num = 1

    # 오른쪽 보며 앉기
    def handle_right_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightSit.png')
        self.draw_width = 147
        self.draw_height = 96
        self.frame_num = 1

    # 왼쪽 방향 위로 보기
    def handle_left_up(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftUp.png')
        self.draw_width = 132
        self.draw_height = 150
        self.frame_num = 1

    # 오른쪽 방향 위로 보기
    def handle_right_up(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightUp.png')
        self.draw_width = 132
        self.draw_height = 150
        self.frame_num = 1

    # 왼쪽 보며 점프
    def handle_left_jump(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftJump.png')
        self.draw_width = 150
        self.draw_height = 150
        self.frame_num = 4

    # 오른쪽 보며 점프
    def handle_right_jump(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightJump.png')
        self.draw_width = 150
        self.draw_height = 150
        self.frame_num = 4

    # 왼쪽 보며 사격
    def handle_left_shot(self):
        # 왼쪽 보며 앉아서 사격
        if sit_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftSit.png')
            self.draw_width = 147
            self.draw_height = 96
            self.frame_num = 2

        # 왼쪽 방향 위로 보며 사격
        elif up_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftUp.png')
            self.draw_width = 132
            self.draw_height = 150
            self.frame_num = 2

        # 왼쪽 보며 서있는 상태 사격
        else:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftShot.png')
            self.draw_width = 144
            self.draw_height = 123
            self.frame_num = 3

    # 오른쪽 보며 사격
    def handle_right_shot(self):
        # 오른쪽 보며 앉아서 사격
        if sit_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightSit.png')
            self.draw_width = 147
            self.draw_height = 96
            self.frame_num = 2

        # 오른쪽 방향 위로 보며 사격
        elif up_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightUp.png')
            self.draw_width = 132
            self.draw_height = 150
            self.frame_num = 2

        # 오른쪽 보며 서있는 상태 사격
        else:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightShot.png')
            self.draw_width = 144
            self.draw_height = 123
            self.frame_num = 3

    # 주인공 액션 상태에 따라 실행할 함수 구분
    handle_state = {
        LEFT_STAND:     handle_left_stand,
        RIGHT_STAND:    handle_right_stand,
        LEFT_RUN:       handle_left_run,
        RIGHT_RUN:      handle_right_run,
        LEFT_SIT:       handle_left_sit,
        RIGHT_SIT:      handle_right_sit,
        LEFT_UP:        handle_left_up,
        RIGHT_UP:       handle_right_up,
        LEFT_JUMP:      handle_left_jump,
        RIGHT_JUMP:     handle_right_jump,
        LEFT_SHOT:      handle_left_shot,
        RIGHT_SHOT:     handle_right_shot
    }

    # 초기화
    def __init__(self):
        self.x, self.y = 200, 300
        self.frame = 0
        self.frame_num = 4
        self.dir_x = 0
        self.dir_y = 0
        self.jump_y = 300
        self.state = self.RIGHT_STAND
        self.draw_width = 156
        self.draw_height = 123

    # 상태 변화 적용
    def update(self, frame_time):
        global run_status, shot_status, character_dir, character_w, move_w
        self.frame = (self.frame + 1) % self.frame_num
        self.handle_state[self.state](self)
        distance = Character.RUN_SPEED_PPS * frame_time

        if move_w > 650:
            self.dir_y = -1
        self.x += self.dir_x * distance
        self.y += self.dir_y * distance

        # 주인공이 화면 밖으로 나가는 것을 방지
        if self.x < 30:
            self.x = 30
        elif self.x > width - 30:
            self.x = width - 30
        if self.y < 50:
            self.y = 50
        elif self.y > height - 50:
            self.y = height - 50

        # 점프 뒤 하강
        if self.y > self.jump_y:
            self.dir_y = -1
        elif self.y < 300:
            self.y = 300
            if self.state == self.RIGHT_JUMP:
                self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_JUMP:
                self.state = self.LEFT_STAND

        # 주인공 시선 방향 저장 (-1 : 왼쪽, 1 : 오른쪽)
        if self.state == self.LEFT_SHOT:
            character_dir = -1
        elif self.state == self.RIGHT_SHOT:
            character_dir = 1

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * self.draw_width, 0, self.draw_width, self.draw_height, self.x, self.y)

    def get_bb(self):
        return self.x - self.draw_width / 2, self.y - self.draw_height / 2, self.x + self.draw_width / 2, self.y + self.draw_height / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        global run_status, sit_status, up_status, shot_status
        global move_tmp, character_w, character_h

        # 왼쪽 보며 대기
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            run_status = False
            self.state = self.LEFT_STAND
            self.dir_x = 0

        # 오른쪽 보며 대기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            run_status = False
            self.state = self.RIGHT_STAND
            self.dir_x = 0

        # 왼쪽 보며 달리기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            run_status = True
            move_tmp = self.x
            self.state = self.LEFT_RUN
            self.dir_x = -1

        # 오른쪽 보며 달리기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            run_status = True
            move_tmp = self.x
            self.state = self.RIGHT_RUN
            self.dir_x = 1

        # 앉기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            sit_status = True

            # 왼쪽 보며 앉기
            if self.state == self.LEFT_STAND:
                self.state = self.LEFT_SIT
            # 오른쪽 보며 앉기
            elif self.state == self.RIGHT_STAND:
                self.state = self.RIGHT_SIT

        # 일어서기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            sit_status = False

            # 왼쪽 보며 대기
            if self.state == self.LEFT_SIT:
                self.state = self.LEFT_STAND
            # 오른쪽 보며 대기
            elif self.state == self.RIGHT_SIT:
                self.state = self.RIGHT_STAND

        # 위로 보기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            up_status = True

            # 왼쪽 방향 위로 보기
            if self.state == self.LEFT_STAND:
                self.state = self.LEFT_UP
            # 오른쪽 방향 위로 보기
            elif self.state == self.RIGHT_STAND:
                self.state = self.RIGHT_UP

        # 다시 정면 보기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            up_status = False

            # 왼쪽 보며 대기
            if self.state == self.LEFT_UP:
                self.state = self.LEFT_STAND
            # 오른쪽 보며 대기
            elif self.state == self.RIGHT_UP:
                self.state = self.RIGHT_STAND

        # 점프
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LALT):
            self.jump_y = self.y + 200

            # 왼쪽 보며 점프
            if self.state == self.LEFT_RUN or self.state == self.LEFT_STAND:
                self.state = self.LEFT_JUMP
                self.dir_y = 1
            # 오른쪽 보며 점프
            elif self.state == self.RIGHT_RUN or self.state == self.RIGHT_STAND:
                self.state = self.RIGHT_JUMP
                self.dir_y = 1

        # 사격 시작
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            shot_status = True
            character_w = self.x
            character_h = self.y

            # 왼쪽 방향 사격
            if self.state == self.LEFT_RUN or self.state == self.LEFT_STAND or  \
               self.state == self.LEFT_SIT or self.state == self.LEFT_UP or \
               self.state == self.LEFT_JUMP:
                self.state = self.LEFT_SHOT
            # 오른쪽 방향 사격
            elif self.state == self.RIGHT_RUN or self.state == self.RIGHT_STAND or \
                 self.state == self.RIGHT_SIT or self.state == self.RIGHT_UP or \
                 self.state == self.RIGHT_JUMP:
                self.state = self.RIGHT_SHOT

        # 사격 중지
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            shot_status = False

            if self.state == self.LEFT_SHOT:
                # 왼쪽 보며 앉기
                if sit_status == True:
                    self.state = self.LEFT_SIT
                # 왼쪽 방향 위로 보기
                elif up_status == True:
                    self.state = self.LEFT_UP
                # 왼쪽 보며 대기
                else:
                    self.state = self.LEFT_STAND

            elif self.state == self.RIGHT_SHOT:
                # 오른쪽 보며 앉기
                if sit_status == True:
                    self.state = self.RIGHT_SIT
                # 오른쪽 방향 위로 보기
                elif up_status == True:
                    self.state = self.RIGHT_UP
                # 오른쪽 보며 대기
                else:
                    self.state = self.RIGHT_STAND


# 주인공 무기
class Weapon:
    # 1 pixel = 1cm
    PIXEL_PER_METER = (10.0 / 0.1)
    # 달리기 속도 = 25km/h
    RUN_SPEED_KMPH = 25.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightArrow1.png')
        self.arrow_w = 279 / 2
        self.arrow_h = 63
        self.x = 800
        self.y = character_h
        self.weapon_w = 0
        self.weapon_h = 0
        self.draw_width = 93
        self.draw_height = 21

    def draw(self, frame_time):
        global shot_status, sit_status, up_status, character_dir, character_w, character_h

        if shot_status == True:
            if character_dir == -1:
                self.x = character_w - self.arrow_w
            elif character_dir == 1:
                self.x = character_w + self.arrow_w

            if sit_status == True:
                self.y = character_h - 10
            elif sit_status == False:
                self.y = character_h
            if up_status == True:
                self.x = character_w
                self.y = character_h + self.arrow_w

        else:
            if character_dir == -1:
                if self.x < self.weapon_w:
                    self.y = 2000
                else:
                    self.image.draw(self.x, self.y)
            elif character_dir == 1:
                if self.x > self.weapon_w:
                    self.y = 2000
                else:
                    self.image.draw(self.x, self.y)
            if up_status == True:
                if self.y < self.weapon_h:
                    self.y = 2000
                else:
                    self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.draw_width / 2, self.y - self.draw_height / 2, self.x + self.draw_width / 2, self.y + self.draw_height / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Weapon.RUN_SPEED_PPS * frame_time

        if character_dir == -1:
            if up_status == False:
                self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftArrow1.png')
                self.weapon_w = character_w - 600
                self.x += character_dir * distance
                self.draw_width = 93
                self.draw_height = 21
        elif character_dir == 1:
            if up_status == False:
                self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightArrow1.png')
                self.weapon_w = character_w + 600
                self.x += character_dir * distance
                self.draw_width = 93
                self.draw_height = 21
        if up_status == True:
            self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_UpArrow1.png')
            self.weapon_h = character_h + 600
            self.y += character_dir * distance
            self.draw_width = 21
            self.draw_height = 93


# 적군
class Goblin:
    # 1 pixel = 1cm
    PIXEL_PER_METER = (10.0 / 0.1)
    # 달리기 속도 = 6km/h
    RUN_SPEED_KMPH = 6.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        global width
        self.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin2.png')
        self.x, self.y = random.randint(600, road_w), 300
        self.frame = 0
        self.frame_num = 6
        self.draw_width = 158
        self.draw_height = 141
        self.dir = -1

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * self.draw_width, 0, self.draw_width, self.draw_height, self.x, self.y)

    def get_bb(self):
        return self.x - self.draw_width / 2, self.y - self.draw_height / 2, self.x + self.draw_width / 2, self.y + self.draw_height / 2

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Goblin.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % self.frame_num
        self.x += self.dir * distance


class Font:
    def __init__(self):
        self.name = 'noname'
        self.image = load_image('Resources\ThreeWonders_Miscellaneous1.png')
        self.x, self.y = 100, height - 15
        self.frame_w = 0
        self.frame_h = 0
        self.draw_width = 24
        self.draw_height = 25

    def draw(self, frame_time):
        self.image.clip_draw(self.frame_w * self.draw_width, self.frame_h * self.draw_height, self.draw_width, self.draw_height, self.x, self.y)


class Card:
    def __init__(self):
        self.name = 'noname'
        self.image = load_image('Resources\Items\ThreeWonders_Items_Card.png')
        self.x, self.y = random.randint(200, road_w), 300
        self.frame_num = 4
        self.frame_w = 0
        self.frame_h = 0
        self.draw_width = 90
        self.draw_height = 160

    def draw(self, frame_time):
        self.image.clip_draw(self.frame_w * self.draw_width, self.frame_h * self.draw_height, self.draw_width, self.draw_height, self.x, self.y)

    def get_bb(self):
        return self.x - self.draw_width / 2, self.y - self.draw_height / 2 + 30, self.x + self.draw_width / 2, self.y + self.draw_height / 2 - 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        self.frame_h = (self.frame_h + 1) % self.frame_num


def create_fonts():
    font_data_file = open('Font_Data.txt', 'r')
    font_data = json.load(font_data_file)
    font_data_file.close()
    fonts = []
    for name in font_data:
        font = Font()
        font.name = name
        font.frame_w = font_data[name]['w']
        font.frame_h = font_data[name]['h']
        font.x = font_data[name]['x']
        fonts.append(font)

    return fonts


def create_cards():
    card_data_file = open('Card_Data.txt', 'r')
    card_data = json.load(card_data_file)
    card_data_file.close()
    cards = []
    for name in card_data:
        card = Card()
        card.name = name
        card.frame_h = card_data[name]['h']
        card.x = card_data[name]['x']
        fonts.append(card)

    return cards


def enter():
    global background, road, gwroads, gwbackground, character, weapons, goblins, fonts, cards

    open_canvas(width, height)
    Game_Framework.reset_time()

    background = Background()
    road = Road()
    gwroads = [GWoodRoad() for i in range(5)]
    gwbackground = GWoodBackground()
    character = Character()
    weapons = [Weapon() for i in range(5)]
    goblins = [Goblin() for i in range(100)]
    fonts = create_fonts()
    cards = [Card() for i in range(20)]


def exit():
    global background, road, gwroads, gwbackground, character, weapons, goblins, fonts, cards

    del background
    del road
    del gwroads
    del gwbackground
    del character
    del weapons
    del goblins
    del fonts
    del cards

    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global run_status, sit_status, up_status, shot_status, move_tmp, character_w, character_h
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            Game_Framework.quit()

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            Game_Framework.quit()

        else:
            character.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update(frame_time):
    character.update(frame_time)
    for weapon in weapons:
        weapon.update(frame_time)
    for goblin in goblins:
        goblin.update(frame_time)
    road.update(frame_time)
    for card in cards:
        card.update(frame_time)

    for goblin in goblins:
        if collide(weapon, goblin):
            goblins.remove(goblin)
    for card in cards:
        if collide(character, card):
            cards.remove(card)
    delay(0.08)


def draw(frame_time):
    clear_canvas()

    # 배경 이미지 화면 출력
    background.draw(frame_time)

    # 스테이지 1 기본 지형 맵 화면 출력
    road.draw(frame_time)

    # 스테이지 1 보스 Golem Wood 출현 맵 화면 출력 (애니메이션 미적용)
    i = 0
    for gwroad in gwroads:
        gwroad.draw(frame_time, i)
        i += 1
    gwbackground.draw(frame_time)

    # 주인공 화면 출력
    character.draw(frame_time)
    # 주인공 무기 화면 출력
    for weapon in weapons:
        weapon.draw(frame_time)

    # 적군 화면 출력
    for goblin in goblins:
        goblin.draw(frame_time)

    # 캐릭터 정보 화면 출력
    for font in fonts:
        font.draw(frame_time)

    # 점수 카드 화면 출력
    for card in cards:
        card.draw(frame_time)

#    road.draw_bb()
#    for gwroad in gwroads:
#        gwroad.draw_bb()
#    character.draw_bb()
#    for weapon in weapons:
#        weapon.draw_bb()
#    for goblin in goblins:
#        goblin.draw_bb()
#    for card in cards:
#        card.draw_bb()

    update_canvas()
