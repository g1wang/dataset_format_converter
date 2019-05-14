
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["car"]
xmlRoot = r'../data/xml_labels_train'
txtRoot =  r'../data/labels'
if os.path.exists(txtRoot)==False: #判断文件夹是否存在
     os.makedirs(txtRoot)
imageRoot = r'../data/picture_train'
def getFile_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        print(files)
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.splitext(file)[0]) #L.append(os.path.join(root, file))
    return L

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open(xmlRoot + '/%s.xml' % (image_id))
    out_file = open(txtRoot + '/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')




list_file_train = open(r'../data/train.txt', 'w')
#list_file_train = open(r'../data/test.txt', 'w')
#list_file_val = open('../data/boat_val.txt', 'w')
image_ids_train = os.listdir(imageRoot)
for image_name in image_ids_train:
	image_id = image_name.strip('\n').rstrip().split('.')[0]
	print(image_id)
	list_file_train.write(imageRoot + '/%s.jpg\n' % (image_id))
	convert_annotation(image_id)
list_file_train.close()
