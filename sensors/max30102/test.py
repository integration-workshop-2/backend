import max30102
import hrcalc
import time

# Initialize the MAX30102 sensor
m = max30102.MAX30102()


def read_sensor():
    while True:
        data = m.get_heart_rate_and_spo2_level()

        print("Heart Rate: ", data.heart_rate, "BPM")
        print("SpO2 Level: ", data.spo2_level, "%")

        # Wait for a short time before reading again
        time.sleep(1)


if __name__ == "__main__":
    read_sensor()
