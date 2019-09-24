from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class Base(object):

    def __init__(self):
        self.dev = 'db798018'
        self.package_name = 'com.yozo.office'
        self.poco = AndroidUiautomationPoco(device=Android(self.dev), use_airtest_input=True,
                                            screenshot_each_action=False)
        self.example_file = '欢迎使用永中Office.docx'
