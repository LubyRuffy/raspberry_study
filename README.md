# raspberry_study
学习树莓派的一些小脚本

## s90_arm 目录：小米蓝牙手柄控制纸板机械臂
1. 安装引脚接好线，或者修改对应的引脚代码(arm_controller.py)，默认是从下而上对应15，13，11
2. 确保蓝牙手柄已经跟树莓派配对成功
3. 运行 python arm_controller.py

## xiaomi_control_car 目录：小米蓝牙手柄控制小车
1. 安装引脚接好线，或者修改对应的引脚代码(car.py)
2. 确保蓝牙手柄已经跟树莓派配对成功
3. 运行 python car.py

FAQ：
* 报错 UnboundLocalError: local variable 'xiaomidev' referenced before assignment
因为没有连接小米蓝牙手柄