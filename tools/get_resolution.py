# 获取屏幕分辨率
# 第一种方法
import os

# result1 = os.popen("adb shell wm size").read()
# va = result1.split()[2]
# va2 = va.split("x")
# # x,y 为屏幕分辨率
# x = int(va2[0])
# y = int(va2[1])

# 第二种方法
from airtest.core.android import Android
app_info = Android().get_display_info()
print(app_info['width'])
print(app_info['height'])
# print(x,y)
