import RPi.GPIO as GPIO
import time


class Servo:
    def __init__(self, key):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin_for_key(key)
        GPIO.setup(self.pin, GPIO.OUT)
        self.motor = GPIO.PWM(self.pin, 50)
        p.start(2.5)

    def release(self):
        p.ChangeDutyCycle(5)

    def __del__(self):
        GPIO.cleanup()

def pin_for_key(key):
    {
        "1": 2,
        "2": 3,
        "3": 4,
        "4": 14,
    }[key]
