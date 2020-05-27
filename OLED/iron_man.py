from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw
import numpy as np
import time

logo_path = 'head.png'


class OLED:
    def __init__(self):
        serial = i2c(port=1, address=0x3C)
        self.device = ssd1306(serial)

    def Animation(self, start, end):
        pass

    def welcome(self):
        with canvas(self.device) as draw:
            draw.text((16, 28), 'Welcome home Sir', fill='white')
        time.sleep(1)

    def main(self):
        # logo初始化
        logo = Image.open(logo_path)
        logo = logo.resize((30, 30))
        logo = logo.convert('L')
        # 切图
        logo_np = np.array(logo)
        for i in range(len(logo_np)):
            for j in range(len(logo_np[i])):
                if logo_np[i][j] >= 200:
                    logo_np[i][j] = 0
                    continue
                if logo_np[i][j] < 200:
                    logo_np[i][j] = 255
                    continue
        # 黑白化
        logo = Image.fromarray(logo_np)
        self.logo = logo.convert('1')
        
        heart=Image.open('_.png')
        heart=heart.resize((98,68))
        heart = heart.convert('L')
        heart_np = np.array(heart)
        for i in range(len(heart_np)):
            for j in range(len(heart_np[i])):
                # print(heart_np[i][j])
                if heart_np[i][j] >= 150:
                    heart_np[i][j] = 0
                    continue
                if heart_np[i][j] < 150:
                    heart_np[i][j] = 255
                    continue
        self.heart=Image.fromarray(heart_np).convert('1')

        while True:
            with canvas(self.device) as draw:
                draw.bitmap((0, 0), self.logo, fill='white')
                draw.text((0, 32), time.strftime("%H:%M", time.localtime()), fill='white')
                draw.text((0, 42), time.strftime("%m/%d", time.localtime()), fill='white')
                draw.text((6, 52), time.strftime("%a", time.localtime()), fill='white')
                draw.bitmap((30,0),self.heart,fill='white')


if __name__ == '__main__':
    oled = OLED()
    oled.welcome()
    try:
        oled.main()
    except Exception as e:
        print(e)
        exit()
