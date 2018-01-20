# -*- coding:utf-8 -*-  
import evdev

# 小米蓝牙手柄控制马达
# start的方法中传递MotorControllor实例
# 左右方向盘控制左右方向
# X键前进，A键后退
# 左右方向的优先级高于前进后退
class XiaomiJoystick:
    def __init__(self, name='小米蓝牙手柄'):
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in devices:
            print(device)
            if device.name == name:
                xiaomidev = device.fn

        print("=======")

        self.gamepad = evdev.InputDevice(xiaomidev)
        print(self.gamepad)
        print(self.gamepad.capabilities(verbose=True))

        print("=======")

    def start(self, mc):
        xy_is_hold = False # 是否方向键一直按着
        for event in self.gamepad.read_loop():
            if event.type == evdev.ecodes.EV_ABS: # 方向
                if event.code == 0: # 0是X， 1是Y
                    xy_is_hold = True
                    if event.value > 128:
                        mc.right()
                    elif event.value < 128:
                        mc.left()
                    else:
                        xy_is_hold = False
                        print("no xy hold, check key press")
                continue

            # 如果一直按着，按键无效
            if xy_is_hold:
                continue

            if event.type == 1: # 按键
                if event.code == 307: # X是307，Y是308，A是304，B是305
                    if event.value > 1:
                        mc.forward()
                    elif event.value == 0:
                        mc.stop()
                elif event.code == 304: # X是307，Y是308，A是304，B是305
                    if event.value > 1:
                        mc.backward()
                    elif event.value == 0:
                        mc.stop()
                continue
            
            if len(self.gamepad.active_keys()) == 0:
                mc.stop()
                
            if event.type != evdev.ecodes.EV_SYN and event.type != 4: 
                print "+++"
                print(event.type)
                print(event.code)
                print(event.value)
                print(evdev.categorize(event))
                print(repr(event))
                print "---"
    