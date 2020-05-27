from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image,ImageDraw
import numpy as np
from time import sleep

#oled = Image.open('OLED.png')

logo = Image.open('logo.png')
logo = logo.resize((40, 40))
logo = logo.convert('L')

logo_np = np.array(logo)
for i in range(len(logo_np)):
    for j in range(len(logo_np[i])):
        if logo_np[i][j] < 100:
            logo_np[i][j] = 0

logo = Image.fromarray(logo_np)
logo.convert('1')

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

with canvas(device) as draw:
    draw.bitmap((44, 10), logo, fill='white')

