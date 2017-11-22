from pico2d import *


running = True
# 달리는 상태인지 알려주는 변수 선언 (True = 달리는 상태)
run_status = False
# 앉은 상태인지 알려주는 변수 선언 (True = 앉은 상태)
sit_status = False
# 위를 보는 상태인지 알려주는 변수 선언 (True = 위를 보는 상태)
up_status = False
# 사격하는 상태인지 알려주는 변수 선언 (True = 사격하는 상태)
shot_status = False


# 플레이 화면 크기 지정 (가로 384 x 세로 224 pixel)
width = 384
height = 224
# 피벗으로 인한 객체 위치 지정 (피벗 : 객체 중앙)
center = height / 2
# 스테이지 1 지형 맵 크기 지정 (가로 3583 x 세로 224 pixel)
road_w = 3583
# 보스 Golem Wood 출현 맵 크기 지정 (가로 192 pixel x 5)
gwroad_w = 192
# 맵 이동 위한 이동 위치 저장 변수
move_w = 0
move_tmp = 0
# 주인공 시선 방향 저장 변수
character_dir = 1
# 주인공 무기 위치 저장 변수
character_w = 100
character_h = 100


# 배경 이미지
class Background:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Background\MidnightWanderers_Levels_1_Background2.png')

    def draw(self):
        self.image.draw((width / 2), center)


# 스테이지 1 Golem Wood 출현 전까지의 맵
class Road:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road.png')

    def draw(self):
        global width, height, move_w

        # 맵 이동 시 맵 크기 이내에서 그리도록 함
        if move_w < 0:
            move_w = 0
        elif move_w > (road_w - width):
            move_w = road_w - width

        self.image.clip_draw(move_w, 0, width, height, width / 2, center)


# 스테이지 1 보스 Golem Wood 출현하는 맵1
class GWoodBackground:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road33.png')

    def draw(self):
        self.image.draw(road_w + (624 / 2), center)


# 스테이지 1 보스 Golem Wood 출현하는 맵2 (애니메이션 적용 예정)
class GWoodRoad:
    def __init__(self):
        self.image = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road_GolemWood.png')

    def draw(self, i):
        global move_w
        if move_w > road_w:
            self.image.draw((road_w + (gwroad_w / 2)) * i, center)


# 주인공 캐릭터 (1P : Lou)
class Character:
    image = None

    # 주인공 액션 상태 구분
    LEFT_STAND, RIGHT_STAND, LEFT_RUN, RIGHT_RUN, LEFT_SIT, RIGHT_SIT, LEFT_UP, RIGHT_UP,    \
    LEFT_JUMP, RIGHT_JUMP, LEFT_SHOT, RIGHT_SHOT = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

    # 왼쪽 보며 대기
    def handle_left_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftStand.png')
        self.draw_width = 52
        self.draw_height = 41
        self.frame_num = 2

    # 오른쪽 보며 대기
    def handle_right_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightStand.png')
        self.draw_width = 52
        self.draw_height = 41
        self.frame_num = 2

    # 왼쪽 보며 달리기
    def handle_left_run(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftRun.png')
        self.draw_width = 52
        self.draw_height = 43
        self.frame_num = 6

    # 오른쪽 보며 달리기
    def handle_right_run(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightRun.png')
        self.draw_width = 52
        self.draw_height = 43
        self.frame_num = 6

    # 왼쪽 보며 앉기
    def handle_left_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftSit.png')
        self.draw_width = 49
        self.draw_height = 32
        self.frame_num = 1

    # 오른쪽 보며 앉기
    def handle_right_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightSit.png')
        self.draw_width = 49
        self.draw_height = 32
        self.frame_num = 1

    # 왼쪽 방향 위로 보기
    def handle_left_up(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftUp.png')
        self.draw_width = 44
        self.draw_height = 50
        self.frame_num = 1

    # 오른쪽 방향 위로 보기
    def handle_right_up(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightUp.png')
        self.draw_width = 44
        self.draw_height = 50
        self.frame_num = 1

    # 왼쪽 보며 점프
    def handle_left_jump(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftJump.png')
        self.draw_width = 50
        self.draw_height = 50
        self.frame_num = 4

    # 오른쪽 보며 점프
    def handle_right_jump(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightJump.png')
        self.draw_width = 50
        self.draw_height = 50
        self.frame_num = 4

    # 왼쪽 보며 사격
    def handle_left_shot(self):
        # 왼쪽 보며 앉아서 사격
        if sit_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftSit.png')
            self.draw_width = 49
            self.draw_height = 32
            self.frame_num = 2

        # 왼쪽 방향 위로 보며 사격
        elif up_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftUp.png')
            self.draw_width = 44
            self.draw_height = 50
            self.frame_num = 2

        # 왼쪽 보며 서있는 상태 사격
        else:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftShot.png')
            self.draw_width = 48
            self.draw_height = 41
            self.frame_num = 3

    # 오른쪽 보며 사격
    def handle_right_shot(self):
        # 오른쪽 보며 앉아서 사격
        if sit_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightSit.png')
            self.draw_width = 49
            self.draw_height = 32
            self.frame_num = 2

        # 오른쪽 방향 위로 보며 사격
        elif up_status == True:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightUp.png')
            self.draw_width = 44
            self.draw_height = 50
            self.frame_num = 2

        # 오른쪽 보며 서있는 상태 사격
        else:
            Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightShot.png')
            self.draw_width = 48
            self.draw_height = 41
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
        self.x, self.y = 100, 100
        self.frame = 0
        self.frame_num = 4
        self.dir_x = 0
        self.dir_y = 0
        self.jump_y = 100
        self.state = self.RIGHT_STAND
        self.draw_width = 52
        self.draw_height = 41

    # 상태 변화 적용
    def update(self):
        global run_status, shot_status, move_w, move_tmp, character_dir, character_w
        self.frame = (self.frame + 1) % self.frame_num
        self.handle_state[self.state](self)
        self.x += self.dir_x * 1
        self.y += self.dir_y * 1

        # 맵 이동을 위한 위치 변화 저장
        if run_status == True:
            move_w += self.x - move_tmp

        # 주인공이 화면 밖으로 나가는 것을 방지
        if self.x < 15:
            self.x = 15
        elif self.x > width - 15:
            self.x = width - 15
        if self.y < 20:
            self.y = 20
        elif self.y > height - 20:
            self.y = height - 20

        # 점프 뒤 하강
        if self.y > self.jump_y:
            self.dir_y = -1
        elif self.y < 100:
            self.y = 100
            if self.state == self.RIGHT_JUMP:
                self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_JUMP:
                self.state = self.LEFT_STAND

        # 주인공 시선 방향 저장 (-1 : 왼쪽, 1 : 오른쪽)
        if self.state == self.LEFT_SHOT:
            character_dir = -1
        elif self.state == self.RIGHT_SHOT:
            character_dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * self.draw_width, 0, self.draw_width, self.draw_height, self.x, self.y)


# 주인공 무기
class Weapon:
    def __init__(self):
        self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightArrow1.png')
        self.arrow_w = 40
        self.arrow_h = 7
        self.x = 400
        self.y = center - 10
        self.weapon_w = 0
        self.weapon_h = 0

    def draw(self):
        global shot_status, sit_status, up_status, character_dir, character_w, character_h

        if shot_status == True:
            if character_dir == -1:
                self.x = character_w - self.arrow_w
            elif character_dir == 1:
                self.x = character_w + self.arrow_w

            if sit_status == True:
                self.y = center - 15
            elif up_status == True:
                self.x = character_w
                self.y = character_h + self.arrow_w

        else:
            if character_dir == -1:
                if self.x < self.weapon_w:
                    pass
                else:
                    self.image.draw(self.x, self.y)
            elif character_dir == 1:
                if self.x > self.weapon_w:
                    pass
                else:
                    self.image.draw(self.x, self.y)
            elif up_status == True:
                if self.y < self.weapon_h:
                    pass
                else:
                    self.image.draw(self.x, self.y)

    def update(self):
        if character_dir == -1:
            if up_status == False:
                self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftArrow1.png')
                self.weapon_w = character_w - 300
                self.x += character_dir * 1
        elif character_dir == 1:
            if up_status == False:
                self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightArrow1.png')
                self.weapon_w = character_w + 300
                self.x += character_dir * 1
        if up_status == True:
            self.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_UpArrow1.png')
            self.weapon_h = character_h + 300
            self.y += character_dir * 1


def handle_events():
    global running
    global run_status, sit_status, up_status, shot_status, move_w, move_tmp, character_w, character_h
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            running = False

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

        # 왼쪽 보며 대기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            run_status = False
            character.state = character.LEFT_STAND
            character.dir_x = 0

        # 오른쪽 보며 대기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            run_status = False
            character.state = character.RIGHT_STAND
            character.dir_x = 0

        # 왼쪽 보며 달리기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            run_status = True
            move_tmp = character.x
            character.state = character.LEFT_RUN
            character.dir_x = -1

        # 오른쪽 보며 달리기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            run_status = True
            move_tmp = character.x
            character.state = character.RIGHT_RUN
            character.dir_x = 1

        # 앉기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            sit_status = True

            # 왼쪽 보며 앉기
            if character.state == character.LEFT_STAND:
                character.state = character.LEFT_SIT
            # 오른쪽 보며 앉기
            elif character.state == character.RIGHT_STAND:
                character.state = character.RIGHT_SIT

        # 일어서기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            sit_status = False

            # 왼쪽 보며 대기
            if character.state == character.LEFT_SIT:
                character.state = character.LEFT_STAND
            # 오른쪽 보며 대기
            elif character.state == character.RIGHT_SIT:
                character.state = character.RIGHT_STAND

        # 위로 보기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            up_status = True

            # 왼쪽 방향 위로 보기
            if character.state == character.LEFT_STAND:
                character.state = character.LEFT_UP
            # 오른쪽 방향 위로 보기
            elif character.state == character.RIGHT_STAND:
                character.state = character.RIGHT_UP

        # 다시 정면 보기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            up_status = False

            # 왼쪽 보며 대기
            if character.state == character.LEFT_UP:
                character.state = character.LEFT_STAND
            # 오른쪽 보며 대기
            elif character.state == character.RIGHT_UP:
                character.state = character.RIGHT_STAND

        # 점프
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LALT):
            character.jump_y = character.y + 50

            # 왼쪽 보며 점프
            if character.state == character.LEFT_RUN or character.state == character.LEFT_STAND:
                character.state = character.LEFT_JUMP
                character.dir_y = 1
            # 오른쪽 보며 점프
            elif character.state == character.RIGHT_RUN or character.state == character.RIGHT_STAND:
                character.state = character.RIGHT_JUMP
                character.dir_y = 1

        # 사격 시작
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            shot_status = True
            character_w = character.x
            character_h = character.y

            # 왼쪽 방향 사격
            if character.state == character.LEFT_RUN or character.state == character.LEFT_STAND or  \
               character.state == character.LEFT_SIT or character.state == character.LEFT_UP or \
               character.state == character.LEFT_JUMP:
                character.state = character.LEFT_SHOT
            # 오른쪽 방향 사격
            elif character.state == character.RIGHT_RUN or character.state == character.RIGHT_STAND or \
                 character.state == character.RIGHT_SIT or character.state == character.RIGHT_UP or \
                 character.state == character.RIGHT_JUMP:
                character.state = character.RIGHT_SHOT

        # 사격 중지
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            shot_status = False

            if character.state == character.LEFT_SHOT:
                # 왼쪽 보며 앉기
                if sit_status == True:
                    character.state = character.LEFT_SIT
                # 왼쪽 방향 위로 보기
                elif up_status == True:
                    character.state = character.LEFT_UP
                # 왼쪽 보며 대기
                else:
                    character.state = character.LEFT_STAND

            elif character.state == character.RIGHT_SHOT:
                # 오른쪽 보며 앉기
                if sit_status == True:
                    character.state = character.RIGHT_SIT
                # 오른쪽 방향 위로 보기
                elif up_status == True:
                    character.state = character.RIGHT_UP
                # 오른쪽 보며 대기
                else:
                    character.state = character.RIGHT_STAND


# 초기화 작업
open_canvas(width, height)
background = Background()
road = Road()
gwroad = GWoodRoad()
gwbackground = GWoodBackground()
character = Character()
weapons = [Weapon() for i in range(5)]


# 게임 메인 루프
while running:
    clear_canvas()

    # 배경 이미지 화면 출력
    background.draw()

    # 스테이지 1 기본 지형 맵 화면 출력
    road.draw()

    # 스테이지 1 보스 Golem Wood 출현 맵 화면 출력 (애니메이션 미적용)
    for i in range(5):
        gwroad.draw(i)
    gwbackground.draw()

    character.update()
    character.draw()
    for weapon in weapons:
        weapon.draw()
        weapon.update()

    update_canvas()
    handle_events()
    delay(0.005)

# 게임 종료
close_canvas()
