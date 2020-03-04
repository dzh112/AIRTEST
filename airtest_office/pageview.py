from PIL import Image
from airtest.core.android import Android
from airtest.core.api import *
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

        if '.png' not in save_as_path:
            save_as_path = os.path.join(save_as_path, 'pic.png')
        cropped.save(save_as_path)
        os.remove(image_path)  # 删除原图
        return save_as_path

    def skip_view(self):
        while not self.poco("com.yozo.office:id/ll_usednow").exists():
            swipe([1000, 500], [0, 500])
        self.poco("com.yozo.office:id/ll_usednow").click()

    def into_search_file(self):
        self.poco("com.yozo.office:id/im_title_bar_menu_search").click()

    def search_file(self, file_name):
        self.poco("com.yozo.office:id/et_search").set_text(file_name)
        # self.poco("com.yozo.office:id/iv_search_search").click()

    def open_file(self, file_name):
        self.poco(text=file_name, name="com.yozo.office:id/tv_title").click()

    def save_as_home_path_and_close(self):
        app_frame_screen = self.poco_screenshots("com.yozo.office:id/yozo_ui_app_frame_office_view_container",
                                                 r'F:\AIRTEST\changepng\load_app_frame_screen.png')
        if self.poco("com.yozo.office:id/yozo_ui_option_group_button").get_text() != '文件':
            self.poco("com.yozo.office:id/yozo_ui_option_group_button").click()
            self.poco(text='文件').click()
        else:
            self.poco("com.yozo.office:id/yozo_ui_option_expand_button").click()
        suff = os.path.splitext(self.poco("com.yozo.office:id/yozo_ui_title_text_view").get_text())[1]
        self.poco("com.yozo.office:id/yozo_ui_ss_option_id_save_as").click()
        self.poco("com.yozo.office:id/yozo_ui_select_save_folder").click()
        self.poco("com.yozo.office:id/yozo_ui_select_save_path_local").click()
        self.poco("com.yozo.office:id/yozo_ui_select_save_path_file_name").set_text('save_as_home')
        self.poco("com.yozo.office:id/yozo_ui_select_save_path_file_type").click()

        # 选择同类型保存
        if self.poco("com.yozo.office:id/file_type_item1").get_text() == suff:
            self.poco("com.yozo.office:id/file_type_item1").click()
        else:
            self.poco("com.yozo.office:id/file_type_item2").click()
        self.poco("com.yozo.office:id/yozo_ui_select_save_path_save_btn").click()
        if self.poco("android:id/button1").exists():
            self.poco("android:id/button1").click()
        self.poco("com.yozo.office:id/yozo_ui_title_text_view").wait_for_appearance()
        self.poco("com.yozo.office:id/yozo_ui_toolbar_button_close").click()
        # 返回值：另存为文件名，内容截图路径
        return 'save_as_home' + suff, app_frame_screen

    def close_file(self):

        if self.poco("com.yozo.office:id/password_edit").exists():
            self.poco("com.yozo.office:id/cancel_btn").click()
        else:
            self.poco("com.yozo.office:id/yozo_ui_toolbar_button_close").wait_for_appearance(timeout=120)
            self.poco("com.yozo.office:id/yozo_ui_toolbar_button_close").click()
        if self.poco(text='不保存').exists():
            self.poco(text='不保存').click()

    def wait_file_title(self):
        self.poco("com.yozo.office:id/yozo_ui_title_text_view").wait_for_appearance(timeout=60)

    def unlocked(self):
        while not Android().is_screenon():
            wake()
            while Android().is_locked():
                self.poco("com.android.systemui:id/unlock_indicator").swipe([0.0, -1])

    @staticmethod
    def fail_file_choose():
        data0 = []
        for line in open(r'F:\AIRTEST\logs\runlog.log', 'r'):
            if 'fail' in line:
                data0.append(line)
                # data0.append(line)
        return data0

    @staticmethod
    def walkfile(file):
        list1 = []
        for root, dirs, files in os.walk(file):

            # root 表示当前正在访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list

            # 遍历文件

            for f in files:
                list1.append(os.path.join(root, f))
        return list1
        # # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))


if __name__ == '__main__':

    f = open(r'F:\AIRTEST\logs\runlog.log', 'a')
    f.write('\n')
    for i in PageView.fail_file_choose():
        f.write(i)
    f.close()
