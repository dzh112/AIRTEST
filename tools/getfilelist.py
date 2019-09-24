import os


def get_filename_list(text_path, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            f = open(text_path, "a+", encoding='utf-8')
            f.writelines("".join(file) + '\n')
            f.close()


# 批处理 遍历PC端文件夹内的文件名到txt中
if __name__ == '__main__':
    path_1 = 'D:\\20190517\\APP2019_currency\\Data\\file_list.txt'
    # path_2 = '../Res/ScreenShots'
    path_2 = r"D:\error_excel03"
    get_filename_list(path_1, path_2)
