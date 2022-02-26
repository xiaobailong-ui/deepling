'''
文件批量重命名
'''
import os

# 图片存放的路径
path = r"F:\1-pythonlearnning\16to8\16"
def Batch_rename(path):
    '''
    # 遍历更改文件名
    :param path:
    :return:
    '''
    num = 1
    for file in os.listdir(path):
        m = file.rindex('.')
        os.rename(os.path.join(path,file),os.path.join(path,str(num))+file[m:])
        num = num + 1
    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Batch_rename(path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
