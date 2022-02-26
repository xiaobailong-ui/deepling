import cv2
import numpy as np
import os
import os.path as osp

from PIL import Image



def transfer_16bit_to_8bit(image_path,path_8_save,f):
    image_16bit = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    min_16bit = np.min(image_16bit)
    max_16bit = np.max(image_16bit)
    # image_8bit = np.array(np.rint((255.0 * (image_16bit - min_16bit)) / float(max_16bit - min_16bit)), dtype=np.uint8)
    # 或者下面一种写法
    image_8bit = np.array(np.rint(255 * ((image_16bit - min_16bit) / (max_16bit - min_16bit))), dtype=np.uint8)
    print(image_16bit.dtype)
    print('16bit dynamic range: %d - %d' % (min_16bit, max_16bit))
    print(image_8bit.dtype)
    print('8bit dynamic range: %d - %d' % (np.min(image_8bit), np.max(image_8bit)))
    cv2.imwrite(path_8_save+f, image_8bit)



def transfer_8bit_to_24bit(path,newpath):
    files = os.listdir(path)
    files = np.sort(files)
    i = 0
    for f in files:
        imgpath = path + f
        img = Image.open(imgpath).convert('RGB')
        dirpath = newpath
        file_name, file_extend = os.path.splitext(f)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.jpg')
        img.save(dst)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    image_path = './16/'    # 16位图像所在路径
    root_path = os.getcwd()
    path_8_save = osp.join(root_path,'8/')      # 8位图像所在路径
    path_24_save = osp.join(root_path,'24/')    # 24位图像所在路径
    if osp.isdir(path_8_save)  is False:
        os.mkdir(path_8_save)
    else:
        print("文件已存在")
    if osp.isdir(path_24_save) is False:
        os.mkdir(path_24_save)
    else:
        print("文件已存在")

    file = os.listdir(image_path)
    for f in file:
        image_path1 = os.path.join(image_path,f)
        img = transfer_16bit_to_8bit(image_path1,path_8_save,f)

    transfer_8bit_to_24bit(path_8_save, path_24_save)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
