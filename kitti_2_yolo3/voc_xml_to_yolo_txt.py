# xml_to_yolo_txt.py
# 此代码和VOC_KITTI文件夹同目录
import glob
import xml.etree.ElementTree as ET
import os
# 这里的类名为我们xml里面的类名，顺序现在不需要考虑
class_names = ['Car', 'Cyclist', 'Pedestrian']
# xml文件路径
path = '../Annotations/'
# 转换一个xml文件为txt
def single_xml_to_txt(xml_file):
    filepath, fullflname = os.path.split(xml_file)
    fname, ext = os.path.splitext(fullflname)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # 保存的txt文件路径
    txt_file = '../labels/'+fname+'.txt'
    with open(txt_file, 'w') as txt_file:
        for member in root.findall('object'):
            #filename = root.find('filename').text
            picture_width = int(root.find('size')[0].text)
            picture_height = int(root.find('size')[1].text)
            class_name = member[0].text
            # 类名对应的index
            class_num = class_names.index(class_name)

            box_x_min = int(member[1][0].text) # 左上角横坐标
            box_y_min = int(member[1][1].text) # 左上角纵坐标
            box_x_max = int(member[1][2].text) # 右下角横坐标
            box_y_max = int(member[1][3].text) # 右下角纵坐标
            # 转成相对位置和宽高
            x_center = (box_x_min + box_x_max) / (2 * picture_width)
            y_center = (box_y_min + box_y_max) / (2 * picture_height)
            width = (box_x_max - box_x_min) / (picture_width)
            height = (box_y_max - box_y_min) / (picture_height)
            print(class_num, x_center, y_center, width, height)
            txt_file.write(str(class_num) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(height) + '\n')
# 转换文件夹下的所有xml文件为txt
def dir_xml_to_txt(path):
    for xml_file in glob.glob(path + '*.xml'):
        single_xml_to_txt(xml_file)
dir_xml_to_txt(path)