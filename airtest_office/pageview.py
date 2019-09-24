from airtest_office.BaseView import Base


class PageView(Base):
    def search_file(self, file_name):
        self.poco("com.yozo.office:id/im_title_bar_menu_search").click()
        self.poco("com.yozo.office:id/et_search").set_text(file_name)
        self.poco("com.yozo.office:id/iv_search_search").click()

    def open_file(self, file_name):
        self.poco(text=file_name, name="com.yozo.office:id/tv_title").click()

    def wait_file_load_complete(self):

        file_option = self.poco("com.yozo.office:id/yozo_ui_option_group_button")
        button_close = self.poco("com.yozo.office:id/yozo_ui_toolbar_button_close")
        file_title_text = self.poco("com.yozo.office:id/yozo_ui_title_text_view")
        self.poco.wait_for_all([file_title_text, file_option, button_close])
        return file_title_text.get_text()

    def close_file(self):
        self.poco("com.yozo.office:id/yozo_ui_toolbar_button_close").click()
