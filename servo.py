import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, key):
        self.key = key
        GPIO.setmode(GPIO.BCM)
        self.pin = pin_for_key(key)
        GPIO.setup(self.pin, GPIO.OUT)
        self.motor = GPIO.PWM(self.pin, 50)
        self.motor.start(1.5)

    def release(self):
        # TODO: optimize for each key
        self.motor.ChangeDutyCycle(2)
        release_time = release_time_for_key(self.key)
        time.sleep(release_time)
        self.motor.ChangeDutyCycle(1.5)

    # def __del__(self):
        # should evidently not call cleanup here
        # GPIO.cleanup()

def pin_for_key(key):
    return {
        "1": 2,
        "2": 3,
        "3": 4,
        "4": 14,
    }[key]

def release_time_for_key(key):
    return {
        "1": 0.7,
        "2": 0.7,
        "3": 0.7,
        "4": 0.7,
    }[key]
