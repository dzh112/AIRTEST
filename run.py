import os
import unittest
import time

from BeautifulReport import BeautifulReport  # 导入BeautifulReport

from airtest_office.send_email_all import SendMail

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    suite_tests = unittest.defaultTestLoader.discover("./airtest_office", pattern="bat_open_case.py",
                                                      top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='测试报告' + now, description='批量打开测试',
                                        report_dir='reports')  # log_path='.'把report放到当前目录下
    m = SendMail(
        email_host='*',
        username='*', passwd='*',
        recv='*',
        title='测试完成',
        content="手机电量: %s" % os.popen("adb shell dumpsys battery |findstr level").readline().split()[1].strip(),
        test_report=r'F:\AIRTEST\reports'
    )
    m.send_mail()
