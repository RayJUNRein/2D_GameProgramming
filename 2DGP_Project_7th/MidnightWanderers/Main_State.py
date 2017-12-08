from pico2d import *

import Game_Framework
import json

name = "Main_State"

from Background import Background as Background
from Road import Road as Road
from Boss_Map import GWoodBackground as GWoodBackground
from Boss_Map import GWoodRoad as GWoodRoad
from Character import Character as Character
from Weapon import Arrow as Arrow
from Enemy import Goblin as Goblin
from Font import Font as Font
from Item import Card as Card


background = None
road = None
gwroads = None
gwbackground = None
character = None
arrows = None
goblins = None
fonts = None
cards = None


def create_fonts():
    font_data_file = open('Data\Font_Data.txt', 'r')
    font_data = json.load(font_data_file)
    font_data_file.close()
    fonts = []
    for name in font_data:
        font = Font()
        font.name = name
        font.frame_w = font_data[name]['w']
        font.frame_h = font_data[name]['h']
        font.x = font_data[name]['x']
        fonts.append(font)

    return fonts


def create_cards():
    card_data_file = open('Card_Data.txt', 'r')
    card_data = json.load(card_data_file)
    card_data_file.close()
    cards = []
    for name in card_data:
        card = Card()
        card.name = name
        card.frame_h = card_data[name]['h']
        card.x = card_data[name]['x']
        fonts.append(card)

    return cards


def enter():
    global background, road, gwroads, gwbackground, character, arrows, goblins, fonts, cards

    Game_Framework.reset_time()

    background = Background()
    road = Road()
    gwroads = [GWoodRoad() for i in range(36)]
    gwbackground = GWoodBackground()
    character = Character()
    arrows = [Arrow() for i in range(3)]
    goblins = [Goblin() for i in range(50)]
    fonts = create_fonts()
    cards = [Card() for i in range(20)]

    character.set_road(road)
    road.set_center_object(character)
    background.set_center_object(character)
    for arrow in arrows:
        arrow.set_road(road)
        arrow.set_character(character)
    for goblin in goblins:
        goblin.set_road(road)
        goblin.set_character(character)
    gwbackground.set_center_object(character)
    i = 0
    for gwroad in gwroads:
        gwroad.x += 16 * i
        gwroad.set_center_object(character)
        if i == 35:
            character.set_gwroad(gwroad)
        i += 1


def exit():
    global background, road, gwroads, gwbackground, character, arrows, goblins, fonts, cards

    del background
    del road
    del gwroads
    del gwbackground
    del character
    del arrows
    del goblins
    del fonts
    del cards

    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            Game_Framework.quit()

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            Game_Framework.quit()

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


def follow(road, character):
    left_a, bottom_a, right_a, top_a = road.get_bb(character)
    left_b, bottom_b, right_b, top_b = character.get_bb()

    if character.jump_status == False and character.fall_status == False:
        if top_a < bottom_b:
            character.y = top_a + 60
        elif top_a > bottom_b:
            character.y = bottom_a + 120


def follow_gwroad(gwroad, character):
    left_a, bottom_a, right_a, top_a = gwroad.get_bb()
    left_b, bottom_b, right_b, top_b = character.get_bb()

    if character.jump_status == False and character.fall_status == False:
        if top_a < bottom_b:
            character.y = top_a + 60
        elif top_a > bottom_b:
            character.y = bottom_a + 120


def follow_enemy(road, enemy):
    left_a, bottom_a, right_a, top_a = road.get_bb(enemy)
    left_b, bottom_b, right_b, top_b = enemy.get_bb()

    if top_a < bottom_b:
        enemy.y = top_a + 60
    elif top_a > bottom_b:
        enemy.y = bottom_a + 120


def update(frame_time):
    background.update(frame_time)
    road.update(frame_time)
    character.update(frame_time)
    gwbackground.update(frame_time)
    for gwroad in gwroads:
        gwroad.update(frame_time)
        if gwroad.draw_status == True:
            follow_gwroad(gwroad, character)
    for arrow in arrows:
        arrow.update(frame_time)
    for goblin in goblins:
        goblin.update(frame_time)
    for card in cards:
        card.update(frame_time)

    for goblin in goblins:
        follow_enemy(road, goblin)
        if collide(character, goblin):
            goblins.remove(goblin)
        #for arrow in arrows:
        #    if collide(arrow, goblin):
        #        goblins.remove(goblin)
    for card in cards:
        if collide(character, card):
            cards.remove(card)

    follow(road, character)


def draw(frame_time):
    clear_canvas()

    # 배경 이미지 화면 출력
    background.draw(frame_time)

    # 스테이지 1 기본 지형 맵 화면 출력
    road.draw()

    # 스테이지 1 보스 Golem Wood 출현 맵 화면 출력 (애니메이션 적용)
    for gwroad in gwroads:
        gwroad.draw(frame_time)
    #gwbackground.draw(frame_time)

    # 주인공 화면 출력
    character.draw(frame_time)
    # 주인공 무기 화면 출력
    for arrow in arrows:
        arrow.draw()

    # 적군 화면 출력
    for goblin in goblins:
        goblin.draw(frame_time)

    # 캐릭터 정보 화면 출력
    for font in fonts:
        font.draw(frame_time)

    # 점수 카드 화면 출력
    for card in cards:
        card.draw(frame_time)

#    road.draw_bb()
    for gwroad in gwroads:
        gwroad.draw_bb()
    character.draw_bb()
    for arrow in arrows:
        arrow.draw_bb()
    for goblin in goblins:
        goblin.draw_bb()
#    for card in cards:
#        card.draw_bb()

    update_canvas()
