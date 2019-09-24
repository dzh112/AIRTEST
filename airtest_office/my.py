import unittest
from airtest_office.pageview import PageView
from airtest.core.api import *

auto_setup(__file__)
pv = PageView()
connect_device("Android:///" + pv.dev)


class StartEnd(unittest.TestCase):
    def setUp(self):
        start_app(pv.package_name)

    def tearDown(self):
        stop_app(pv.package_name)

    def test_open_file(self, filename=pv.example_file):  # 搜索、打开、关闭
        pv.search_file(filename)
        pv.open_file(filename)
        file_frame_title = pv.wait_file_load_complete()
        self.assertEqual(file_frame_title, filename, msg='%s open fail' % filename)
        pv.close_file()
