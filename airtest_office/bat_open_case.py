import unittest
from airtest_office.pageview import PageView
from airtest.core.api import *
from ddt import ddt, data

pv = PageView()
pro_path = pv.pro_path
package = pv.package_name
print(pro_path)
sheet_path = os.path.join(pro_path, 'airtest_office', 'files_filter1_list.xls')
sheet_name = ['excel03', 'excel10', 'word03', 'word10', 'ppt03', 'ppt10']
files = pv.excel_cols_list(sheet_path, sheet_name[1], 1)[0:]


# files = ['wp_1.docx']


@ddt
class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        auto_setup(__file__, devices=["Android:///%s" % pv.dev])
        # connect_device("Android:///" + pv.dev)
        stop_app(package)
        start_app(package)
        pv.into_search_file()

    @classmethod
    def tearDownClass(cls):
        stop_app(package)

    def setUp(self):
        pass

    def tearDown(self):
        len1 = str(self).split(" ")[0]
        len2 = len1.split("_")[-1]
        len3 = len1.split("_")[-2]
        len_name = len3 + '.' + len2
        f = open(os.path.join(pro_path, 'test.txt'), 'a')
        f.write('\n%s' % len_name)
        f.close()
        # print(len_name)
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        wrong = error or failure

        if wrong:
            clear_app(package)
            start_app(package)
            pv.skip_view()
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
        assert_equal(pv.poco("com.yozo.office:id/et_search").wait(3).exists(), True, msg='open fail')
