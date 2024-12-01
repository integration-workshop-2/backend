from tcrt5000 import TCRT5000
from time import sleep

sensor = TCRT5000()

while True:
    print(sensor.get_sensor_reading())
    sleep(1)
