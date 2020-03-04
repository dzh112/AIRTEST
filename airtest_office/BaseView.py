import xlrd
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco



class Base(object):

    def __init__(self):
        self.default_dev = 'KZI7SCLR99999999'
        self.package_name = 'com.yozo.office'
        self.project_root = os.path.dirname(os.path.dirname(__file__))
        self.dev = connect_device("Android:///"+"%s" % self.default_dev)
        self.poco = AndroidUiautomationPoco(device=self.dev,use_airtest_input=True,
                                            screenshot_each_action=False)
        self.load_file_name =' '
        self.example_file = '欢迎使用永中Office.docx'

    @staticmethod
    def excel_cols_list(sheet_path, sheet_name, col, start_rowx=0, end_rowx=None):
        book = xlrd.open_workbook(sheet_path)
        sheet = book.sheet_by_name(sheet_name)  # 获取第一个工作表
        # col 列号,start_rowx 起始行,end_rowx 结束行
        files = sheet.col_values(col, start_rowx, end_rowx)

        # fi = 0
        # for i in files:
        #     if len(i) == 0:
        #         fi = files.index(i)
        #         break
        return files


if __name__ == '__main__':
    print(Base().project_root)
