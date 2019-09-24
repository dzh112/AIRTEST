import os
import time
from airtest.core.android.android import Android


# os.popen("adb shell dumpsys window policy |find \"ScreenOn\"").readline().split("=")[2].strip() true:亮屏  false：锁屏
# os.popen("adb shell input keyevent 26")  点击电源键

def get_app_level():
    res1 = os.popen("adb shell dumpsys battery |findstr level")
    level = res1.readline().split()[1].strip()
    print("手机电量: %s" % int(level))
    return level


def app_charge():
    #  app电量低于20%时，锁屏充电，充电完成后亮屏  锁屏方式为 无
    # 若锁屏方式为上划或密码，需要判断是否锁屏
    old_level = int(get_app_level())
    if old_level < 50:
        out_screen()
        time.sleep(1200)
        new_level = int(get_app_level())
        level_1 = new_level - old_level  # 充电二十分钟增加的电量
        print("充电二十分钟增加的电量: %s" % level_1)
        level_2 = 1200 / level_1  # 充满1%的电需要的时间
        print("充百分之一的电需要: %s 秒" % level_2)
        level_3 = (100 - new_level) * level_2  # 充满需要多少时间
        print("充满需要: %s 秒" % level_3)
        print("充电中……………………")
        time.sleep(level_3)
        bright_screen()
        time.sleep(10.0)


# 亮屏
def bright_screen():
    if Android().is_screenon():
        pass
    else:
        os.popen("adb shell input keyevent 26")  # 点击电源亮屏


# 灭屏
def out_screen():
    if Android().is_screenon():
        os.popen("adb shell input keyevent 26")  # 点击电源灭屏
    else:
        pass
