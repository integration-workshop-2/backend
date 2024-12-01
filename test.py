import time
import board
import adafruit_max30102

# Initialize the sensor
i2c = board.I2C()  # Uses board.SCL and board.SDA
sensor = adafruit_max30102.MAX30102(i2c)

while True:
    try:
        red, ir = sensor.read_red_and_ir()
        print(f"Red: {red}, IR: {ir}")
        time.sleep(1)
    except KeyboardInterrupt:
        break
