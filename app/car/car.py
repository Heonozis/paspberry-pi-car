import RPi.GPIO as GPIO
import math
from .constants import PIN_DRIVE, PIN_FORWARD, PIN_LEFT, PIN_REVERSE, PIN_RIGHT, PIN_STEER

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Car(object):
    drive_pwm = None
    steer_pwm = None

    def start(self):
        print("Starting up car!")
        frequency = 1000
        # setup pins
        GPIO.setup(PIN_FORWARD, GPIO.OUT)
        GPIO.setup(PIN_REVERSE, GPIO.OUT)
        GPIO.setup(PIN_LEFT, GPIO.OUT)
        GPIO.setup(PIN_RIGHT, GPIO.OUT)

        GPIO.setup(PIN_DRIVE, GPIO.OUT)
        self.drive_pwm = GPIO.PWM(PIN_DRIVE, frequency)
        self.drive_pwm.start(0)

        GPIO.setup(PIN_STEER, GPIO.OUT)
        self.steer_pwm = GPIO.PWM(PIN_STEER, frequency)
        self.steer_pwm.start(0)

    def ride(self, radius, angle):
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        drive_speed = abs(y) * 100
        steer_speed = abs(x) * 100

        GPIO.output(PIN_FORWARD, y > 0)
        GPIO.output(PIN_REVERSE, y < 0)
        GPIO.output(PIN_RIGHT, x > 0)
        GPIO.output(PIN_LEFT, x < 0)

        self.drive_pwm.ChangeDutyCycle(min(drive_speed, 100))
        self.steer_pwm.ChangeDutyCycle(min(steer_speed, 100))

    def stop(self):
        print("Stoping car...")
        self.ride(0, 0)
        GPIO.cleanup()
