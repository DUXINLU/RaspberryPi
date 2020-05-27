from PIL import ImageDraw, Image
from time import sleep

oled = Image.open('OLED.png')

logo = Image.open('logo.png')
logo = logo.resize((64, 64))
logo = logo.convert('L')

draw = ImageDraw.Draw(oled)
draw.bitmap((34, 0), logo, fill='white')

oled.show()
