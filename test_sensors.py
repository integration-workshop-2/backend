from sensors.gy906 import GY906
from sensors.max30102 import MAX30102
from sensors.tcrt5000 import TCRT5000

gy906 = GY906()
max30102 = MAX30102()
tcrt5000 = TCRT5000()

while True:
    print(f"Ambient temperature: {gy906.get_ambient_temperature()} °C")
    print(f"Target temperature: {gy906.get_target_temperature()} °C")

    max30102_response = max30102.get_heart_rate_and_spo2_level()
    print(f"Heart rate: {max30102_response.heart_rate} BPM")
    print(f"SPO2 level: {max30102_response.spo2_level} %")

    print(f"TCRT5000 reading: {tcrt5000.get_sensor_reading()}")
