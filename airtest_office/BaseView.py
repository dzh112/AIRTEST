import xlrd
from airtest.core.android import Android
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from PIL import Image


class Base(object):

    def __init__(self):
        self.dev = 'db798018'
        self.package_name = 'com.yozo.office'
        self.poco = AndroidUiautomationPoco(device=Android(self.dev), use_airtest_input=True,
                                            screenshot_each_action=False)
        self.example_file = '欢迎使用永中Office.docx'

    def login(self):
        username = '13915575564'
        passname = 'zhang199412'
        self.poco("com.yozo.office:id/et_account").set_text(username)
        self.poco("com.yozo.office:id/et_pwd").set_text(passname)
        self.poco("com.yozo.office:id/btn_login").click(sleep_interval=3)

    def poco_screenshots(self, p_value, save_as_path):
        # 元素截图
        image_path = "d:\\screen.png"
        snapshot(image_path)  # 将当前截图保存到image_path
        img = Image.open(image_path)  # 打开图片：image_path
        # 获取手机分辨率
        app_info = Android().get_display_info()
        # x,y 为屏幕分辨率
        x = int(app_info['width'])
        y = int(app_info['height'])
        a, b, c, d = self.poco(p_value).get_bounds()
        cropped = img.crop((x * d, y * a, x * b, y * c))  # (left, upper, right, lower)
        print("_________________________________________")
        if '.png' not in save_as_path:
            save_as_path = os.path.join(save_as_path, 'pic.png')
        cropped.save(save_as_path)
        os.remove(image_path)  # 删除原图

    @staticmethod
    def excel_cols_list(sheet_path, sheet_name, col):
        book = xlrd.open_workbook(sheet_path)
        sheet = book.sheet_by_name(sheet_name)  # 获取第一个工作表
        return sheet.col_values(col)
