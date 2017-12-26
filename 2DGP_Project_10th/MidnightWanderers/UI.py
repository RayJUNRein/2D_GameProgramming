from pico2d import *
from Font import Font as Font

fonts = []

ui_data_file = open('Data\StatusUI_Data.txt', 'r')
ui_data = json.load(ui_data_file)
ui_data_file.close()

font_data_file = open('Data\Font_Data.txt', 'r')
font_data = json.load(font_data_file)
font_data_file.close()


class UI:
    def __init__(self):
        self.score_1p = 0

    def create_ui(self):
        global fonts, font_data, ui_data

        font = Font()
        font.name = 'S1'
        font.frame_x = font_data['Credit']['S']['x']
        font.frame_y = font_data['Credit']['S']['y']
        font.draw_width = font_data['Credit']['S']['w']
        font.draw_width = font_data['Credit']['S']['h']
        font.x = ui_data['S1']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'C1'
        font.frame_x = font_data['Credit']['C']['x']
        font.frame_y = font_data['Credit']['C']['y']
        font.draw_width = font_data['Credit']['C']['w']
        font.draw_width = font_data['Credit']['C']['h']
        font.x = ui_data['C1']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'O1'
        font.frame_x = font_data['Credit']['O']['x']
        font.frame_y = font_data['Credit']['O']['y']
        font.draw_width = font_data['Credit']['O']['w']
        font.draw_width = font_data['Credit']['O']['h']
        font.x = ui_data['O1']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'R1'
        font.frame_x = font_data['Credit']['R']['x']
        font.frame_y = font_data['Credit']['R']['y']
        font.draw_width = font_data['Credit']['R']['w']
        font.draw_width = font_data['Credit']['R']['h']
        font.x = ui_data['R1']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'E1'
        font.frame_x = font_data['Credit']['E']['x']
        font.frame_y = font_data['Credit']['E']['y']
        font.draw_width = font_data['Credit']['E']['w']
        font.draw_width = font_data['Credit']['E']['h']
        font.x = ui_data['E1']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '-1'
        font.frame_x = font_data['Credit']['-']['x']
        font.frame_y = font_data['Credit']['-']['y']
        font.draw_width = font_data['Credit']['-']['w']
        font.draw_width = font_data['Credit']['-']['h']
        font.x = ui_data['-1']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '01'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['01']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '02'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['02']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '03'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['03']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '04'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['04']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '05'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['05']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '06'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['06']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '07'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['07']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '08'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['08']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'H'
        font.frame_x = font_data['Credit']['H']['x']
        font.frame_y = font_data['Credit']['H']['y']
        font.draw_width = font_data['Credit']['H']['w']
        font.draw_width = font_data['Credit']['H']['h']
        font.x = ui_data['H']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'I'
        font.frame_x = font_data['Credit']['I']['x']
        font.frame_y = font_data['Credit']['I']['y']
        font.draw_width = font_data['Credit']['I']['w']
        font.draw_width = font_data['Credit']['I']['h']
        font.x = ui_data['I']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '-2'
        font.frame_x = font_data['Credit']['-']['x']
        font.frame_y = font_data['Credit']['-']['y']
        font.draw_width = font_data['Credit']['-']['w']
        font.draw_width = font_data['Credit']['-']['h']
        font.x = ui_data['-2']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '001'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['001']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '002'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['002']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '003'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['003']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '004'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['004']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '005'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['005']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '006'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['006']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '007'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['007']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '008'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['008']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'S2'
        font.frame_x = font_data['Credit']['S']['x']
        font.frame_y = font_data['Credit']['S']['y']
        font.draw_width = font_data['Credit']['S']['w']
        font.draw_width = font_data['Credit']['S']['h']
        font.x = ui_data['S2']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'C2'
        font.frame_x = font_data['Credit']['C']['x']
        font.frame_y = font_data['Credit']['C']['y']
        font.draw_width = font_data['Credit']['C']['w']
        font.draw_width = font_data['Credit']['C']['h']
        font.x = ui_data['C2']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'O2'
        font.frame_x = font_data['Credit']['O']['x']
        font.frame_y = font_data['Credit']['O']['y']
        font.draw_width = font_data['Credit']['O']['w']
        font.draw_width = font_data['Credit']['O']['h']
        font.x = ui_data['O2']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'R2'
        font.frame_x = font_data['Credit']['R']['x']
        font.frame_y = font_data['Credit']['R']['y']
        font.draw_width = font_data['Credit']['R']['w']
        font.draw_width = font_data['Credit']['R']['h']
        font.x = ui_data['R2']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = 'E2'
        font.frame_x = font_data['Credit']['E']['x']
        font.frame_y = font_data['Credit']['E']['y']
        font.draw_width = font_data['Credit']['E']['w']
        font.draw_width = font_data['Credit']['E']['h']
        font.x = ui_data['E2']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '-3'
        font.frame_x = font_data['Credit']['-']['x']
        font.frame_y = font_data['Credit']['-']['y']
        font.draw_width = font_data['Credit']['-']['w']
        font.draw_width = font_data['Credit']['-']['h']
        font.x = ui_data['-3']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0001'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0001']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0002'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0002']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0003'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0003']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0004'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0004']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0005'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0005']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0006'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0006']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0007'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0007']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        font = Font()
        font.name = '0008'
        font.frame_x = font_data['Credit']['0']['x']
        font.frame_y = font_data['Credit']['0']['y']
        font.draw_width = font_data['Credit']['0']['w']
        font.draw_width = font_data['Credit']['0']['h']
        font.x = ui_data['0008']['x']
        font.y = font.canvas_height - 15
        fonts.append(font)

        return fonts

    def update(self, frame_time):
        global fonts, font_data, ui_data

        if self.score_1p / 100 == 0:
            for font in fonts:
                if font.name == '06':
                    font.frame_x = font_data['Credit']['0']['x']
                    font.frame_y = font_data['Credit']['0']['y']
                    font.draw_width = font_data['Credit']['0']['w']
                    font.draw_width = font_data['Credit']['0']['h']

        elif self.score_1p / 100 == 1:
            for font in fonts:
                if font.name == '06':
                    font.frame_x = font_data['Credit']['1']['x']
                    font.frame_y = font_data['Credit']['1']['y']
                    font.draw_width = font_data['Credit']['1']['w']
                    font.draw_width = font_data['Credit']['1']['h']

        elif self.score_1p / 100 == 2:
            for font in fonts:
                if font.name == '06':
                    font.frame_x = font_data['Credit']['2']['x']
                    font.frame_y = font_data['Credit']['2']['y']
                    font.draw_width = font_data['Credit']['2']['w']
                    font.draw_width = font_data['Credit']['2']['h']
