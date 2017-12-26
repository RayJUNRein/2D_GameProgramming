import Game_Framework
import GameSelect_State
import time
from Font import Font as Font
from pico2d import *


name = "End_State"


# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672


background = None
fonts = []
current_time = 0.0
font_time = 0.0
sound_clear = None


def enter():
    global background, fonts, current_time, font_time, sound_clear
    background = load_image('Resources\Title\GameEnd.jpg')
    fonts = []
    current_time = time.time()
    font_time = current_time + 12.0
    sound_clear = load_music('Sounds\Music\ALL_ROUND_CLEAR.mp3')
    sound_clear.set_volume(40)
    sound_clear.play(1)


def exit():
    global background, fonts, sound_clear
    del background, fonts, sound_clear


def update(frame_time):
    global fonts, current_time, font_time

    current_time = time.time()

    font_data_file = open('Data\Font_Data.txt', 'r')
    font_data = json.load(font_data_file)
    font_data_file.close()

    if current_time < 0.1:
        font = Font()
        font.frame_x = font_data['Credit']['C']['x']
        font.frame_y = font_data['Credit']['C']['y']
        font.draw_width = font_data['Credit']['C']['w']
        font.draw_height = font_data['Credit']['C']['h']
        font.x = 100
        font.y = 100
        fonts.append(font)

    elif current_time < 0.2:
        font = Font()
        font.frame_x = font_data['Credit']['O']['x']
        font.frame_y = font_data['Credit']['O']['y']
        font.draw_width = font_data['Credit']['O']['w']
        font.draw_height = font_data['Credit']['O']['h']
        font.x = 125
        font.y = 100
        fonts.append(font)

    elif current_time < 0.3:
        font = Font()
        font.frame_x = font_data['Credit']['N']['x']
        font.frame_y = font_data['Credit']['N']['y']
        font.draw_width = font_data['Credit']['N']['w']
        font.draw_height = font_data['Credit']['N']['h']
        font.x = 150
        font.y = 100
        fonts.append(font)

    elif current_time < 0.4:
        font = Font()
        font.frame_x = font_data['Credit']['G']['x']
        font.frame_y = font_data['Credit']['G']['y']
        font.draw_width = font_data['Credit']['G']['w']
        font.draw_height = font_data['Credit']['G']['h']
        font.x = 175
        font.y = 100
        fonts.append(font)

    elif current_time < 0.5:
        font = Font()
        font.frame_x = font_data['Credit']['R']['x']
        font.frame_y = font_data['Credit']['R']['y']
        font.draw_width = font_data['Credit']['R']['w']
        font.draw_height = font_data['Credit']['R']['h']
        font.x = 200
        font.y = 100
        fonts.append(font)

    elif current_time < 0.6:
        font = Font()
        font.frame_x = font_data['Credit']['A']['x']
        font.frame_y = font_data['Credit']['A']['y']
        font.draw_width = font_data['Credit']['A']['w']
        font.draw_height = font_data['Credit']['A']['h']
        font.x = 225
        font.y = 100
        fonts.append(font)

    elif current_time < 0.7:
        font = Font()
        font.frame_x = font_data['Credit']['T']['x']
        font.frame_y = font_data['Credit']['T']['y']
        font.draw_width = font_data['Credit']['T']['w']
        font.draw_height = font_data['Credit']['T']['h']
        font.x = 250
        font.y = 100
        fonts.append(font)

    elif current_time < 0.8:
        font = Font()
        font.frame_x = font_data['Credit']['U']['x']
        font.frame_y = font_data['Credit']['U']['y']
        font.draw_width = font_data['Credit']['U']['w']
        font.draw_height = font_data['Credit']['U']['h']
        font.x = 275
        font.y = 100
        fonts.append(font)

    elif current_time < 0.9:
        font = Font()
        font.frame_x = font_data['Credit']['L']['x']
        font.frame_y = font_data['Credit']['L']['y']
        font.draw_width = font_data['Credit']['L']['w']
        font.draw_height = font_data['Credit']['L']['h']
        font.x = 300
        font.y = 100
        fonts.append(font)

    elif current_time < 1.0:
        font = Font()
        font.frame_x = font_data['Credit']['A']['x']
        font.frame_y = font_data['Credit']['A']['y']
        font.draw_width = font_data['Credit']['A']['w']
        font.draw_height = font_data['Credit']['A']['h']
        font.x = 325
        font.y = 100
        fonts.append(font)

    elif current_time < 1.1:
        font = Font()
        font.frame_x = font_data['Credit']['T']['x']
        font.frame_y = font_data['Credit']['T']['y']
        font.draw_width = font_data['Credit']['T']['w']
        font.draw_height = font_data['Credit']['T']['h']
        font.x = 350
        font.y = 100
        fonts.append(font)

    elif current_time < 1.2:
        font = Font()
        font.frame_x = font_data['Credit']['I']['x']
        font.frame_y = font_data['Credit']['I']['y']
        font.draw_width = font_data['Credit']['I']['w']
        font.draw_height = font_data['Credit']['I']['h']
        font.x = 375
        font.y = 100
        fonts.append(font)

    elif current_time < 1.3:
        font = Font()
        font.frame_x = font_data['Credit']['O']['x']
        font.frame_y = font_data['Credit']['O']['y']
        font.draw_width = font_data['Credit']['O']['w']
        font.draw_height = font_data['Credit']['O']['h']
        font.x = 400
        font.y = 100
        fonts.append(font)

    elif current_time < 1.4:
        font = Font()
        font.frame_x = font_data['Credit']['N']['x']
        font.frame_y = font_data['Credit']['N']['y']
        font.draw_width = font_data['Credit']['N']['w']
        font.draw_height = font_data['Credit']['N']['h']
        font.x = 425
        font.y = 100
        fonts.append(font)

    elif current_time < 1.5:
        font = Font()
        font.frame_x = font_data['Credit']['S']['x']
        font.frame_y = font_data['Credit']['S']['y']
        font.draw_width = font_data['Credit']['S']['w']
        font.draw_height = font_data['Credit']['S']['h']
        font.x = 450
        font.y = 100
        fonts.append(font)

    elif current_time < 1.6:
        font = Font()
        font.frame_x = font_data['Credit']['!']['x']
        font.frame_y = font_data['Credit']['!']['y']
        font.draw_width = font_data['Credit']['!']['w']
        font.draw_height = font_data['Credit']['!']['h']
        font.x = 475
        font.y = 100
        fonts.append(font)

    elif current_time > font_time:
        font_time = 0
        Game_Framework.change_state(GameSelect_State)


def draw(frame_time):
    global background, fonts

    clear_canvas()
    background.draw(width / 2, height / 2)

    for font in fonts:
        font.draw(frame_time)

    update_canvas()


def handle_events(frame_time):
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            close_canvas()
            Game_Framework.quit()

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            close_canvas()
            Game_Framework.quit()


def pause():
    pass


def resume():
    pass
