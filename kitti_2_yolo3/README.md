### kitti 数据转换为yolo格式
####kitti Object Detection 主要车辆、行人
http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d
下载：
images： http://www.cvlibs.net/download.php?file=data_object_image_2.zip
labels： http://www.cvlibs.net/download.php?file=data_object_label_2.zip


#### kitti -> pascal voc xml-> yolo txt
Step 1：小类别归纳 (modify_annotations_txt.py)
Step 2: kitti -> pascal voc xml  (kitti_txt_to_voc_xml.py)
Step 3: pascal voc xml-> yolo txt   (voc_xml_to_yolo_txt.py)
Step 4: generate train list (kitti_train_val.py)