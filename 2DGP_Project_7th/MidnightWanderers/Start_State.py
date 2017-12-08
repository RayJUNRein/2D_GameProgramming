import Game_Framework
import Warning_State
from pico2d import *

# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672

name = "Start_State"
background = None
font = None
logo_time = 0.0


def enter():
    global background, font
    open_canvas(width, height)
    background = load_image('Resources\Title\BlackWindow.jpg')
    font = load_image('Resources\Title\Logo.png')


def exit():
    global font, background
    del font
    del background


def update(frame_time):
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        Game_Framework.change_state(Warning_State)
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global logo_time, font, background
    clear_canvas()
    background.draw(width / 2, height / 2)
    if logo_time < 0.9:
        font.draw(width / 2, height / 2)
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
