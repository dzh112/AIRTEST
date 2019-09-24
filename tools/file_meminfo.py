from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
'''导出文件名到filelist.txt中，使用此脚本计算每篇文档所占用内存'''
# def get_package():
#     print('输入文档类型:')
#     print('1: wp')
#     print('2: ss')
#     print('3: pg')
#     wps = input()
#     command = ''
#     if wps == '1':
#         print('文档类型为：word')
#         command = "adb shell dumpsys meminfo cn.wps.moffice_eng:writer1"
#     elif wps == '2':
#         print('文档类型为：excel')
#         command = "adb shell dumpsys meminfo cn.wps.moffice_eng:spreadsheet1"
#     elif wps == '3':
#         print('文档类型为：ppt')
#         command = "adb shell dumpsys meminfo cn.wps.moffice_eng:presentation1"
#     return command
from appium.webdriver.extensions.android.activities import Activities


def get_allocated_memory(adb_command=''):
    adb_memory_re = os.popen(adb_command)
    list = []
    for line in adb_memory_re:
        line = line.strip()
        list = line.split(' ')
        if list[0] == "TOTAL":
            while '' in list:
                list.remove('')
            # allocated_memory = format(int(list[1]) / 1024, ".2f")
            allocated_memory = int(list[1])
            return allocated_memory


def memory_result(command_r):
    global a
    for i in range(50):
        a = get_allocated_memory(command_r)
        b = get_allocated_memory(command_r)
        c = get_allocated_memory(command_r)
        if abs(a - b) < 5000 and abs(b - c) < 5000:
            break
    return a


def open_office_file(name):
    stop_app(test_package_name)
    start_app(test_package_name)
    poco("com.yozo.office:id/im_title_bar_menu_search").click()
    poco("com.yozo.office:id/et_search").set_text(name)
    poco("com.yozo.office:id/iv_search_search").click()
    poco(name='com.yozo.office:id/tv_title', text=name).click()
    try:
        poco("com.yozo.office:id/yozo_ui_title_text_view").wait_for_appearance(60)
        time.sleep(5)
        cc = (name, memory_result(command))
    except:
        cc = ('文件打开超时', '文件打开超时')
    print(cc)
    list_memory_result.append(cc)


if __name__ == '__main__':
    list_memory_result = []
    device_name = 'db798018'
    sheet_title = ('文件名', '占用内存')
    list_memory_result.append(sheet_title)
    test_package_name = 'com.yozo.office'  # 文档所在包名（一个app可能有多个包名：adb shell dumpsys meminfo）
    command = "adb -s %s shell dumpsys meminfo %s" % (device_name, test_package_name)
    auto_setup(__file__)
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    # connect_device('android:///?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH')
    connect_device('android:///'+device_name)
    pc_path = os.path.join(os.getcwd(), 'filelist.txt')
    a = open(pc_path).readlines()
    for i in a:
        open_office_file(i.replace('\n', ''))
    # print(list_memory_result)
    for i in list_memory_result:
        print(i)
