# 导入相关的库
from PIL import Image
import os
import time

files_list =[]
for files in os.walk("E:\\记忆\\脸谱\\选手记忆93张\\"):
    files_list.append(files)
files_list=files_list[0][2]



input_route = 'E:\\记忆\\脸谱\\选手记忆93张\\'
output_route1 = "E:\\记忆\\脸谱\\选手记忆93张部位1\\"
output_route2 = "E:\\记忆\\脸谱\\选手记忆93张部位2\\"
output_route3 = "E:\\记忆\\脸谱\\选手记忆93张部位3\\"
output_route4 = "E:\\记忆\\脸谱\\选手记忆93张部位4\\"
output_route5 = "E:\\记忆\\脸谱\\选手记忆93张部位5\\"
output_route6 = "E:\\记忆\\脸谱\\选手记忆93张部位6\\"
output_route7 = "E:\\记忆\\脸谱\\选手记忆93张部位7\\"
output_route8 = "E:\\记忆\\脸谱\\选手记忆93张部位8\\"
output_route9 = "E:\\记忆\\脸谱\\选手记忆93张部位9\\"
for i in range(0, len(files_list)):
    img = Image.open(input_route+files_list[i])
    w = img.width/3
    h = img.height/3
    file_name = files_list[i][:-4]

    region1 = img.crop((0, 0, w, h))
    region1.save(output_route1+file_name+'_1.png')

    region2 = img.crop((w, 0, 2*w, h))
    region2.save(output_route2+file_name+'_2.png')

    region3 = img.crop((2*w, 0, 3*w, h))
    region3.save(output_route3+file_name+'_3.png')

    region4 = img.crop((0, h, w, 2*h))
    region4.save(output_route4+file_name+'_4.png')

    region5 = img.crop((w, h, 2*w, 2*h))
    region5.save(output_route5+file_name+'_5.png')

    region6 = img.crop((2*w, h, 3*w, 2*h))
    region6.save(output_route6+file_name+'_6.png')

    region7 = img.crop((0, 2*h, w, 3*h))
    region7.save(output_route7+file_name+'_7.png')

    region8 = img.crop((w, 2*h, 2*w, 3*h))
    region8.save(output_route8+file_name+'_8.png')

    region9 = img.crop((2*w, 2*h, 3*w, 3*h))
    region9.save(output_route9+file_name+'_9.png')

    print(file_name+"切割完成")
    time.sleep(1)