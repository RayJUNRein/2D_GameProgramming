import Game_Framework
import Warning_State
import time
from pico2d import *

# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672


name = "Start_State"
background = None
font = None
sound_start = None
current_time = 0.0
logo_time = 0.0


def enter():
    global background, font, sound_start, current_time, logo_time
    open_canvas(width, height)
    background = load_image('Resources\Title\BlackWindow.jpg')
    font = load_image('Resources\Title\Logo.png')
    sound_start = load_wav('Sounds\Start.wav')
    sound_start.set_volume(30)
    sound_start.play(1)
    current_time = time.time()
    logo_time = current_time + 2.0


def exit():
    global font, background
    del font
    del background


def update(frame_time):
    global current_time, logo_time

    current_time = time.time()
    if current_time > logo_time:
        logo_time = 0
        Game_Framework.change_state(Warning_State)


def draw(frame_time):
    global current_time, logo_time, font, background

    clear_canvas()
    background.draw(width / 2, height / 2)

    if current_time < logo_time - 0.2:
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
