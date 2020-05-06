# 导入相关的库
from PIL import Image
from PIL import ImageDraw
import os
import time

## 将脸谱图片进行六宫格画线
files_list = []
for files in os.walk("E:\\记忆\\脸谱\\选手记忆93张\\"):
    files_list.append(files)
files_list = files_list[0][2]

input_route = 'E:\\记忆\\脸谱\\选手记忆93张\\'
output_route = "E:\\记忆\\脸谱\\选手记忆93张六部位画线\\"
for i in range(0, len(files_list)):
    img = Image.open(input_route + files_list[i])
    img_d = ImageDraw.Draw(img)
    x_len = img.width
    y_len = img.height
    file_name = files_list[i][:-4]
    for x in range(0, x_len, int(x_len / 2)):
        img_d.line(((x, 0), (x, y_len)), (0, 0, 0))
        img_d.line(((x + 1, 0), (x + 1, y_len)), (0, 0, 0))
        img_d.line(((x + 2, 0), (x + 2, y_len)), (0, 0, 0))
        img_d.line(((x - 2, 0), (x - 2, y_len)), (0, 0, 0))
        img_d.line(((x - 1, 0), (x - 1, y_len)), (0, 0, 0))
    for y in range(0, y_len, int(y_len / 3)):
        img_d.line(((0, y), (x_len, y)), (0, 0, 0))
        img_d.line(((0, y + 1), (x_len, y + 1)), (0, 0, 0))
        img_d.line(((0, y + 2), (x_len, y + 2)), (0, 0, 0))
        img_d.line(((0, y - 1), (x_len, y - 1)), (0, 0, 0))
        img_d.line(((0, y - 2), (x_len, y - 2)), (0, 0, 0))
    img.save(output_route + file_name + ".png")
    print(file_name + '画线完成')
    time.sleep(2)
