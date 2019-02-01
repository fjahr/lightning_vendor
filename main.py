from keypad import keypad

def main():
    keypad.registerKeyPressHandler(handleKey)

    try:
        while True:
            time.sleep(0.005)
    except:
        keypad.cleanup()

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


