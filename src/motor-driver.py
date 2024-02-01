"""
Drives the stepper motor to open the door.
"""

import RPi.GPIO as GPIO
import time


class MotorDriver:
    def __init__(
        self,
        step_pin,
        dir_pin,
        enable_pin,
        sleep_pin,
        steps_per_revolution,
        speed,
        acceleration,
    ):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.enable_pin = enable_pin
        self.sleep_pin = sleep_pin
        self.steps_per_revolution = steps_per_revolution
        self.speed = speed
        self.acceleration = acceleration

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.sleep_pin, GPIO.OUT)

        GPIO.output(self.enable_pin, GPIO.LOW)
        GPIO.output(self.sleep_pin, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()

    def move(self, direction, steps):
        GPIO.output(self.dir_pin, direction)
        GPIO.output(self.enable_pin, GPIO.LOW)

        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(self.speed)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(self.speed)

    def open_door(self):
        self.move(GPIO.HIGH, self.steps_per_revolution)

    def close_door(self):
        self.move(GPIO.LOW, self.steps_per_revolution)

    def set_speed(self, speed):
        self.speed = speed

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

    def set_steps_per_revolution(self, steps_per_revolution):
        self.steps_per_revolution = steps_per_revolution
