#!/usr/bin/env python    
# -*- coding:utf-8 -*-      
from raspi_sg90 import *
from xiaomi_joystick import *
import threading

class ArmControllor:
    def __init__(self, down_sg90, middle_sg90, up_sg90):
        self.down_sg90 = [0, sg90( down_sg90, 0 ), "down", "stop"]
        self.down_sg90[1].setdirection( 0, 50 )
        self.middle_sg90 = [0, sg90( middle_sg90, 0 ), "middle", "stop" ]
        self.middle_sg90[1].setdirection( 0, 50 )
        self.up_sg90 = [0, sg90( up_sg90, 0 ), "up", "stop" ]
        self.up_sg90[1].setdirection( 0, 50 )

    def down_left(self):
        if self.down_sg90[3] == "stop":
            threading.Thread(target = self.sg90_move_left, args = (self.down_sg90, ) ).start()
        # self.sg90_move_left(self.down_sg90)

    def down_right(self):
        if self.down_sg90[3] == "stop":
            threading.Thread(target = self.sg90_move_right, args = (self.down_sg90, ) ).start()
        # self.sg90_move_right(self.down_sg90)

    def down_stop(self):
        print("stop")
        self.down_sg90[3] = "stop"

    def middle_left(self):
        if self.middle_sg90[3] == "stop":
            threading.Thread(target = self.sg90_move_left, args = (self.middle_sg90, ) ).start()
        # self.sg90_move_left(self.middle_sg90)

    def middle_right(self):
        if self.middle_sg90[3] == "stop":
            threading.Thread(target = self.sg90_move_right, args = (self.middle_sg90, ) ).start()
        # self.sg90_move_right(self.middle_sg90)

    def middle_stop(self):
        print("stop")
        self.middle_sg90[3] = "stop"

    def up_left(self):
        if self.up_sg90[3] == "stop":
            threading.Thread(target = self.sg90_move_left, args = (self.up_sg90, ) ).start()
        # self.sg90_move_left(self.up_sg90)

    def up_right(self):
        if self.up_sg90[3] == "stop":
            threading.Thread(target = self.sg90_move_right, args = (self.up_sg90, ) ).start()
        # self.sg90_move_right(self.up_sg90)

    def up_stop(self):
        print("stop")
        self.up_sg90[3] = "stop"

    def sg90_move_left(self, sg90_info):
        sg90_info[3] = "left"
        print (sg90_info[2], sg90_info[3])
        while True:
            if sg90_info[0] >= 100:
                break
            sg90_info[0] += 5 
            sg90_info[1].setdirection( sg90_info[0], 5 )
            print (sg90_info[2], sg90_info[0])
            time.sleep(0.1)
            if sg90_info[3] == "stop":
                break
        print (sg90_info[2], "stopped") 
        sg90_info[3] = "stop"

    def sg90_move_right(self, sg90_info):
        sg90_info[3] = "right"
        print (sg90_info[2], sg90_info[3])
        while True:
            if sg90_info[0] <= -100:
                break
            sg90_info[0] -= 5 
            sg90_info[1].setdirection( sg90_info[0], -5 )
            print (sg90_info[2], sg90_info[0])
            time.sleep(0.1)
            if sg90_info[3] == "stop":
                break
        print (sg90_info[2], "stopped")
        sg90_info[3] = "stop"

if __name__ == "__main__":
    armc = ArmControllor(15, 13, 11)
    xj = XiaomiJoystick()
    xj.start(armc)