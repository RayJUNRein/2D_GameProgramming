from pico2d import *


def handle_events():
    global running
    events = get_events()

    for event in events:
        # ESC키를 이용한 종료
        if event.type == SDL_QUIT:
            running = False

        # 종료 버튼 클릭을 이용한 종료
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False


open_canvas(4000, 224)


# 배경 이미지
background = load_image('Resources\Levels_1\Background\MidnightWanderers_Levels_1_Background2.png')
# 스테이지 1 Golem Wood 출현 전까지의 맵
road = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road.png')
# 스테이지 1 보스 Golem Wood 출현하는 맵 (애니메이션 적용 예정)
gwood_road = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road_GolemWood.png')
gwood_background = load_image('Resources\Levels_1\Road\MidnightWanderers_Levels_1_Road33.png')


running = True

# 플레이 화면 크기 지정
width = 384
height = 224
# 피벗으로 인한 객체 위치 지정
center = height / 2
# 스테이지 1 지형 맵 크기 지정
road_w = 3583
groad_w = 192


while running:
    clear_canvas()

    # 배경 이미지 화면 출력
    for i in range(10):
        background.draw(width * i, center)

    # 스테이지 1 기본 지형 맵 화면 출력
    road.draw(road_w / 2, center)

    # 스테이지 1 보스 Golem Wood 출현 맵 화면 출력 (애니메이션 미적용)
    for i in range(5):
        gwood_road.draw((road_w / 2) + (groad_w / 2) * i, center)
    gwood_background.draw(road_w / 2 + (624 / 2), center)

    update_canvas()
    handle_events()

close_canvas()