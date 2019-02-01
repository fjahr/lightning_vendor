from keypad import keypad
from price import Price
from display import Display
from server import new_invoice, invoice_paid
import time

PRICE = 0
display = Display()

def main():
    PRICE = Price().update_mbtc()
    display.welcome(PRICE)
    keypad.registerKeyPressHandler(handleKey)

    while True:
        time.sleep(0.1)

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

def restart():
    display.welcome(PRICE)
    display.clean_invoice()

def selection(key):
    display.choice(key)
    time.sleep(1)
    id, invoice = new_invoice(PRICE)
    display.invoice(invoice)

    counter = 0
    while True:
        time.sleep(1)
        counter += 1

        if invoice_paid(id):
            display.thank()
            # servo action with key
            restart()
        elif counter > 60:
            restart()

main()
