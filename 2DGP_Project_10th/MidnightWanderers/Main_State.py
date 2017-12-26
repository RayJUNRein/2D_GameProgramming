from pico2d import *

import Game_Framework
import End_State
import random
import time

name = "Main_State"

from Background import Background as Background
from Road import Road as Road
from Character import Character as Character
from Weapon import Arrow as Arrow
from Enemy import Goblin as Goblin
from Item import Card as Card
from Item import Bound as Bound
from UI import UI as UI
from Credit import Credit as Credit


background = None
road = None
character = None
arrows = []
goblins = None
cards = None
bounds = None
card_num = 20
status_ui = None
font_ui = None
font_credit = None
credit_num = 0
sound_credit = None
sound_music = None


def enter():
    global background, road, character, goblins, cards, bounds, arrows,\
           status_ui, font_ui, font_credit, sound_music, sound_credit

    Game_Framework.reset_time()

    #open_canvas(1152, 672)

    background = Background()
    road = Road()
    character = Character()
    goblins = [Goblin() for i in range(5)]
    cards = [Card() for i in range(20)]
    bounds = [Bound() for i in range(4)]
    arrows = []
    status_ui = UI()
    font_ui = status_ui.create_ui()
    font_credit = Credit()

    character.set_road(road)
    road.set_center_object(character)
    background.set_center_object(character)

    for goblin in goblins:
        goblin.set_road(road)
        goblin.set_character(character)

    for card in cards:
        card.set_road(road)

    for bound in bounds:
        bound.set_road(road)

    sound_music = load_music('Sounds\Music\STAGE1_AREA1.mp3')
    sound_music.set_volume(30)
    sound_music.repeat_play()

    sound_credit = load_wav('Sounds\Credit.wav')
    sound_credit.set_volume(60)
    character.credit_num = credit_num


def exit():
    global background, road, character, arrows, goblins, cards, bounds,\
           status_ui, font_ui, font_credit, sound_music, sound_credit

    del background, road
    del character, arrows
    del goblins
    del cards, bounds
    del status_ui, font_ui, font_credit
    del sound_music, sound_credit


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global credit_num, sound_credit
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

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            if character.life_num == 0 and credit_num > 0:
                character.dir_y = -1
                character.fall_status = True
                credit_num -= 1
                character.life_num = 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_9):
            credit_num += 1
            sound_credit.play(1)

        else:
            character.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def character_follow_road(road, character):
    left_a, bottom_a, right_a, top_a = road.get_bb(character)
    left_b, bottom_b, right_b, top_b = character.get_bb()

    if character.jump_status == False and character.fall_status == False and character.life_num != 0:
        if top_a < bottom_b:
            character.y = top_a + 60
        elif top_a > bottom_b:
            character.y = bottom_a + 120


def others_follow_road(road, others):
    left_a, bottom_a, right_a, top_a = road.get_bb(others)
    left_b, bottom_b, right_b, top_b = others.get_bb()

    if top_a < bottom_b:
        others.y = top_a + 60
    elif top_a > bottom_b:
        others.y = bottom_a + 120


def update(frame_time):
    global card_num, font_ui

    background.update(frame_time)
    road.update(frame_time)
    character.update(frame_time)

    if character.shot_status == True:
        arrow = Arrow()
        arrow.set_road(road)
        arrow.set_character(character)
        arrows.append(arrow)
        character.shot_status = False

    for arrow in arrows:
        if arrow.x < character.x - arrow.canvas_width or arrow.x > character.x + arrow.canvas_width or arrow.y > arrow.canvas_height:
            arrows.remove(arrow)
        arrow.update(frame_time)

    for card in cards:
        card.update(frame_time)
        others_follow_road(road, card)
        if collide(character, card):
            character.get_item()
            cards.remove(card)
            card_num += 1
            status_ui.score_1p = 100 * card_num

    status_ui.update(frame_time)

    for bound in bounds:
        bound.update(frame_time)
        others_follow_road(road, bound)
        if collide(character, bound):
            character.get_item()
            for arrow in arrows:
                arrow.get_bound()
            bounds.remove(bound)

    if character.x > 400:
        if len(goblins) < 5 and character.life_num > 0:
            goblin = Goblin()
            goblin.set_road(road)
            goblin.set_character(character)
            goblin.x = character.x + random.randint(0, 500)
            if abs(goblin.x - character.x) < 200:
                goblin.x -= 400
            goblin.y = character.y + random.randint(-300, 300)
            goblins.append(goblin)

    for goblin in goblins:
        if goblin.x < character.x - goblin.canvas_width:
            goblins.remove(goblin)

        others_follow_road(road, goblin)

        if collide(character, goblin):
            attacked_time = time.time()
            character.attacked(attacked_time)

        if character.life_num == 0:
            goblin.dir_x = -1

        for arrow in arrows:
            if collide(arrow, goblin):
                goblin.dead()
                character.kill_enemy()
                arrows.remove(arrow)
                goblins.remove(goblin)

        goblin.update(frame_time)

    character_follow_road(road, character)
    font_credit.update(frame_time, credit_num)

    if character.x > road.w:
        Game_Framework.change_state(End_State)


def draw(frame_time):
    global font_ui

    clear_canvas()

    # 배경 이미지 화면 출력
    background.draw(frame_time)

    # 스테이지 1 기본 지형 맵 화면 출력
    road.draw()

    # 주인공 화면 출력
    character.draw(frame_time)
    # 주인공 무기 화면 출력
    for arrow in arrows:
        arrow.draw(frame_time)

    # 적군 화면 출력
    for goblin in goblins:
        goblin.draw(frame_time)

    # 점수 카드 화면 출력
    for card in cards:
        card.draw(frame_time)

    for bound in bounds:
        bound.draw(frame_time)

    status_ui.update(frame_time)
    # 캐릭터 정보 화면 출력
    for font in font_ui:
        font.draw(frame_time)
        #font.image.clip_draw(font.frame_x * font.draw_width, font.frame_y * font.draw_height, font.draw_width, font.draw_height, font.x, font.y)

    font_credit.draw(frame_time)

#   road.draw_bb()
#    for gwroad in gwroads:
#        gwroad.draw_bb()
#    character.draw_bb()
#    for arrow in arrows:
#        arrow.draw_bb()
#    for goblin in goblins:
#        goblin.draw_bb()
#    for card in cards:
#        card.draw_bb()
#    for bound in bounds:
#        bound.draw_bb()

    update_canvas()
