from server import new_invoice, invoice_paid
from servo import Servo
from price import Price, PriceUpdater
from display import Display
from keypad import keypad
import time
import RPi.GPIO as GPIO

class Vendor:
    def __init__(self):
        self.state = "welcome"
        self.price = Price().update_mbtc()
        self.display = Display()
        self.keypad = keypad
        PriceUpdater(self)

    def start(self):
        try:
            self.state = "welcome"
            self.cleanup()
            self.display.welcome(self.price)
            self.keypad.registerKeyPressHandler(self.selection)

            while True:
                time.sleep(0.1)
        finally:
            GPIO.cleanup()

    def cleanup(self):
        self.display.clean_invoice()

    def selection(self, key):
        try:
            if key in ["1", "2", "3", "4"]:
                self.state = "invoice"
                self.display.choice(key)

                id, invoice = new_invoice(self.price)
                self.display.invoice(invoice)
                self.keypad.registerKeyPressHandler(self.cancel)

                counter = 0
                while True:
                    time.sleep(1)
                    counter += 1

                    # TODO
                    print("waiting for payment try " + str(counter))
                    print("checking invoice " + str(id))

                    if invoice_paid(id) or (counter > 10):
                        self.display.thank()
                        # TODO
                        print("GIVE CANDY!!!!!!!!!!!")
                        Servo(key).release()
                        self.start()
                    elif counter > 60:
                        self.start()
                    break
            else:
                self.start()
        finally:
            GPIO.cleanup()

    def cancel(self, key):
        self.start()

    def update_price(self, price):
        if self.state == "welcome":
            self.price = price
            self.start()
        else:
            self.price = price
