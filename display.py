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

        font_path = os.path.join(os.path.dirname(__file__), 'assets/fonts/ubuntu/Ubuntu-M.ttf')
        self.font_small = ImageFont.truetype(font_path, 14)
        self.font_medium = ImageFont.truetype(font_path, 24)
        self.font_large = ImageFont.truetype(font_path, 100)

    def welcome(self, price):
        image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(image)

        line1 = 'All items'
        line2 = str(price)[:6] + ' mBTC'

        draw.text((50, 130), line1, font = self.font_medium, fill = 0)
        draw.text((30, 160), line2, font = self.font_medium, fill = 0)

        image_path = os.path.join(os.path.dirname(__file__), 'assets/img/lightning100x100bw.bmp')
        bmp = Image.open(image_path)
        image.paste(bmp, (50, 10))

        self.epd.display(self.epd.getbuffer(image.rotate(90)))

    def choice(self, key):
        image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(image)

        draw.text((75, 40), key, font = self.font_large, fill = 0)
        draw.text((20, 160), "Generating invoice...", font = self.font_medium, fill = 0)

        self.epd.display(self.epd.getbuffer(image.rotate(90)))

    def invoice(self, invoice):
        image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(image)

        generate_qr(invoice)

        qr_path = os.path.join(os.path.dirname(__file__), 'tmp/qr.bmp')
        bmp = Image.open(qr_path)
        image.paste(bmp, (13, 0))

        line1 = 'Press any key to start over'
        draw.text((5, 185), line1, font = self.font_small, fill = 0)

        self.epd.display(self.epd.getbuffer(image.rotate(90)))

    def thank(self):
        image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(image)

        draw.text((20, 80), 'Thank you!', font = self.font_medium, fill = 0)

        self.epd.display(self.epd.getbuffer(image.rotate(90)))

    def clean_invoice(self):
        try:
            qr_path = os.path.join(os.path.dirname(__file__), 'tmp/qr.bmp')
            os.remove(qr_path)
        except:
            return
