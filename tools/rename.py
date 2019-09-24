import os


def rename_file(folder_path):
    num = 1
    os.chdir(folder_path)
    for file in os.listdir(folder_path):
        file_num = str(num)
        while len(file_num) < 5:
            file_num = '0' + file_num
        suffix = os.path.splitext(file)[1]
        new_name = file_num + suffix
        os.rename(file, new_name)
        num += 1


# 将目标文件夹内文件进行重命名
if __name__ == '__main__':
    path = r'D:\20190517\临时目录\新建文件夹'
    rename_file(path)
