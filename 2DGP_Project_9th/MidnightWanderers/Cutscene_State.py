import Game_Framework
import Main_State
import time
from Font import Font as Font
from pico2d import *


name = "Cutscene_State"


# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672


background = None
bg_pub = None
character = None
fonts = []
current_time = 0.0
font_time = 0.0


def enter():
    global background, bg_pub, character, current_time, font_time
    background = load_image('Resources\Title\BlackWindow.jpg')
    bg_pub = load_image('Resources\Title\Cutscene_Background_Pub.png')
    character = load_image('Resources\Title\Cutscene_Character.png')
    current_time = time.time()
    font_time = current_time + 2.0


def exit():
    global background, bg_pub, character, fonts
    del background, bg_pub, character, fonts


def update(frame_time):
    global current_time, font_time

    current_time = time.time()

    font_data_file = open('Data\Font_Data.txt', 'r')
    font_data = json.load(font_data_file)
    font_data_file.close()

    if current_time < 0.1:
        font = Font()
        font.frame_x = font_data['Credit']['Quote']['x']
        font.frame_y = font_data['Credit']['Quote']['y']
        font.draw_width = font_data['Credit']['Quote']['w']
        font.draw_height = font_data['Credit']['Quote']['h']
        font.x = 100
        font.y = 100
        fonts.append(font)

    elif current_time < 0.2:
        font = Font()
        font.frame_x = font_data['Credit']['H']['x']
        font.frame_y = font_data['Credit']['H']['y']
        font.draw_width = font_data['Credit']['H']['w']
        font.draw_height = font_data['Credit']['H']['h']
        font.x = 125
        font.y = 100
        fonts.append(font)

    elif current_time > font_time:
        font_time = 0
        Game_Framework.change_state(Main_State)


def draw(frame_time):
    global background, bg_pub, character, fonts, status_ui

    clear_canvas()
    background.draw(width / 2, height / 2)
    bg_pub.draw(width / 2, height / 2)
    character.draw(width / 2, height / 2)

    for font in fonts:
        font.draw(frame_time)

    update_canvas()


def handle_events(frame_time):
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            Game_Framework.quit()

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            Game_Framework.quit()


def pause():
    pass


def resume():
    pass
