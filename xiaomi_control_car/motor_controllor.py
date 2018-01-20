# -*- coding:utf-8 -*-  
import RPi.GPIO as GPIO

# 电机控制类 可以是HG7881 也 可以是L298N
# 使用方法：
# mc = MotorControllor( [
#     [31, 33], # A 前左
#     [35, 37], # B 前右
#     [32, 36], # C 后左
#     [38, 40], # D 后右
# ] )
# 然后 mc.left() mc.right(), mc.forward(), mc.backword(), mc.stop就好了
class MotorControllor:
    def __init__(self, motors):
        self.motors = motors
        self.top_left = self.motors[0]
        self.top_right = self.motors[1]
        self.down_right = self.motors[2]
        self.down_left = self.motors[3]

        self.left_motors = [ self.top_left, self.down_left ]
        self.right_motors = [ self.top_right, self.down_right ]

        for motor in self.motors:
            self.init_motor(motor)

    # 初始化设置为输出引脚
    def init_motor(self, motor):
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    # 前进
    def forward(self):
        print("forward")
        for motor in self.motors:
            self.forward_motor(motor)

    # 后退
    def backward(self):
        print("backward")
        for motor in self.motors:
            self.backward_motor(motor)

    # 右转
    def right(self):
        print("right")
        for motor in self.left_motors:
            self.forward_motor(motor)
        for motor in self.right_motors:
            self.backward_motor(motor)

    # 坐转
    def left(self):
        print("left")
        for motor in self.right_motors:
            self.forward_motor(motor)
        for motor in self.left_motors:
            self.backward_motor(motor)

    # 停止
    def stop(self):
        print("stop")
        for motor in self.motors:
            for pin in motor:
                GPIO.output(pin, False)

    # 单个轮子前进
    def forward_motor(self, motor):
        GPIO.output(motor[0], True)
        GPIO.output(motor[1], False)

    # 单个轮子后退
    def backward_motor(self, motor):
        GPIO.output(motor[0], False)
        GPIO.output(motor[1], True)
