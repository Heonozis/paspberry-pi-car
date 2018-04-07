import RPi.GPIO as GPIO
import numpy as np
import math
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Car(object):
    drive_pwm = None
    steer_pwm = None

    drive_pin = 5
    steer_pin = 6
    forward_pin = 23
    reverse_pin = 24
    left_pin = 27
    right_pin = 17

    def start(self):
        print("Starting up car!")
        frequency = 1000
        # setup pins
        GPIO.setup(self.forward_pin, GPIO.OUT)
        GPIO.setup(self.reverse_pin, GPIO.OUT)
        GPIO.setup(self.left_pin, GPIO.OUT)
        GPIO.setup(self.right_pin, GPIO.OUT)

        GPIO.setup(self.drive_pin, GPIO.OUT)
        self.drive_pwm = GPIO.PWM(self.drive_pin, frequency)
        self.drive_pwm.start(0)

        GPIO.setup(self.steer_pin, GPIO.OUT)
        self.steer_pwm = GPIO.PWM(self.steer_pin, frequency)
        self.steer_pwm.start(0)

    def ride(self, radius, angle):
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        drive_speed = abs(y) * 100
        steer_speed = abs(x) * 100

        GPIO.output(self.forward_pin, y > 0)
        GPIO.output(self.reverse_pin, y < 0)
        GPIO.output(self.right_pin, x > 0)
        GPIO.output(self.left_pin, x < 0)

        self.drive_pwm.ChangeDutyCycle(min(drive_speed, 100))
        self.steer_pwm.ChangeDutyCycle(min(steer_speed, 100))

    def stop(self):
        print("Stoping car...")
        self.ride(0, 0)
        GPIO.cleanup()
