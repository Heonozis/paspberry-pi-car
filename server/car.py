import RPi.GPIO as GPIO
import numpy as np
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

    def ride(self, values, nsteps=5, step_speed=0.3):
        for step in range(nsteps):
            for i, pin in enumerate(self.pwm):
                print('setting pin {}'.format(i))
                start_value = self.values[i]
                end_value = values[i]
                speeds = np.linspace(start_value, end_value, num=nsteps)
                print('setting speed to {}'.format(speeds[step]))
                pin.ChangeDutyCycle(int(speeds[step]))
            time.sleep(step_speed)
        self.values = values

    def stop(self):
        print("Stoping car...")
        self.ride([0, 0, 0, 0])
        GPIO.cleanup()
