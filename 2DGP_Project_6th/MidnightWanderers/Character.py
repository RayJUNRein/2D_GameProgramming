from pico2d import *

class Character:
    speed_data_file = open('Data\Speed_Data.txt', 'r')
    speed_data = json.load(speed_data_file)
    speed_data_file.close()


    # 1 pixel = 1 cm / 10 pixel = 0.1 m
    PIXEL_PER_METER = (10.0 / 0.1)
    # Running Speed = 12 km/h
    RUN_SPEED_KMPH = speed_data['Character']['speed']
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = speed_data['Character']['time']
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    # 왼쪽 보며 대기
    def handle_left_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftStand.png')

    # 오른쪽 보며 대기
    def handle_right_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightStand.png')

    # 왼쪽 보며 달리기
    def handle_left_run(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftRun.png')

    # 오른쪽 보며 달리기
    def handle_right_run(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightRun.png')

    # 왼쪽 보며 앉기
    def handle_left_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftSit.png')

    # 오른쪽 보며 앉기
    def handle_right_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightSit.png')

    # 왼쪽 방향 위로 보기
    def handle_left_lookup(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftLookup.png')

    # 오른쪽 방향 위로 보기
    def handle_right_lookup(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightLookup.png')

    # 왼쪽 보며 점프
    def handle_left_jump(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftJump.png')

    # 오른쪽 보며 점프
    def handle_right_jump(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightJump.png')


    # 왼쪽 보며 서있는 상태 사격
    def handle_left_shot_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftShot.png')

    # 오른쪽 보며 서있는 상태 사격
    def handle_right_shot_stand(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightShot.png')

    # 왼쪽 보며 앉아서 사격
    def handle_left_shot_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftSit.png')

    # 오른쪽 보며 앉아서 사격
    def handle_right_shot_sit(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightSit.png')

    # 왼쪽 방향 위로 보며 사격
    def handle_left_shot_lookup(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_LeftUp.png')

    # 오른쪽 방향 위로 보며 사격
    def handle_right_shot_lookup(self):
        Character.image = load_image('Resources\Character\Lou\MidnightWanderers_Character_Lou(Clothed)_RightUp.png')


    # Character Action State
    LEFT_STAND, RIGHT_STAND, LEFT_RUN, RIGHT_RUN, LEFT_SIT, RIGHT_SIT, LEFT_LOOKUP, RIGHT_LOOKUP, LEFT_JUMP, RIGHT_JUMP,\
    LEFT_SHOT_STAND, RIGHT_SHOT_STAND, LEFT_SHOT_SIT, RIGHT_SHOT_SIT, LEFT_SHOT_LOOKUP, RIGHT_SHOT_LOOKUP\
    = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

    # 주인공 액션 상태에 따라 실행할 함수 구분
    handle_state = {
        LEFT_STAND:         handle_left_stand,
        RIGHT_STAND:        handle_right_stand,
        LEFT_RUN:           handle_left_run,
        RIGHT_RUN:          handle_right_run,
        LEFT_SIT:           handle_left_sit,
        RIGHT_SIT:          handle_right_sit,
        LEFT_LOOKUP:        handle_left_lookup,
        RIGHT_LOOKUP:       handle_right_lookup,
        LEFT_JUMP:          handle_left_jump,
        RIGHT_JUMP:         handle_right_jump,
        LEFT_SHOT_STAND:    handle_left_shot_stand,
        RIGHT_SHOT_STAND:   handle_right_shot_stand,
        LEFT_SHOT_SIT:      handle_left_shot_sit,
        RIGHT_SHOT_SIT:     handle_right_shot_sit,
        LEFT_SHOT_LOOKUP:   handle_left_shot_lookup,
        RIGHT_SHOT_LOOKUP:  handle_right_shot_lookup
    }

    def __init__(self):
        self.x, self.y = 200, 200
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir_x = 0
        self.dir_y = 0
        self.jump_move = 200
        self.jump_y = 0
        self.state = self.RIGHT_STAND
        self.clip_width = 156
        self.clip_height = 123
        # 달리는 상태인지 알려주는 변수 선언 (True = 달리는 상태)
        self.run_status = False
        # 앉은 상태인지 알려주는 변수 선언 (True = 앉은 상태)
        self.sit_status = False
        # 위를 보는 상태인지 알려주는 변수 선언 (True = 위를 보는 상태)
        self.up_status = False
        # 사격하는 상태인지 알려주는 변수 선언 (True = 사격하는 상태)
        self.shot_status = False
        # 점프하는 상태인지 알려주는 변수 선언 (True = 점프하는 상태)
        self.jump_status = False
        self.fall_status = False

    def set_road(self, road):
        self.road = road

    def set_weapon(self, weapon):
        self.weapon = weapon

    def update(self, frame_time):
        character_data_file = open('Data\Character_Data.txt', 'r')
        character_data = json.load(character_data_file)
        character_data_file.close()

        self.life_time += frame_time
        distance = Character.RUN_SPEED_PPS * frame_time
        self.x += self.dir_x * distance
        self.y += self.dir_y * distance

        if self.state == self.LEFT_STAND:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_STAND']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_STAND']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_STAND']['clip_height']
        elif self.state == self.RIGHT_RUN:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_RUN']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_RUN']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_RUN']['clip_height']
        elif self.state == self.LEFT_RUN:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_RUN']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_RUN']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_RUN']['clip_height']
        elif self.state == self.RIGHT_RUN:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_RUN']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_RUN']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_RUN']['clip_height']
        elif self.state == self.LEFT_SIT:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_SIT']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_SIT']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_SIT']['clip_height']
        elif self.state == self.RIGHT_SIT:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_SIT']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_SIT']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_SIT']['clip_height']
        elif self.state == self.LEFT_LOOKUP:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_LOOKUP']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_LOOKUP']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_LOOKUP']['clip_height']
        elif self.state == self.RIGHT_LOOKUP:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_LOOKUP']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_LOOKUP']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_LOOKUP']['clip_height']
        elif self.state == self.LEFT_JUMP:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_JUMP']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_JUMP']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_JUMP']['clip_height']
        elif self.state == self.RIGHT_JUMP:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_JUMP']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_JUMP']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_JUMP']['clip_height']
        elif self.state == self.LEFT_SHOT_STAND:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_SHOT_STAND']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_SHOT_STAND']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_SHOT_STAND']['clip_height']
        elif self.state == self.RIGHT_SHOT_STAND:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_SHOT_STAND']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_SHOT_STAND']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_SHOT_STAND']['clip_height']
        elif self.state == self.LEFT_SHOT_SIT:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_SHOT_SIT']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_SHOT_SIT']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_SHOT_SIT']['clip_height']
        elif self.state == self.RIGHT_SHOT_SIT:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_SHOT_SIT']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_SHOT_SIT']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_SHOT_SIT']['clip_height']
        elif self.state == self.LEFT_SHOT_LOOKUP:
            Character.FRAMES_PER_ACTION = character_data['Lou']['LEFT_SHOT_LOOKUP']['frames_per_action']
            self.clip_width = character_data['Lou']['LEFT_SHOT_LOOKUP']['clip_width']
            self.clip_height = character_data['Lou']['LEFT_SHOT_LOOKUP']['clip_height']
        elif self.state == self.RIGHT_SHOT_LOOKUP:
            Character.FRAMES_PER_ACTION = character_data['Lou']['RIGHT_SHOT_LOOKUP']['frames_per_action']
            self.clip_width = character_data['Lou']['RIGHT_SHOT_LOOKUP']['clip_width']
            self.clip_height = character_data['Lou']['RIGHT_SHOT_LOOKUP']['clip_height']


        self.total_frames += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % Character.FRAMES_PER_ACTION
        self.handle_state[self.state](self)

        # 주인공이 화면 밖으로 나가는 것을 방지
        self.x = clamp(30, self.x, self.road.w - 30)
        self.y = clamp(50, self.y, self.canvas_height - 50)

        self.x, self.y = self.x, self.y

        # 점프 뒤 하강
        if self.jump_status == True:
            if self.y < self.jump_y:
                self.dir_y = 1
            elif self.y > self.jump_y:
                self.dir_y = -1
                self.jump_y -= self.jump_move
                self.fall_status = True
                self.jump_status = False

        if self.fall_status == True:
            if self.y < self.jump_y:
                self.dir_y = 0
                self.fall_status = False
                if self.state == self.RIGHT_JUMP:
                    self.state = self.RIGHT_STAND
                elif self.state == self.LEFT_JUMP:
                    self.state = self.LEFT_STAND

    def draw(self):
        self.image.clip_draw(self.frame * self.clip_width, 0, self.clip_width, self.clip_height, self.x - self.road.window_left, self.y - self.road.window_bottom)

    def get_bb(self):
        return self.x - self.clip_width / 2 - self.road.window_left, self.y - self.clip_height / 2 - self.road.window_bottom, self.x + self.clip_width / 2 - self.road.window_left, self.y + self.clip_height / 2 - self.road.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        # 왼쪽 보며 대기
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.run_status = False
            self.state = self.LEFT_STAND
            self.dir_x = 0

        # 오른쪽 보며 대기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.run_status = False
            self.state = self.RIGHT_STAND
            self.dir_x = 0

        # 왼쪽 보며 달리기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.run_status = True
            self.state = self.LEFT_RUN
            self.dir_x = -1

        # 오른쪽 보며 달리기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.run_status = True
            self.state = self.RIGHT_RUN
            self.dir_x = 1

        # 앉기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.sit_status = True

            # 왼쪽 보며 앉기
            if self.state == self.LEFT_STAND:
                self.state = self.LEFT_SIT
            # 오른쪽 보며 앉기
            elif self.state == self.RIGHT_STAND:
                self.state = self.RIGHT_SIT

        # 일어서기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.sit_status = False

            # 왼쪽 보며 대기
            if self.state == self.LEFT_SIT:
                self.state = self.LEFT_STAND
            # 오른쪽 보며 대기
            elif self.state == self.RIGHT_SIT:
                self.state = self.RIGHT_STAND

        # 위로 보기
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.up_status = True

            # 왼쪽 방향 위로 보기
            if self.state == self.LEFT_STAND:
                self.state = self.LEFT_LOOKUP
            # 오른쪽 방향 위로 보기
            elif self.state == self.RIGHT_STAND:
                self.state = self.RIGHT_LOOKUP

        # 다시 정면 보기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.up_status = False

            # 왼쪽 보며 대기
            if self.state == self.LEFT_LOOKUP:
                self.state = self.LEFT_STAND
            # 오른쪽 보며 대기
            elif self.state == self.RIGHT_LOOKUP:
                self.state = self.RIGHT_STAND

        # 점프
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LALT):
            self.jump_status = True
            self.jump_y = self.y + self.jump_move

            # 왼쪽 보며 점프
            if self.state == self.LEFT_RUN or self.state == self.LEFT_STAND:
                self.state = self.LEFT_JUMP
            # 오른쪽 보며 점프
            elif self.state == self.RIGHT_RUN or self.state == self.RIGHT_STAND:
                self.state = self.RIGHT_JUMP

        # 사격 시작
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            self.shot_status = True

            # 왼쪽 방향 사격
            if self.state == self.LEFT_STAND or self.state == self.LEFT_RUN or self.state == self.LEFT_JUMP:
                self.state = self.LEFT_SHOT_STAND
            elif self.state == self.LEFT_SIT:
                self.state = self.LEFT_SHOT_SIT
            elif self.state == self.LEFT_LOOKUP:
                self.state = self.LEFT_SHOT_LOOKUP

            # 오른쪽 방향 사격
            if self.state == self.RIGHT_STAND or self.state == self.RIGHT_RUN or self.state == self.RIGHT_JUMP:
                self.state = self.RIGHT_SHOT_STAND
            elif self.state == self.RIGHT_SIT:
                self.state = self.RIGHT_SHOT_SIT
            elif self.state == self.RIGHT_LOOKUP:
                self.state = self.RIGHT_SHOT_LOOKUP

        # 사격 중지
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            if self.state == self.LEFT_SHOT_STAND:
                # 왼쪽 보며 대기
                self.state = self.LEFT_STAND
            elif self.state == self.LEFT_SHOT_SIT:
                # 왼쪽 보며 앉기
                self.state = self.LEFT_SIT
            elif self.state == self.LEFT_SHOT_LOOKUP:
                # 왼쪽 방향 위로 보기
                self.state = self.LEFT_LOOKUP

            if self.state == self.RIGHT_SHOT_STAND:
                # 오른쪽 보며 대기
                self.state = self.RIGHT_STAND
            elif self.state == self.RIGHT_SHOT_SIT:
                # 오른쪽 보며 앉기
                self.state = self.RIGHT_SIT
            elif self.state == self.RIGHT_SHOT_LOOKUP:
                # 오른쪽 방향 위로 보기
                self.state = self.RIGHT_LOOKUP
