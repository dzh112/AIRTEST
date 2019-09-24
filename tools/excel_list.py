import os
import xlrd
import xlwt

'''表格列转为数组'''
PC_path = os.path.join(os.path.expanduser("~"), 'Desktop', '自行车.xlsx')
book = xlrd.open_workbook(PC_path)
sheet = book.sheet_by_index(0)  # 获取第一个工作表
cols = sheet.ncols  # 获取列数
# for c in range(cols):  # 读取每一列的数据
# #     c_values = sheet.col_values(c)
# #     print(c_values)
print(sheet.col_values(0))
