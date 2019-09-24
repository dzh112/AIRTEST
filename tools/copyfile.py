import xlrd
import shutil
import os

# 在文件夹内查找excel内的文档名称，并将其拷贝到其他路径下
if __name__ == '__main__':
    # 查找文件路径
    path = r'D:\20190517\移动事业部_自动化\文档集合\自动化测试文件列表\ppt10'
    # 其他文件目录
    other_path = r'D:\20190517\临时目录\BUG库\0923'
    # 错误文档工作薄
    PC_path = os.path.join(os.path.expanduser("~"), 'Desktop', '2019_09_23_09_00_57.xls')
    book = xlrd.open_workbook(PC_path)
    sheet = book.sheet_by_index(2)  # 获取第一个工作表
    s = sheet.col_values(0)
    for i in s:
        old_path = os.path.join(path, i)
        print(old_path)
        shutil.copy(old_path, other_path)

    # cols = sheet.ncols  # 获取列数
    # for c in range(cols):  # 读取每一列的数据
    # #     c_values = sheet.col_values(c)
    # #     print(c_values)
