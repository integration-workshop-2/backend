from infra.hardware.motor.motor import Motor
from time import sleep

motor_1 = Motor(control_pins=[6, 13, 19, 26])
motor_2 = Motor(control_pins=[18, 23, 24, 25])
motor_3 = Motor(control_pins=[12, 16, 20, 21])

motor_1.execute_half_step()
sleep(2)

motor_2.execute_half_step()
sleep(2)

motor_3.execute_half_step()
sleep(2)
