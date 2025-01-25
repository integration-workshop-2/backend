from typing import List
import RPi.GPIO as GPIO
import time


class Motor:
    def __init__(self, control_pins: List[int] = [4, 17, 27, 22]) -> None:
        GPIO.setmode(GPIO.BCM)

        self.__control_pins = control_pins

        self.__half_step_sequence = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
        ]

        for pin in self.__control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    def execute_half_step(self) -> None:
        for _ in range(512):
            for i in range(8):
                for j in range(4):
                    GPIO.output(self.__control_pins[j], self.__half_step_sequence[i][j])
                time.sleep(0.001)

    def __del__(self) -> None:
        GPIO.cleanup()
