import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, key):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin_for_key(key)
        GPIO.setup(self.pin, GPIO.OUT)
        self.motor = GPIO.PWM(self.pin, 50)
        self.motor.start(1.5)

    def release(self):
        self.motor.ChangeDutyCycle(2)
        time.sleep(0.7)
        self.motor.ChangeDutyCycle(1.5)

    def __del__(self):
        GPIO.cleanup()

def pin_for_key(key):
    return {
        "1": 2,
        "2": 3,
        "3": 4,
        "4": 14,
    }[key]
