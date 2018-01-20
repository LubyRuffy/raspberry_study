# -*- coding:utf-8 -*-  
import RPi.GPIO as GPIO
from motor_controllor import *
from xiaomi_joystick import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

mc = MotorControllor( [
        [31, 33], # A
        [35, 37], # B
        [32, 36], # C
        [38, 40], # D
    ] )

xj = XiaomiJoystick()
xj.start(mc)
