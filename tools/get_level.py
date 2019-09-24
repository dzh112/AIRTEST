import os

result = os.popen("adb shell dumpsys battery |findstr level")
level_val = result.readline().split()[1].strip()
print("手机电量: %s" % level_val)


