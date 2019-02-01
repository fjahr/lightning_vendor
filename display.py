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
        self.font_small = ImageFont.truetype('assets/fonts/ubuntu/Ubuntu-M.ttf', 12)
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
        self.image.paste(bmp, (10, 0))

        line1 = 'Press any key to start over'
        self.draw.text((5, 185), line1, font = self.font_small, fill = 0)

        self.epd.display(self.epd.getbuffer(self.image.rotate(90)))

    def clean_invoice(self):
        os.remove("tmp/qr.bmp")

        # try:
        #     # Drawing on the image
        #     image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)  # 255: clear the frame
        #
        #     draw = ImageDraw.Draw(image)
        #     # draw.rectangle((0, 10, 200, 34), fill = 0)
        #     draw.text((8, 12), 'hello world', font = font, fill = 255)
        #     draw.text((8, 36), 'e-Paper Demo', font = font, fill = 0)
        #     draw.line((16, 60, 56, 60), fill = 0)
        #     draw.line((56, 60, 56, 110), fill = 0)
        #     draw.line((16, 110, 56, 110), fill = 0)
        #     draw.line((16, 110, 16, 60), fill = 0)
        #     draw.line((16, 60, 56, 110), fill = 0)
        #     draw.line((56, 60, 16, 110), fill = 0)
        #     draw.arc((90, 60, 150, 120), 0, 360, fill = 0)
        #     draw.rectangle((16, 130, 56, 180), fill = 0)
        #     draw.chord((90, 130, 150, 190), 0, 360, fill = 0)
        #     epd.display(epd.getbuffer(image.rotate(90)))
        #     time.sleep(2)
        #     
        #     # read bmp file 
        #     # epd.Clear(0xFF)
        #     image = Image.open('1in54.bmp')
        #     epd.display(epd.getbuffer(image))
        #     time.sleep(2)
        #     
        #     # read bmp file on window
        #     epd.Clear(0xFF)
        #     image1 = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)  # 255: clear the frame
        #     bmp = Image.open('100x100.bmp')
        #     image1.paste(bmp, (50,50))    
        #     epd.display(epd.getbuffer(image1))
        #     time.sleep(2)
        #     
        #     # # partial update
        #     epd.init(epd.lut_partial_update)
        #     
        #     epd.Clear(0xFF)
        #     time_image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
        #     time_draw = ImageDraw.Draw(time_image)
        #     while (True):
        #         time_draw.rectangle((10, 10, 120, 50), fill = 255)
        #         time_draw.text((10, 10), time.strftime('%H:%M:%S'), font = font, fill = 0)
        #         newimage = time_image.crop([10, 10, 120, 50])
        #         time_image.paste(newimage, (10,10))  
        #         epd.display(epd.getbuffer(time_image))
        #         
        #     epd.sleep()
        #         
        #         
        # except:
        #     print("traceback.format_exc():\n%s", traceback.format_exc()) 
        #     exit()
        #
        #
