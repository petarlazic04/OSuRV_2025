#!/usr/bin/env python3

from motors import *
import time

def raise_flag(motor_number, hold, angle, velocity):
        motor_state.angle = angle * 10
        motor_state.velocity = velocity
        motors_driver.update(motor_number, motor_state)
        time.sleep(hold)

motor_state = MotorState(
    angle=0.0,
    velocity=0.0,
    acceleration=0.0,
    pattern_time=0.0,
    sub_patterns=[],
    color='black',
    width=2,
    active_instrument=None
)
motors_driver = MotorsDriver()

#raise_flag(1,3)
raise_flag(0,2,90,25)
time.sleep(2)
raise_flag(0,2,0,25)

print('End')
