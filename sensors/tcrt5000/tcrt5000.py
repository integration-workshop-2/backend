import RPi.GPIO as GPIO


class TCRT5000:
    def __init__(self, sensor_pin: int = 17) -> None:
        self.__sensor_pint = sensor_pin

        # Set up the GPIO mode (BCM or BOARD)
        GPIO.setmode(GPIO.BCM)

        # Using internal pull-up resistor
        GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_sensor_reading(self) -> int:
        """If the reading is 1, it detected something"""

        return GPIO.input(self.__sensor_pint)

    def __del__(self):
        GPIO.cleanup()
