from pad4pi import rpi_gpio
import time

KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

ROW_PINS = [12, 16, 20, 21]
COL_PINS = [6, 13, 19, 26]

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def handleKey(key):
  if (key=="1"):
    print("number 1")
  elif (key=="2"):
    print("number 2")
  elif (key=="3"):
    print("number 3")
  elif (key=="4"):
    print("number 4")
  elif (key=="#"):
    print("escape")
  else:
    print("key not used")

keypad.registerKeyPressHandler(handleKey)

try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()
