import shutil
import unittest
import logging
from airtest_office.pageview import PageView
from airtest.core.api import *
from ddt import ddt, data

# '11000-11999',
# '12000-12999',
# '13000-13999',
# '14000-14999',
# '15000-15999',
# '16000-16999',
# '17000-17999',
# '18000-18999',
# '19000-19999',

pv = PageView()
package = pv.package_name
all_file_path = []
file_dir = ['其他']
test_path = r'E:\MSfiles\MS2007files\xlsx'


def dir_list(folder1):
    path1 = os.path.join(r'E:\MSfiles\MS2007files\xlsx', folder1)
    file_names1 = []
    for root, dirs, files in os.walk(path1):
        for f in files:
            file_names1.append(f)
    return file_names1


for i in file_dir:
    all_file_path.extend(dir_list(i))


@ddt
class OpenFiles(unittest.TestCase):

    def setUp(self):
        stop_app(package)
        start_app(package)
        sleep(3)

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        wrong = error or failure
        if wrong:
            logging.info('fail:%s' % pv.load_file_name)
            # 保存截图到桌面
            # PC_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
            # GetScreenbyADBCap(screenpath=PC_path, name=self.string_change_path_name(pv.load_file_name),
            #                   dev=pv.default_dev)
            wrong_file_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
            for i in file_dir:
                path2 = os.path.join(test_path, i, pv.load_file_name)
                if os.path.isfile(path2):
                    shutil.copy(path2, wrong_file_path)
                    break
        else:
            logging.info('pass:%s' % pv.load_file_name)
        stop_app(package)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    @data(*all_file_path)
    def test_a_bat_open_files(self, file_name):
        pv.load_file_name = file_name
        logging.info('==========正在打开%s==========' % file_name)
        try:
            type1 = os.path.splitext(file_name)[1]
            if type1 != '.xls' and type1 != '.xlsx':
                raise Exception("文件格式为%s" % type1)
            pv.into_search_file()
            pv.search_file(os.path.splitext(file_name)[0])
            sleep(3)
            pv.open_file(file_name)
            pv.close_file()
            pv.poco("com.yozo.office:id/et_search").wait_for_appearance(timeout=30)
        except Exception as e:
            if pv.poco("android:id/message").exists():
                logging.info('%s' % pv.poco("android:id/message").get_text())
                if pv.poco("android:id/button1").exists():
                    pv.poco("android:id/button1").click()
                raise
            else:
                logging.info(e)
                raise


if __name__ == '__main__':
    unittest.main()
