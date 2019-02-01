import epd1in54
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from qr import generate_qr
import os

class Display:
    def __init__(self):
        epd = epd1in54.EPD()
        epd.init(epd.lut_full_update)
        epd.Clear(0xFF)
        self.epd = epd

        self.image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.font_small = ImageFont.truetype('assets/fonts/ubuntu/Ubuntu-M.ttf', 14)
        self.font_medium = ImageFont.truetype('assets/fonts/ubuntu/Ubuntu-M.ttf', 24)
        self.font_large = ImageFont.truetype('assets/fonts/ubuntu/Ubuntu-M.ttf', 100)

    def welcome(self, price):
        line1 = 'All items'
        line2 = str(price)[:6] + ' mBTC'

        self.draw.text((50, 130), line1, font = self.font_medium, fill = 0)
        self.draw.text((30, 160), line2, font = self.font_medium, fill = 0)

        bmp = Image.open('assets/img/lightning100x100bw.bmp')
        self.image.paste(bmp, (50, 10))

        self.epd.display(self.epd.getbuffer(self.image.rotate(90)))
        self.epd.sleep()

    def choice(self, key):
        self.draw.text((75, 40), key, font = self.font_large, fill = 0)

        self.epd.display(self.epd.getbuffer(self.image.rotate(90)))
        self.epd.sleep()

    def invoice(self, invoice):
        generate_qr(invoice)

        bmp = Image.open('tmp/qr.bmp')
        self.image.paste(bmp, (13, 0))

        line1 = 'Press any key to start over'
        self.draw.text((5, 185), line1, font = self.font_small, fill = 0)

        self.epd.display(self.epd.getbuffer(self.image.rotate(90)))

    def thank(self):
        self.draw.text((20, 80), 'Thank you!', font = self.font_medium, fill = 0)

        self.epd.display(self.epd.getbuffer(self.image.rotate(90)))

    def clean_invoice(self):
        os.remove("tmp/qr.bmp")
