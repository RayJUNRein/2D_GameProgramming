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
font_credit = None
credit_x = 0
credit_y = 0
credit_w = 25
credit_h = 25
selectbox_mw = None
selectbox_mw_x = 0
selectbox_mw_background = None
selectbox_mw_background_x = 0
selectbox_mw_character = None
selectbox_mw_character_x = 0
selectbox_ch = None
selectbox_ch_x = 336
selectbox_dp = None
selectbox_dp_x = 336
selectedgame = 1
credit_num = 0
sound_music = None
sound_credit = None


def enter():
    global background, font_gameselect, font_notice, font_credit, selectbox_mw, selectbox_mw_background, selectbox_mw_character, selectbox_ch, selectbox_dp, sound_music, sound_credit
    background = load_image('Resources\Title\RedWindow.jpg')
    font_gameselect = load_image('Resources\Title\GameSelect.png')
    font_notice = load_image('Resources\Title\GameSelect_Notice.png')
    font_credit = load_image('Resources\Fonts\Font_Credit.png')
    selectbox_mw = load_image('Resources\Title\GameSelect_Box_MidnightWanderers.png')
    selectbox_mw_background = load_image('Resources\Title\GameSelect_Box_Background_MidnightWanderers.png')
    selectbox_mw_character = load_image('Resources\Title\GameSelect_Box_Character_MidnightWanderers.png')
    selectbox_ch = load_image('Resources\Title\GameSelect_Box_Chariot.png')
    selectbox_dp = load_image('Resources\Title\GameSelect_Box_DontPull.png')
    sound_music = load_music('Sounds\Music\GAME_SELECT.mp3')
    sound_music.set_volume(40)
    sound_music.repeat_play()
    sound_credit = load_wav('Sounds\Credit.wav')
    sound_credit.set_volume(30)


def exit():
    global background, font_gameselect, font_notice, font_credit, selectbox_mw, selectbox_mw_background, selectbox_mw_character, selectbox_ch, selectbox_dp, sound_credit
    del background
    del font_gameselect
    del font_notice
    del font_credit
    del selectbox_mw
    del selectbox_mw_background
    del selectbox_mw_character
    del selectbox_ch
    del selectbox_dp
    del sound_credit


def update(frame_time):
    global sound_music, selectedgame, selectbox_mw_x, selectbox_mw_background_x, selectbox_mw_character_x, selectbox_ch_x, selectbox_dp_x, credit_num
    if selectedgame == 1:
        selectbox_mw_x = 0
        selectbox_mw_background_x = 0
        selectbox_mw_character_x = 0
        selectbox_ch_x = 336
        selectbox_dp_x = 336
    elif selectedgame == 2:
        selectbox_mw_x = 336
        selectbox_mw_background_x = 336
        selectbox_mw_character_x = 297
        selectbox_ch_x = 0
        selectbox_dp_x = 336
    elif selectedgame == 3:
        selectbox_mw_x = 336
        selectbox_mw_background_x = 336
        selectbox_mw_character_x = 297
        selectbox_ch_x = 336
        selectbox_dp_x = 0

    elif selectedgame == 0:
        sound_music.stop()
        Game_Framework.change_state(Main_State)

    credit_num = clamp(0, credit_num, 9)


def draw(frame_time):
    global selectedgame, background, font_gameselect, font_notice, selectbox_mw, selectbox_mw_x, selectbox_mw_background, selectbox_mw_background_x, selectbox_mw_character, selectbox_mw_character_x, selectbox_ch, selectbox_ch_x, selectbox_dp, selectbox_dp_x

    font_data_file = open('Data\Font_Data.txt', 'r')
    font_data = json.load(font_data_file)
    font_data_file.close()

    clear_canvas()
    background.draw(width / 2, height / 2)
    font_gameselect.draw(width / 2, height - 25)
    font_notice.draw(width / 2 - 40, 80)


    credit_w = font_data['Credit']['C']['w']
    credit_h = font_data['Credit']['C']['h']
    credit_x = font_data['Credit']['C']['x'] * credit_w
    credit_y = font_data['Credit']['C']['y'] * credit_h
    font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 275, 10)

    credit_w = font_data['Credit']['R']['w']
    credit_h = font_data['Credit']['R']['h']
    credit_x = font_data['Credit']['R']['x'] * credit_w
    credit_y = font_data['Credit']['R']['y'] * credit_h
    font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 250, 10)

    credit_w = font_data['Credit']['E']['w']
    credit_h = font_data['Credit']['E']['h']
    credit_x = font_data['Credit']['E']['x'] * credit_w
    credit_y = font_data['Credit']['E']['y'] * credit_h
    font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 225, 10)

    credit_w = font_data['Credit']['D']['w']
    credit_h = font_data['Credit']['D']['h']
    credit_x = font_data['Credit']['D']['x'] * credit_w
    credit_y = font_data['Credit']['D']['y'] * credit_h
    font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 200, 10)

    credit_w = font_data['Credit']['I']['w']
    credit_h = font_data['Credit']['I']['h']
    credit_x = font_data['Credit']['I']['x'] * credit_w
    credit_y = font_data['Credit']['I']['y'] * credit_h
    font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 175, 10)

    credit_w = font_data['Credit']['T']['w']
    credit_h = font_data['Credit']['T']['h']
    credit_x = font_data['Credit']['T']['x'] * credit_w
    credit_y = font_data['Credit']['T']['y'] * credit_h
    font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 150, 10)

    if credit_num == 0:
        credit_w = font_data['Credit']['0']['w']
        credit_h = font_data['Credit']['0']['h']
        credit_x = font_data['Credit']['0']['x'] * credit_w
        credit_y = font_data['Credit']['0']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 1:
        credit_w = font_data['Credit']['1']['w']
        credit_h = font_data['Credit']['1']['h']
        credit_x = font_data['Credit']['1']['x'] * credit_w
        credit_y = font_data['Credit']['1']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 2:
        credit_w = font_data['Credit']['2']['w']
        credit_h = font_data['Credit']['2']['h']
        credit_x = font_data['Credit']['2']['x'] * credit_w
        credit_y = font_data['Credit']['2']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 3:
        credit_w = font_data['Credit']['3']['w']
        credit_h = font_data['Credit']['3']['h']
        credit_x = font_data['Credit']['3']['x'] * credit_w
        credit_y = font_data['Credit']['3']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 4:
        credit_w = font_data['Credit']['4']['w']
        credit_h = font_data['Credit']['4']['h']
        credit_x = font_data['Credit']['4']['x'] * credit_w
        credit_y = font_data['Credit']['4']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 5:
        credit_w = font_data['Credit']['5']['w']
        credit_h = font_data['Credit']['5']['h']
        credit_x = font_data['Credit']['5']['x'] * credit_w
        credit_y = font_data['Credit']['5']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 6:
        credit_w = font_data['Credit']['6']['w']
        credit_h = font_data['Credit']['6']['h']
        credit_x = font_data['Credit']['6']['x'] * credit_w
        credit_y = font_data['Credit']['6']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 7:
        credit_w = font_data['Credit']['7']['w']
        credit_h = font_data['Credit']['7']['h']
        credit_x = font_data['Credit']['7']['x'] * credit_w
        credit_y = font_data['Credit']['7']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 8:
        credit_w = font_data['Credit']['8']['w']
        credit_h = font_data['Credit']['8']['h']
        credit_x = font_data['Credit']['8']['x'] * credit_w
        credit_y = font_data['Credit']['8']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)

    elif credit_num == 9:
        credit_w = font_data['Credit']['9']['w']
        credit_h = font_data['Credit']['9']['h']
        credit_x = font_data['Credit']['9']['x'] * credit_w
        credit_y = font_data['Credit']['9']['y'] * credit_h
        font_credit.clip_draw(credit_x, credit_y, credit_w, credit_h, width - 100, 10)


    selectbox_mw_background.clip_draw(selectbox_mw_background_x, 0, 336, 384, 215, 335)
    selectbox_mw_character.clip_draw(selectbox_mw_character_x, 0, 297, 210, 215, 275)
    selectbox_mw.clip_draw(selectbox_mw_x, 0, 336, 480, 215, 380)
    selectbox_ch.clip_draw(selectbox_ch_x, 0, 336, 480, width / 2, 380)
    selectbox_dp.clip_draw(selectbox_dp_x, 0, 336, 480, width - 215, 380)

    update_canvas()

    if selectedgame == 4:
        delay(2.0)
        selectedgame = 0


def handle_events(frame_time):
    global selectedgame, selectbox_mw_character_x, credit_num, sound_credit
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            Game_Framework.quit()

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            Game_Framework.quit()

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LCTRL):
            if selectedgame == 1:
                selectbox_mw_character_x = 594
                selectedgame = 4

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

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_9):
            credit_num += 1
            sound_credit.play(1)


def pause():
    pass


def resume():
    pass
