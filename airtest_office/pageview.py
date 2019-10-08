import os

from PIL import Image
from airtest.core.android import Android
from airtest.core.api import snapshot, swipe

from airtest_office.BaseView import Base


class PageView(Base):
    def login(self):
        username = '13915575564'
        passname = 'zhang199412'
        self.poco("com.yozo.office:id/et_account").set_text(username)
        self.poco("com.yozo.office:id/et_pwd").set_text(passname)
        self.poco("com.yozo.office:id/btn_login").click()

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

    def skip_view(self):
        while not self.poco("com.yozo.office:id/ll_usednow").exists():
            swipe([1000, 500], [0, 500])
        self.poco("com.yozo.office:id/ll_usednow").click()

    def into_search_file(self):
        self.poco("com.yozo.office:id/im_title_bar_menu_search").click()

    def search_file(self, file_name):
        self.poco("com.yozo.office:id/et_search").set_text(file_name)
        self.poco("com.yozo.office:id/iv_search_search").click()

    def open_file(self, file_name):
        self.poco(text=file_name, name="com.yozo.office:id/tv_title").click()

    def wait_file_load_complete(self):
        file_option = self.poco("com.yozo.office:id/yozo_ui_option_group_button")
        button_close = self.poco("com.yozo.office:id/yozo_ui_toolbar_button_close")
        file_title_text = self.poco("com.yozo.office:id/yozo_ui_title_text_view")
        self.poco.wait_for_all([file_title_text, file_option, button_close], timeout=60)
        return file_title_text.get_text()

    def close_file(self):
        self.poco("com.yozo.office:id/yozo_ui_toolbar_button_close").click()


if __name__ == '__main__':
    print(os.getcwd())
