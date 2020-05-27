from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw
import numpy as np
from time import sleep

logo_path = 'logo.png'


class OLED:
    def __init__(self):
        serial = i2c(port=1, address=0x3C)
        self.device = ssd1306(serial)

    def Animation(self, start, end):

    def welcome(self):
        with canvas(self.device) as draw:
            draw.text((15, 30), 'Welcome home Sir.', fill='white')
        sleep(3)

    def show_logo(self):
        # 初始化
        logo = Image.open(logo_path)
        logo = logo.resize((40, 40))
        logo = logo.convert('L')
        # 切图
        logo_np = np.array(logo)
        for i in range(len(logo_np)):
            for j in range(len(logo_np[i])):
                if logo_np[i][j] < 100:
                    logo_np[i][j] = 0
        # 黑白化
        logo = Image.fromarray(logo_np)
        self.logo = logo.convert('1')

        with canvas(self.device) as draw:
            draw.bitmap((44, 15), logo, fill='white')
        sleep(3)

        # logo移动
        logox, logoy = 44, 15
        logo_size = 40
        for i in range(5):


def init():


def show():
    # welcome text
    with canvas(device) as draw:
        draw.text((15, 30), 'welcome home Sir.', fill='white')
    sleep(3)

    # show logo
    with canvas(device) as draw:
        draw.bitmap((44, 15), logo, fill='white')
    sleep(1)

    logo = logo.resize((20, 20))
    with canvas(device) as draw:
        draw.bitmap((0, 0), logo, fill='white')
    sleep(3)


if __name__ == '__main__':
    show()
