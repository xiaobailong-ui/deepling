#
import cv2
import os
import numpy as np
from PIL import Image


def pic_compress_png(image_path,new_image_path):
    '''
    将图片压缩成png格式
    :param image_path:  原始文件路径
    :param new_image_path:  保存文件路径
    :return:
    '''
    files = os.listdir(image_path)  # 获取当前路径下的所有文件名字
    files = np.sort(files)         #按名称排序
    i = 0
    for f in files:
        imgpath = image_path + f   #路径+文件名字
        img = cv2.imread(imgpath, 1)   #读取图片
        dirpath = new_image_path       #压缩后存储路径
        file_name, file_extend = os.path.splitext(f)   #将文件名的，名字和后缀进行分割
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.png')  #文件最终保存的路径及名字（名字和压缩前的名字一致），
        print(os.path.join(dirpath,"1.png"))  #打印压缩缓存文件路径
        shrink = cv2.resize(img, (4864,1024), interpolation = cv2.INTER_AREA) #对图像的大小进行resize   4864 *1024
        cv2.imwrite(os.path.join(dirpath,"1.png"), shrink, [cv2.IMWRITE_PNG_COMPRESSION, 1]) #对图像进行压缩 【cv2.IMWRITE_PNG_COMPRESSION, 1】
                                                                                            #v2.IMWRITE_PNG_COMPRESSION  压缩品质 0-10 ，数字越小压缩比越小
        img1 = Image.open(os.path.join(dirpath,"1.png"))    #打开压缩后的缓冲文件
        img1.save(dst,quality=70)                          #二次压缩，并保存位原始文件的文件名
        os.remove(os.path.join(dirpath,"1.png"))           #删除缓存文件



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_path = r'C:/Users/shulei/Desktop/data_shu/4/'  # 原始文件路径
    new_image_path = r'C:/Users/shulei/Desktop/data_shu/luo/' # 压缩后文件保存路径
    pic_compress_png(image_path,new_image_path)
    print("压缩完成")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
