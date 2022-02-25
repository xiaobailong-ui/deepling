import os
import cv2
import numpy as np
bace_path = r"E:\ceshi"  #提取后标签所在的png的路径
save_path = r'E:\erzhi'       #二至图像最终保存的路径

for im in os.listdir(bace_path):
    img = cv2.imread(os.path.join(bace_path, im))
    b, g, r = cv2.split(img)
    r[np.where(r != 0)] = 255
    cv2.imwrite(os.path.join(save_path, im), r)
