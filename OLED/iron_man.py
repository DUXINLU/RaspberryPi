from PIL import ImageDraw, Image
import numpy as np
from time import sleep

oled = Image.open('OLED.png')

logo = Image.open('logo.png')
logo = logo.resize((50, 50))
logo = logo.convert('L')

logo_np = np.array(logo)
for i in range(len(logo_np)):
    for j in range(len(logo_np[i])):
        if logo_np[i][j] < 100:
            logo_np[i][j] = 0

logo = Image.fromarray(logo_np)
logo.convert('1')

draw = ImageDraw.Draw(oled)
draw.bitmap((39, 7), logo, fill='white')

oled.show()
