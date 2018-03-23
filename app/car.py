import RPi.GPIO as GPIO
import numpy as np
import math
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Car(object):
    pins = []
    pwm = []
    values = [0, 0, 0, 0]

    def start(self):
        print("Starting up car!")
        # forward, reverse, left, right
        self.pins = [17, 27, 23, 24]
        # setup pins
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            self.pwm.append(GPIO.PWM(pin, 2000))
        # start pins
        for i, pin in enumerate(self.pwm):
            pin.start(self.values[i])

    def ride(self, radius, angle):
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        forward = abs(y) * 100 if y > 0 else 0
        reverse = abs(y) * 100 if y < 0 else 0
        left = abs(x) * 100 if x > 0 else 0
        right = abs(x) * 100 if x > 0 else 0

        values = [forward, reverse, left, right]

        print(values)

        for i, pin in enumerate(self.pwm):
            pin.ChangeDutyCycle(values[i])
        self.values = values

    def stop(self):
        print("Stoping car...")
        self.ride(0, 0)
        GPIO.cleanup()
