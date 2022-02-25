# 将标签图从json文件中批量取出
import os
import shutil

path = r'E:\yuanshi'        # json文件夹所在位置
dirpath = 'E:\ceshi'        # 将标签图从json文件中批量取出后指定保存的文件目录

for eachfile in os.listdir(path):
    path1=os.path.join(path,eachfile)  #获取单个json文件夹的目录
    if os.path.isdir(path1):
        if os.path.exists(path1 + '/label.png'):
            path1 = os.path.join(path1,'label.png')   #获取PNG所在的路径，准备等待复制
            path2 = os.path.join(dirpath,(eachfile.split('_')[0] + '.png'))  #将png复制到path2路径下的文件夹中去
            shutil.copy(path1, path2)
            print(eachfile + ' successfully moved')
