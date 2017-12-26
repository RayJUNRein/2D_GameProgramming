from pico2d import *
import random


class Enemy:
    enemy_data_file = open('Data\Enemy_Data.txt', 'r')
    enemy_data = json.load(enemy_data_file)
    enemy_data_file.close()


# 적군
class Goblin(Enemy):
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
    FRAMES_PER_ACTION = 6

    image = None

    def __init__(self):
        self.x, self.y = random.randint(600, 7000), 300
        self.canvas_width, self.canvas_height = get_canvas_width(), get_canvas_height()
        self.frame = 0
        self.total_frames = 0.0
        self.dir_x = 0
        self.dir_y = 0
        self.clip_width = 176
        self.clip_height = 156
        self.comeout = False
        self.is_dead = False
        self.dead_effect = False
        self.delete = False
        if Goblin.image == None:
            Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_LeftCreation.png')

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
        distance = Goblin.RUN_SPEED_PPS * frame_time
        self.x += self.dir_x * distance
        self.y += self.dir_y * distance

        if self.is_dead == True and self.dead_effect == False:
            if self.frame == 4:
                Goblin.FRAMES_PER_ACTION = Enemy.enemy_data['Goblin']['DeadEffect']['frames_per_action']
                self.clip_width = Enemy.enemy_data['Goblin']['DeadEffect']['clip_width']
                self.clip_height = Enemy.enemy_data['Goblin']['DeadEffect']['clip_height']

                if self.x > self.character.x:
                    Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_LeftDeadEffect.png')
                else:
                    Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_RightDeadEffect.png')

                self.dead_effect = True

        elif self.is_dead == False and self.dead_effect == False:
            if self.comeout == False:
                Goblin.FRAMES_PER_ACTION = Enemy.enemy_data['Goblin']['Creation']['frames_per_action']
                self.clip_width = Enemy.enemy_data['Goblin']['Creation']['clip_width']
                self.clip_height = Enemy.enemy_data['Goblin']['Creation']['clip_height']

                if self.x > self.character.x:
                    Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_LeftCreation.png')
                    self.dir_x = -1
                else:
                    Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_RightCreation.png')
                    self.dir_x = 1

                if self.frame == 5:
                    self.comeout = True

            else:
                Goblin.FRAMES_PER_ACTION = Enemy.enemy_data['Goblin']['Walk']['frames_per_action']
                self.clip_width = Enemy.enemy_data['Goblin']['Walk']['clip_width']
                self.clip_height = Enemy.enemy_data['Goblin']['Walk']['clip_height']

                if self.x > self.character.x:
                    Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_LeftWalk.png')
                    self.dir_x = -1
                elif self.x < self.character.x and self.character.x - self.x < 300 and self.character.y - self.x < 200:
                    Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_RightWalk.png')
                    self.dir_x = 1

        elif self.is_dead == True and self.dead_effect == True:
            if self.frame == 9:
                self.delete = True
                self.is_dead = False
                self.dead_effect = False
                self.dir_x = 0

        self.total_frames += Goblin.FRAMES_PER_ACTION * Goblin.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % Goblin.FRAMES_PER_ACTION

    def dead(self):
        Goblin.FRAMES_PER_ACTION = Enemy.enemy_data['Goblin']['Walk']['frames_per_action']
        self.clip_width = Enemy.enemy_data['Goblin']['Dead']['clip_width']
        self.clip_height = Enemy.enemy_data['Goblin']['Dead']['clip_height']

        self.is_dead = True

        if self.x > self.character.x:
            Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_LeftDead.png')
            self.dir_x = 1
        else:
            Goblin.image = load_image('Resources\Enemies\MidnightWanderers_Enemies_Goblin_RightDead.png')
            self.dir_x = -1
