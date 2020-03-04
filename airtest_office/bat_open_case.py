import unittest
import logging
from airtest_office.pageview import PageView
from airtest.core.api import *
from ddt import ddt, data

from tools.PC_screen import GetScreenbyADBCap

# from tools.get_level import get_level

pv = PageView()
package = pv.package_name
sheet_path = os.path.join(pv.project_root, 'airtest_office', 'files_filter1_list.xls')
sheet_name = ['excel03', 'excel10', 'word03', 'word10', 'ppt03', 'ppt10', '3000_1', '3000_2']
test_sheet = '3000_1'
col, start_rowx, end_rowx = 0, 0, 3000
files = pv.excel_cols_list(sheet_path, sheet_name[sheet_name.index(test_sheet)], col, start_rowx, end_rowx)
logging.info("选择工作表：%s" % test_sheet)
logging.info("第%d列，第%d行开始，第%d行结束" % (col + 1, start_rowx + 1, end_rowx))
logging.info("文件数量为：%s" % len(files))
logging.info("首行文件名：%s" % files[0])
logging.info("末行文件名：%s" % files[-1])
# logging.info('手机电量：%s' % get_level(pv.default_dev))
logging.info('\n')


# files = ['wp_1.docx']


@ddt
class StartEnd(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pv.unlocked()
    #     # stop_app(package)
    #     # start_app(package)
    #     # pv.into_search_file()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     stop_app(package)

    def setUp(self):
        # pass
        # pv.unlocked()
        stop_app(package)
        start_app(package)

    def tearDown(self):

        # print(len_name)
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        wrong = error or failure
        # len1 = str(self).split(" ")[0]
        # len2 = len1.split("_")[-1]
        # len3 = len1.split("_")[-2]
        # len_name = len3 + '.' + len2

        if wrong:
            logging.info('fail:%s' % pv.load_file_name)
            # stop_app(package)
            # start_app(package)
            # # # pv.skip_view()
            # pv.into_search_file()

            # 保存截图到桌面
            # PC_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
            # GetScreenbyADBCap(screenpath=PC_path, name=self.string_change_path_name(pv.load_file_name),
            #                   dev=pv.default_dev)
        else:
            logging.info('pass:%s' % pv.load_file_name)
        stop_app(package)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    # @data(*files)
    # def test_bat_open_files(self, filename):  # 搜索、打开、另存、校验、关闭
    #     pv.load_file_name = filename
    #     pv.into_search_file()
    #     pv.search_file(filename)
    #     pv.open_file(filename)
    #     pv.close_file()
    #     # if '000.' in filename:
    #     #     logging.info('手机电量：%s' % get_level(pv.default_dev))
    #     assert_equal(pv.poco("com.yozo.office:id/et_search").wait(3).exists(), True, msg='open fail')

    @data(*files)
    def test_bat_save_as(self, filename):  # 搜索、打开、另存、校验、关闭
        try:
            pv.load_file_name = filename
            pv.into_search_file()
            pv.search_file(filename)
            pv.open_file(filename)
            save_result = pv.save_as_home_path_and_close()
            pv.search_file(save_result[0])
            pv.open_file(save_result[0])
            pv.wait_file_title()
            # save_as_png = pv.poco_screenshots("com.yozo.office:id/yozo_ui_app_frame_office_view_container",
            #                                   r'F:\AIRTEST\changepng\save_app_frame_screen.png')
            assert_exists(
                Template(r'F:\AIRTEST\changepng\load_app_frame_screen.png', rgb=True, record_pos=(-0.249, -0.15),
                         resolution=(720, 1280)), msg='另存截图对比失败')
            pv.close_file()
        except Exception as e:
            logging.info(e)
            raise

    @staticmethod
    def string_change_path_name(str_name=''):
        list_str_name = list(str_name)
        for index, i in enumerate(list_str_name):
            if not (i.isdigit() or i.isalpha()):
                list_str_name[index] = "_"
        str_name = ''.join(list_str_name)
        return str_name


if __name__ == '__main__':
    unittest.main()
