import Game_Framework
import Main_State
from pico2d import *

# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672

name = "GameSelect_State"
background = None
font_gameselect = None
font_notice = None
selectbox_mw = None
selectbox_mw_x = 0
selectbox_ch = None
selectbox_ch_x = 336
selectbox_dp = None
selectbox_dp_x = 336
selectedgame = 1


def enter():
    global background, font_gameselect, font_notice, selectbox_mw, selectbox_ch, selectbox_dp
    background = load_image('Resources\Title\RedWindow.jpg')
    font_gameselect = load_image('Resources\Title\GameSelect.png')
    font_notice = load_image('Resources\Title\GameSelect_Notice1.png')
    selectbox_mw = load_image('Resources\Title\GameSelect_Box_MidnightWanderers.png')
    selectbox_ch = load_image('Resources\Title\GameSelect_Box_Chariot.png')
    selectbox_dp = load_image('Resources\Title\GameSelect_Box_DontPull.png')


def exit():
    global background, font_gameselect, font_notice, selectbox_mw, selectbox_ch, selectbox_dp
    del background
    del font_gameselect
    del font_notice
    del selectbox_mw
    del selectbox_ch
    del selectbox_dp


def update(frame_time):
    global selectedgame, selectbox_mw_x, selectbox_ch_x, selectbox_dp_x
    if selectedgame == 1:
        selectbox_mw_x = 0
        selectbox_ch_x = 336
        selectbox_dp_x = 336
    elif selectedgame == 2:
        selectbox_mw_x = 336
        selectbox_ch_x = 0
        selectbox_dp_x = 336
    elif selectedgame == 3:
        selectbox_mw_x = 336
        selectbox_ch_x = 336
        selectbox_dp_x = 0


def draw(frame_time):
    global background, font_gameselect, font_notice, selectbox_mw, selectbox_mw_x, selectbox_ch, selectbox_ch_x, selectbox_dp, selectbox_dp_x
    clear_canvas()
    background.draw(width / 2, height / 2)
    font_gameselect.draw(width / 2, height - 30)
    font_notice.draw(width / 2 - 30, 50)
    selectbox_mw.clip_draw(selectbox_mw_x, 0, 336, 480, 225, 350)
    selectbox_ch.clip_draw(selectbox_ch_x, 0, 336, 480, 575, 350)
    selectbox_dp.clip_draw(selectbox_dp_x, 0, 336, 480, width - 225, 350)

    update_canvas()


def handle_events(event):
    global selectedgame
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            Game_Framework.quit()

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            Game_Framework.quit()

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            Game_Framework.change_state(Main_State)

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if selectedgame == 2:
                selectedgame = 1
            elif selectedgame == 3:
                selectedgame = 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if selectedgame == 1:
                selectedgame = 2
            elif selectedgame == 2:
                selectedgame = 3

def pause():
    pass


def resume():
    pass
