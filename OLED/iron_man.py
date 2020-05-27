from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw
import numpy as np
import time

logo_path = 'logo.png'


class OLED:
    def __init__(self):
        serial = i2c(port=1, address=0x3C)
        self.device = ssd1306(serial)

    def Animation(self, start, end):
        pass

    def welcome(self):
        with canvas(self.device) as draw:
            draw.text((16, 28), 'Welcome home Sir', fill='white')
        time.sleep(3)

    def main(self):
        # logo初始化
        logo = Image.open(logo_path)
        logo = logo.resize((30, 30))
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

        print(time.strftime("%m/%d %H:%M %a", time.localtime()))

        while True:
            with canvas(self.device) as draw:
                draw.bitmap((0, 0), logo, fill='white')
                draw.text((0, 32), time.strftime("%H:%M", time.localtime()))
                draw.text((0, 44), time.strftime("%m/%d", time.localtime()))
                draw.text((6, 56), time.strftime("%a", time.localtime()))


if __name__ == '__main__':
    oled = OLED()
    oled.welcome()
    try:
        oled.main()
    except:
        exit()
