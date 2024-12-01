from sensors.gy906 import GY906
from time import sleep

gy906 = GY906()

while True:
    print(gy906.get_ambient_temperature())
    sleep(1)
