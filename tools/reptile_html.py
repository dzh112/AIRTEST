# -*- coding:UTF8 -*-

import re
import requests


# import urllib.request


# pattern = re.compile(r'data-objurl="(.*)"')  # 查找数字
# result1 = pattern.findall('data-objurl="http://pic.kekenet.com/2018/0107/8121515325256.jpg"')
# urllib.request.urlretrieve(result1[0], '1.png')
#
#
# print(result1)


def find(url1):
    html = requests.get(url1, timeout=7).text
    pa = re.compile('data-tools=\'{"title":"(.*?)","url":"(.*?)"}')
    tilte = pa.findall(html)
    list(map(lambda x: print(x), tilte))



if __name__ == '__main__':
    search_text = input("请输入搜索关键字：")
    url = 'http://www.baidu.com/s?wd=%s' % search_text
    find(url)
