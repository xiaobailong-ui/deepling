import os
import glob
path = r'E:\pic3\json'  # 这里是指.json文件所在文件夹的路径
json_file = glob.glob(os.path.join(path, "*.json"))
os.system("activate labelme")
for file in json_file:
    os.system("labelme_json_to_dataset.exe %s" % ( file))
