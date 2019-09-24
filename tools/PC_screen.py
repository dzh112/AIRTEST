import os
import time

from airtest.core.android.adb import ADB

'''使用时请放到桌面，用命令行执行。多台测试机时，请开多个命令窗口。截图默认保存到桌面'''
# 命令：python .\PC_screen.py


def GetScreenbyADBCap(devices, screenpath, name):
    # 先给昵称赋值，防止生成图片的命名格式问题。
    if ":" in devices:
        nickname = devices.split(":")[1]
    else:
        nickname = devices
    print("screenpath=", screenpath)
    png = screenpath + "\\" + time.strftime("%Y%m%d_%H%M%S_",
                                            time.localtime(time.time())) + "_" + nickname + "_" + name + ".png"
    print("png=", png)
    os.system(" adb -s " + devices + " shell screencap -p /sdcard/01.png")
    time.sleep(1)
    fp = open(png, "a+", encoding="utf-8")
    fp.close()
    os.system(" adb -s " + devices + " pull /sdcard/01.png " + png)
    time.sleep(0.5)
    # ADB截图过大，需要压缩，默认压缩比为0.2，全屏。
    # compressImage(png)
    print("<img src='" + png + "' width=600 />")
    return png


if __name__ == '__main__':
    ad = ADB().devices()
    print("————————手机连接状态为offline时，请重新连接手机————————")
    len_ad = len(ad)
    global device1
    if len_ad == 0:
        print("未检测到手机")
    elif len_ad == 1:
        print("连接数为1")
        print("测试机device为:%s" % ad[0][0])
        device1 = ad[0][0]
    else:
        a = 0
        for i in ad:
            print(a, " ", i[0], " ", i[1])
            a = a + 1
        print("请输入测试机的编号0-%s:" % (a - 1))
        input_1 = input()
        print("测试机device为:%s" % ad[int(input_1)][0])
        device1 = ad[int(input_1)][0]  # 设备名称
    PC_path = os.path.join(os.path.expanduser("~"), 'Desktop')  # 保存路径：PC端桌面
    name = "app2019"  # 项目名称
    GetScreenbyADBCap(device1, PC_path, name)
    while True:
        print("是否需要继续（Y/N）:")
        jx = input()
        if jx.upper() == "Y":
            GetScreenbyADBCap(device1, PC_path, name)
        else:
            break
