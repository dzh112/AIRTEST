import xlrd,re,os
from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class Base(object):

    def __init__(self):
        self.dev = '9613fafd'
        self.package_name = 'com.yozo.office'
        self.pro_path = ''.join(re.findall('(.*AIRTEST)', os.getcwd()))
        self.poco = AndroidUiautomationPoco(device=Android(self.dev), use_airtest_input=True,
                                            screenshot_each_action=False)
        self.example_file = '欢迎使用永中Office.docx'

    @staticmethod
    def excel_cols_list(sheet_path, sheet_name, col):
        book = xlrd.open_workbook(sheet_path)
        sheet = book.sheet_by_name(sheet_name)  # 获取第一个工作表
        return sheet.col_values(col)
