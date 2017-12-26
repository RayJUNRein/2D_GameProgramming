from pico2d import *

import Game_Framework
import GameStart_State
import Main_State
import time

from Credit import Credit as Credit


name = "GameSelect_State"


# 플레이 화면 크기 지정 (가로 1152 x 세로 672 pixel)
width = 1152
height = 672


gameselect_data_file = open('Data\GameSelect_Data.txt', 'r')
gameselect_data = json.load(gameselect_data_file)
gameselect_data_file.close()


background = None
font_gameselect = None
font_notice = None
font_credit = None
sbox_mw = None
sbox_mw_x, sbox_mw_w, sbox_mw_h = 0, 0, 0
sbox_mw_bg = None
sbox_mw_bg_x, sbox_mw_bg_w, sbox_mw_bg_h = 0, 0, 0
sbox_mw_character = None
sbox_mw_character_x, sbox_mw_character_w, sbox_mw_character_h = 0, 0, 0
sbox_ch = None
sbox_ch_x, sbox_ch_w, sbox_ch_h = 0, 0, 0
sbox_ch_bg1 = None
sbox_ch_bg1_x, sbox_ch_bg1_w, sbox_ch_bg1_h = 0, 0, 0
sbox_ch_bg2 = None
sbox_ch_bg2_x, sbox_ch_bg2_w, sbox_ch_bg2_h = 0, 0, 0
sbox_ch_character = None
sbox_ch_character_x, sbox_ch_character_w, sbox_ch_character_h = 0, 0, 0
sbox_dp = None
sbox_dp_x, sbox_dp_w, sbox_dp_h = 0, 0, 0
sbox_dp_bg = None
sbox_dp_bg_x, sbox_dp_bg_w, sbox_dp_bg_h = 0, 0, 0
sbox_dp_selected = None
sbox_dp_selected_x, sbox_dp_selected_w, sbox_dp_selected_h = 0, 0, 0
selectedgame = 1
credit_num = 0
sound_music = None
sound_credit = None
sound_select = None
current_time = 0.0
delay_time = 0.0


def enter():
    global background, font_gameselect, font_notice, font_credit, gameselect_data, sound_music, sound_credit, sound_select,\
           sbox_mw, sbox_mw_w, sbox_mw_h, sbox_mw_bg, sbox_mw_bg_w, sbox_mw_bg_h, sbox_mw_character, sbox_mw_character_w, sbox_mw_character_h,\
           sbox_ch, sbox_ch_w, sbox_ch_h, sbox_ch_bg1, sbox_ch_bg1_w, sbox_ch_bg1_h, sbox_ch_bg2, sbox_ch_bg2_w, sbox_ch_bg2_h, sbox_ch_character, sbox_ch_character_w, sbox_ch_character_h,\
           sbox_dp, sbox_dp_w, sbox_dp_h, sbox_dp_bg, sbox_dp_bg_w, sbox_dp_bg_h, sbox_dp_selected, sbox_dp_selected_w, sbox_dp_selected_h,\
           selectedgame

    selectedgame = 1
    background = load_image('Resources\Title\RedWindow.jpg')
    font_gameselect = load_image('Resources\Title\GameSelect.png')
    font_notice = load_image('Resources\Title\GameSelect_Notice.png')
    font_credit = Credit()

    sound_music = load_music('Sounds\Music\GAME_SELECT.mp3')
    sound_music.set_volume(40)
    sound_music.repeat_play()
    sound_credit = load_wav('Sounds\Credit.wav')
    sound_credit.set_volume(60)
    sound_select = load_wav('Sounds\GameSelect.wav')
    sound_select.set_volume(40)

    sbox_mw = load_image('Resources\Title\GameSelect_Box_MidnightWanderers.png')
    sbox_mw_w, sbox_mw_h = gameselect_data['SBox']['MW']['Box']['w'], gameselect_data['SBox']['MW']['Box']['h']
    sbox_mw_bg = load_image('Resources\Title\GameSelect_Box_Background_MidnightWanderers.png')
    sbox_mw_bg_w, sbox_mw_bg_h = gameselect_data['SBox']['MW']['BG']['w'], gameselect_data['SBox']['MW']['BG']['h']
    sbox_mw_character = load_image('Resources\Title\GameSelect_Box_Character_MidnightWanderers.png')
    sbox_mw_character_w, sbox_mw_character_h = gameselect_data['SBox']['MW']['Character']['w'], gameselect_data['SBox']['MW']['Character']['h']
    sbox_ch = load_image('Resources\Title\GameSelect_Box_Chariot.png')
    sbox_ch_w, sbox_ch_h = gameselect_data['SBox']['CH']['Box']['w'], gameselect_data['SBox']['CH']['Box']['h']
    sbox_ch_bg1 = load_image('Resources\Title\GameSelect_Box_Background_Chariot1.png')
    sbox_ch_bg1_w, sbox_ch_bg1_h = gameselect_data['SBox']['CH']['BG1']['w'], gameselect_data['SBox']['CH']['BG1']['h']
    sbox_ch_bg2 = load_image('Resources\Title\GameSelect_Box_Background_Chariot2.png')
    sbox_ch_bg2_w, sbox_ch_bg2_h = gameselect_data['SBox']['CH']['BG2']['w'], gameselect_data['SBox']['CH']['BG2']['h']
    sbox_ch_character = load_image('Resources\Title\GameSelect_Box_Character_Chariot.png')
    sbox_ch_character_w, sbox_ch_character_h = gameselect_data['SBox']['CH']['Character']['w'], gameselect_data['SBox']['CH']['Character']['h']
    sbox_dp = load_image('Resources\Title\GameSelect_Box_DontPull.png')
    sbox_dp_w, sbox_dp_h = gameselect_data['SBox']['DP']['Box']['w'], gameselect_data['SBox']['DP']['Box']['h']
    sbox_dp_bg = load_image('Resources\Title\GameSelect_Box_Background_DontPull.png')
    sbox_dp_bg_w, sbox_dp_bg_h = gameselect_data['SBox']['DP']['BG']['w'], gameselect_data['SBox']['DP']['BG']['h']
    sbox_dp_selected = load_image('Resources\Title\GameSelect_Box_Selected_DontPull.png')
    sbox_dp_selected_w, sbox_dp_selected_h = gameselect_data['SBox']['DP']['Selected']['w'], gameselect_data['SBox']['DP']['Selected']['h']


def exit():
    global background, font_gameselect, font_notice, font_credit, sbox_mw, sbox_mw_bg, sbox_mw_character, \
           sbox_ch, sbox_ch_bg1, sbox_ch_bg2, sbox_ch_character, sbox_dp, sbox_dp_bg, sbox_dp_selected, sound_music, sound_credit
    del background
    del font_gameselect, font_notice, font_credit
    del sbox_mw, sbox_mw_bg, sbox_mw_character
    del sbox_ch, sbox_ch_bg1, sbox_ch_bg2, sbox_ch_character
    del sbox_dp, sbox_dp_bg, sbox_dp_selected
    del sound_music, sound_credit


def update(frame_time):
    global sound_music, selectedgame, credit_num, current_time, delay_time, font_credit,\
           sbox_mw_x, sbox_mw_w, sbox_mw_bg_x, sbox_mw_bg_w, sbox_mw_character_x, sbox_mw_character_w,\
           sbox_ch_x, sbox_ch_w, sbox_ch_bg1_x, sbox_ch_bg1_w, sbox_ch_bg2_x, sbox_ch_bg2_w, sbox_ch_character_x, sbox_ch_character_w,\
           sbox_dp_x, sbox_dp_w, sbox_dp_bg_x, sbox_dp_bg_w, sbox_dp_selected_x, sbox_dp_selected_w

    current_time = time.time()

    font_credit.update(frame_time, credit_num)

    if selectedgame == 1:
        sbox_mw_x = sbox_mw_w * 0
        sbox_mw_bg_x = sbox_mw_bg_w * 0
        sbox_mw_character_x = sbox_mw_character_w * 0
        sbox_ch_x = sbox_ch_w * 1
        sbox_ch_bg1_x = sbox_ch_bg1_w * 1
        sbox_ch_bg2_x = sbox_ch_bg2_w * 1
        sbox_ch_character_x = sbox_ch_character_w * 1
        sbox_dp_x = sbox_dp_w * 1
        sbox_dp_bg_x = sbox_dp_bg_w * 1
    elif selectedgame == 2:
        sbox_mw_x = sbox_mw_w * 1
        sbox_mw_bg_x = sbox_mw_bg_w * 1
        sbox_mw_character_x = sbox_mw_character_w * 1
        sbox_ch_x = sbox_ch_w * 0
        sbox_ch_bg1_x = sbox_ch_bg1_w * 0
        sbox_ch_bg2_x = sbox_ch_bg2_w * 0
        sbox_ch_character_x = sbox_ch_character_w * 0
        sbox_dp_x = sbox_dp_w * 1
        sbox_dp_bg_x = sbox_dp_bg_w * 1
    elif selectedgame == 3:
        sbox_mw_x = sbox_mw_w * 1
        sbox_mw_bg_x = sbox_mw_bg_w * 1
        sbox_mw_character_x = sbox_mw_character_w * 1
        sbox_ch_x = sbox_ch_w * 1
        sbox_ch_bg1_x = sbox_ch_bg1_w * 1
        sbox_ch_bg2_x = sbox_ch_bg2_w * 1
        sbox_ch_character_x = sbox_ch_character_w * 1
        sbox_dp_x = sbox_dp_w * 0
        sbox_dp_bg_x = sbox_dp_bg_w * 0
        sbox_dp_selected_x = sbox_dp_selected_w * 0
    elif selectedgame == 4:
        if current_time < delay_time - 0.8:
            sbox_mw_x = sbox_mw_w * 1
        elif current_time < delay_time - 0.5:
            sbox_mw_x = sbox_mw_w * 0
        elif current_time < delay_time - 0.2:
            sbox_mw_x = sbox_mw_w * 1
        elif current_time < delay_time:
            sbox_mw_x = sbox_mw_w * 0
            selectedgame = 0
    elif selectedgame == 5:
        if current_time < delay_time - 0.8:
            sbox_ch_x = sbox_ch_w * 1
        elif current_time < delay_time - 0.5:
            sbox_ch_x = sbox_ch_w * 0
        elif current_time < delay_time - 0.2:
            sbox_ch_x = sbox_ch_w * 1
        elif current_time < delay_time:
            sbox_ch_x = sbox_ch_w * 0
            selectedgame = 0
    elif selectedgame == 6:
        if current_time < delay_time - 0.8:
            sbox_dp_x = sbox_dp_w * 1
        elif current_time < delay_time - 0.5:
            sbox_dp_x = sbox_dp_w * 0
        elif current_time < delay_time - 0.2:
            sbox_dp_selected_x = sbox_dp_selected_w * 1
            sbox_dp_x = sbox_dp_w * 1
        elif current_time < delay_time:
            sbox_dp_x = sbox_dp_w * 0
            selectedgame = 0
    elif selectedgame == 0:
        Main_State.credit_num = credit_num - 1
        Game_Framework.change_state(GameStart_State)


def draw(frame_time):
    global background, font_gameselect, font_notice, selectedgame, gameselect_data,\
           sbox_mw, sbox_mw_x, sbox_mw_bg, sbox_mw_bg_x, sbox_mw_character, sbox_mw_character_x, sbox_ch, sbox_ch_x,\
           sbox_dp, sbox_dp_x, sbox_dp_bg, sbox_dp_bg_x, sbox_dp_selected, sbox_dp_selected_x

    clear_canvas()
    background.draw(width / 2, height / 2)
    font_gameselect.draw(width / 2, height - 25)
    font_notice.draw(width / 2 - 40, 90)
    font_credit.draw(frame_time)

    sbox_mw_draw_x, sbox_mw_draw_y = gameselect_data['SBox']['MW']['Box']['x'], gameselect_data['SBox']['MW']['Box']['y']
    sbox_mw_bg_draw_x, sbox_mw_bg_draw_y = gameselect_data['SBox']['MW']['BG']['x'], gameselect_data['SBox']['MW']['BG']['y']
    sbox_mw_character_draw_x, sbox_mw_character_draw_y = gameselect_data['SBox']['MW']['Character']['x'], gameselect_data['SBox']['MW']['Character']['y']
    sbox_mw_bg.clip_draw(sbox_mw_bg_x, 0, sbox_mw_bg_w, sbox_mw_bg_h, sbox_mw_bg_draw_x, sbox_mw_bg_draw_y)
    sbox_mw_character.clip_draw(sbox_mw_character_x, 0, sbox_mw_character_w, sbox_mw_character_h, sbox_mw_character_draw_x, sbox_mw_character_draw_y)
    sbox_mw.clip_draw(sbox_mw_x, 0, sbox_mw_w, sbox_mw_h, sbox_mw_draw_x, sbox_mw_draw_y)

    sbox_ch_draw_x, sbox_ch_draw_y = gameselect_data['SBox']['CH']['Box']['x'], gameselect_data['SBox']['CH']['Box']['y']
    sbox_ch_bg1_draw_x, sbox_ch_bg1_draw_y = gameselect_data['SBox']['CH']['BG1']['x'], gameselect_data['SBox']['CH']['BG1']['y']
    sbox_ch_bg2_draw_x, sbox_ch_bg2_draw_y = gameselect_data['SBox']['CH']['BG2']['x'], gameselect_data['SBox']['CH']['BG2']['y']
    sbox_ch_character_draw_x, sbox_ch_character_draw_y = gameselect_data['SBox']['CH']['Character']['x'], gameselect_data['SBox']['CH']['Character']['y']
    sbox_ch_bg1.clip_draw(sbox_ch_bg1_x, 0, sbox_ch_bg1_w, sbox_ch_bg1_h, sbox_ch_bg1_draw_x, sbox_ch_bg1_draw_y)
    sbox_ch_bg2.clip_draw(sbox_ch_bg2_x, 0, sbox_ch_bg2_w, sbox_ch_bg2_h, sbox_ch_bg2_draw_x, sbox_ch_bg2_draw_y)
    sbox_ch_character.clip_draw(sbox_ch_character_x, 0, sbox_ch_character_w, sbox_ch_character_h, sbox_ch_character_draw_x, sbox_ch_character_draw_y)
    sbox_ch.clip_draw(sbox_ch_x, 0, sbox_ch_w, sbox_ch_h, sbox_ch_draw_x, sbox_ch_draw_y)

    sbox_dp_draw_x, sbox_dp_draw_y = gameselect_data['SBox']['DP']['Box']['x'], gameselect_data['SBox']['DP']['Box']['y']
    sbox_dp_bg_draw_x, sbox_dp_bg_draw_y = gameselect_data['SBox']['DP']['BG']['x'], gameselect_data['SBox']['DP']['BG']['y']
    sbox_dp_selected_draw_x, sbox_dp_selected_draw_y = gameselect_data['SBox']['DP']['Selected']['x'], gameselect_data['SBox']['DP']['Selected']['y']
    sbox_dp_bg.clip_draw(sbox_dp_bg_x, 0, sbox_dp_bg_w, sbox_dp_bg_h, sbox_dp_bg_draw_x, sbox_dp_bg_draw_y)
    if selectedgame == 6:
        sbox_dp_selected.clip_draw(sbox_dp_selected_x, 0, sbox_dp_selected_w, sbox_dp_selected_h, sbox_dp_selected_draw_x, sbox_dp_selected_draw_y)
    sbox_dp.clip_draw(sbox_dp_x, 0, sbox_dp_w, sbox_dp_h, sbox_dp_draw_x, sbox_dp_draw_y)

    update_canvas()


def handle_events(frame_time):
    global selectedgame, sbox_mw_character_x, sbox_ch_character_x, sbox_dp_selected_x, credit_num,\
           sound_music, sound_credit, sound_select, delay_time

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

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_1):
            if credit_num > 0:
                if selectedgame == 1:
                    sbox_mw_character_x = sbox_mw_character_w * 2
                    selectedgame = 4
                elif selectedgame == 2:
                    sbox_ch_character_x = sbox_ch_character_w * 2
                    selectedgame = 5
                elif selectedgame == 3:
                    sbox_dp_selected_x = sbox_dp_selected_w * 0
                    selectedgame = 6
                delay_time = current_time + 1.0
                sound_music.stop()
                sound_select.play(1)

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
