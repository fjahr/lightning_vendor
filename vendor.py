from server import new_invoice, invoice_paid
from price import Price, PriceUpdater
from display import Display
from keypad import keypad
import time

class Vendor:
    def __init__(self):
        self.price = Price().update_mbtc()
        self.display = Display()
        PriceUpdater(self)

    def start(self):
        # display.welcome(self.price)
        # keypad.registerKeyPressHandler(handleKey)

        while True:
            time.sleep(0.1)

def restart():
    display.welcome(PRICE)
    display.clean_invoice()

def handleKey(key):
    if key in ["1", "2", "3", "4"]:
        print(key)
        selection(key)
    elif (key=="#"):
        print(key)
        restart()
    else:
        print(key)
        print("key not used")

def selection(key):
    display.choice(key)
    time.sleep(1)
    id, invoice = new_invoice(PRICE)
    display.invoice(invoice)

    counter = 0
    while True:
        time.sleep(1)
        counter += 1

        print("waiting for payment try " + str(counter))
        print("checking invoice " + str(id))

        if invoice_paid(id):
            display.thank()
            # servo action with key
            restart()
        elif counter > 60:
            restart()

Vendor().start()
