# 读数据
import os

import xlrd
import xlwt

'''友盟导出数据另存为office埋点统计.xlsx后，使用次脚本筛选'''


# 命令：python .\PC_screen.py

def read_excel(filename, thing):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)  # 获取第一个工作表
    # sheet = book.sheet_by_name('1') # 获取工作表名称为1的工作表
    rows = sheet.nrows  # 获取行数
    # cols = sheet.ncols  # 获取列数
    # for c in range(cols):  # 读取每一列的数据
    #     c_values = sheet.col_values(c)
    #     print(c_values)
    list1 = []
    for r in range(rows):  # 读取每一行的数据
        if thing in sheet.row_values(r):
            r_values = sheet.row_values(r)
            # print(r_values)
            list1.append(r_values)
    a = b = 0
    print('事件ID：%s' % thing)
    if len(list1) == 0:
        return thing, "未读取到该事件", 0, 0
    print('事件名称：', list1[0][3])
    for i1 in range(len(list1)):
        a += list1[i1][4]
        b += list1[i1][5]
    print('消息数量为：%s' % a)
    print('独立用户数为：%s' % b)
    return thing, list1[0][3], a, b

    # print(sheet.cell(1, 1))  # 读取指定单元格的数据


# 写数据
def write_excel(filename, data):
    book = xlwt.Workbook(filename)  # 创建excel对象

    sheet = book.add_sheet('筛选结果')  # 添加一个表
    c = 0  # 保存当前列
    for d in data:  # 取出data中的每一个元组存到表格的每一行
        for index in range(len(d)):  # 将每一个元组中的每一个单元存到每一列
            sheet.write(c, index, d[index])
        c += 1
    book.save(filename)  # 保存excel


if __name__ == '__main__':
    # 导出数据另存为（office埋点统计.xlsx）到桌面，工作表重命名为1
    list_sheet = []
    list_a = ['OFFICE_SIGN_EDIT_WP', 'OFFICE_SIGN_EDIT_SS', 'OFFICE_SIGN_EDIT_PG', 'OFFICE_SIGN_PLAY_PG',
              'OFFICE_SIGN_TRANSITION_PG', 'OFFICE_FILE_REVESION_WP', 'OFFICE_INSERT_TABLE_WP',
              'OFFICE_INSERT_TABLE_PG', 'OFFICE_WP_SAVE', 'OFFICE_WP_SAVE_AS_LOCAL', 'OFFICE_WP_SAVE_AS_CLOUD',
              'OFFICE_SS_SAVE', 'OFFICE_SS_SAVE_AS_LOCAL', 'OFFICE_SS_SAVE_AS_CLOUD', 'OFFICE_WP_EXPORT_PDF',
              'OFFICE_PG_EXPORT_PDF', 'OFFICE_FILE_CLOSE_SAVE_WP', 'OFFICE_FILE_CLOSE_SAVE_SS',
              'OFFICE_FILE_CLOSE_SAVE_PG', 'OFFICE_FILE_CLOSE_NOT_SAVE_WP', 'OFFICE_FILE_CLOSE_NOT_SAVE_SS',
              'OFFICE_FILE_CLOSE_NOT_SAVE_PG', 'OFFICE_SHARE_FILE_WP_WECHAT', 'OFFICE_SHARE_FILE_WP_QQ',
              'OFFICE_SHARE_FILE_WP_DINGDING', 'OFFICE_SHARE_FILE_WP_EMAIL', 'OFFICE_SHARE_FILE_SS_WECHAT',
              'OFFICE_SHARE_FILE_SS_QQ', 'OFFICE_SHARE_FILE_SS_DINGDING', 'OFFICE_SHARE_FILE_SS_EMAIL',
              'OFFICE_SHARE_FILE_PG_WECHAT', 'OFFICE_SHARE_FILE_PG_QQ', 'OFFICE_SHARE_FILE_PG_DINGDING',
              'OFFICE_SHARE_FILE_PG_EMAIL', 'HOME_MODIFY_NAME', 'HOME_ABOUT_YOZO', 'HOME_MODIFY_EMAIL',
              'HOME_ENTER_SDCARD_DIRECTORY', 'HOME_FILE_SEARCH', 'HOME_FILE_SORT_BY_TYPE', 'HOME_FILE_SORT_BY_NAME',
              'HOME_FILE_SORT_BY_SIZE', 'HOME_FILE_SORT_BY_TIME', 'HOME_ENTER_RECENT_PAGE', 'HOME_ENTER_CLOUD_PAGE',
              'HOME_ENTER_STAR_PAGE', 'HOME_ENTER_MY_PAGE', 'HOME_SIGN_OUT', 'HOME_OPEN_LOCAL_FILE',
              'HOME_OPEN_CLOUD_FILE', 'HOME_OPEN_RECENT_FILE', 'HOME_OPEN_STAR_FILE', 'HOME_FILE_UPLOAD',
              'HOME_FILE_DOWNLOAD', 'HOME_FILE_STAR', 'HOME_FILE_CANCEL_STAR', 'HOME_FILE_DELET_LOCAL',
              'HOME_FILE_DELET_CLOUD', 'HOME_FILE_DELET_RECENT', 'HOME_SHARE_FILE_WECHAT', 'HOME_SHARE_FILE_QQ',
              'HOME_SHARE_FILE_DINGDING', 'HOME_SHARE_FILE_EMAIL', 'HOME_FILE_INFO_READ', 'HOME_FILE_MULTIPLE_CHOICE',
              'HOME_NEW_FILE_WP', 'HOME_NEW_FILE_SS', 'HOME_NEW_FILE_PG', 'OFFICE_EDIT_WP', 'OFFICE_EDIT_SS',
              'OFFICE_EDIT_PG', 'OFFICE_INSPECT_WP', 'OFFICE_INSPECT_SS', 'OFFICE_INSERT_OBJECT_WP',
              'OFFICE_INSERT_OBJECT_SS', 'OFFICE_INSERT_OBJECT_PG', 'OFFICE_FORMULA_EDIT_SS', 'HOME_FIND_PASSWORD',
              'HOME_REGISTER_ACCOUNT', 'HOME_MESSAGE_LOGIN', 'HOME_ACCOUNT_LOGIN', 'HOME_WECHAT_LOGIN',
              'HOME_ENTER_HOME_PAGE', 'ENTER_BY_OA', 'REVISE_MODE', 'SIGN_MODE', 'EDIT_MODE', 'NEW_FILE', 'OPEN_FILE',
              'SAVE_AS', 'SAVE']

    PC_path = os.path.join(os.getcwd(), 'Excel', 'office埋点统计.xlsx')
    PC_result_path = os.path.join(os.getcwd(), 'Excel', '筛选结果.xlsx')
    for i in list_a:
        list_sheet.append(read_excel(PC_path, i))
    list_sheet.insert(0, ('事件Id', '事件名称', '消息数量', '独立用户数'))
    print(list_sheet)
    write_excel(PC_result_path, list_sheet)
