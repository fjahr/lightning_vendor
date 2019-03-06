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
        self.motor.ChangeDutyCycle(2)
        release_time = release_time_for_key(self.key)
        time.sleep(release_time)
        self.motor.ChangeDutyCycle(1.5)

def pin_for_key(key):
    # for demo only 3 and 4 will be ready
    # return {
    #     "1": 2,
    #     "2": 3,
    #     "3": 4,
    #     "4": 14,
    # }[key]
    return {
        "1": 4,
        "2": 14,
    }[key]

def release_time_for_key(key):
    return {
        "1": 0.75,
        "2": 0.75,
        "3": 0.75,
        "4": 0.75,
    }[key]
