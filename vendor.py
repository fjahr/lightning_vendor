from server import new_invoice, invoice_paid
from servo import Servo
from price import Price, PriceUpdater
from display import Display
from keypad import new_keypad
import time

class Vendor:
    def __init__(self):
        self.state = "welcome"
        self.price = Price().update_mbtc()
        self.display = Display()
        PriceUpdater(self)

    def start(self):
        self.state = "welcome"
        self.cleanup()
        self.display.welcome(self.price)
        new_keypad().registerKeyPressHandler(self.selection)

        while True:
            time.sleep(0.1)

    def cleanup(self):
        self.display.clean_invoice()

    def selection(self, key):
        if key in ["1", "2", "3", "4"]:
            self.state = "invoice"
            self.display.choice(key)

            id, invoice = new_invoice(self.price)
            self.display.invoice(invoice)
            # remove for now
            # self.keypad.registerKeyPressHandler(self.cancel)

            counter = 0
            while True:
                time.sleep(1)
                counter += 1
                print("waiting for payment try " + str(counter))

                if invoice_paid(id):
                    self.display.thank()
                    Servo(key).release()
                    break
                elif counter > 60:
                    break
        self.start()

    def cancel(self, key):
        self.start()

    def update_price(self, price):
        if self.state == "welcome":
            self.price = price
            self.start()
        else:
            self.price = price
