import unittest
from airtest_office.pageview import PageView
from airtest.core.api import *
from ddt import ddt, data

pv = PageView()
sheet_path = os.path.join(os.getcwd(), 'files_filter1_list.xls')
sheet_name = ['excel03', 'excel10', 'word03', 'word10', 'ppt03', 'ppt10']
files = pv.excel_cols_list(sheet_path, sheet_name[0], 0)


@ddt
class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        auto_setup(__file__)
        connect_device("Android:///" + pv.dev)
        start_app(pv.package_name)
        pv.into_search_file()

    @classmethod
    def tearDownClass(cls):
        stop_app(pv.package_name)

    def setUp(self):
        pass

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        wrong = error or failure
        if wrong:
            stop_app(pv.package_name)
            start_app(pv.package_name)
            pv.into_search_file()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    @data(*files)
    def test_bat_open_files(self, filename):  # 搜索、打开、关闭
        pv.search_file(filename)
        pv.open_file(filename)
        pv.wait_file_load_complete()
        pv.close_file()
        time.sleep(3)
        assert_equal(pv.poco("com.yozo.office:id/et_search").exists(), True, msg='open fail')
