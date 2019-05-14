import os
import matplotlib.image as pimg
import matplotlib.pyplot as plt
import numpy as np


def test():
    with open('./train_gt.txt', 'r') as f:
        gt = f.readlines()
    with open('./train_ign.txt', 'r') as f:
        ign = f.readlines()
    base_dir = './/Insight-MVT_Annotation_Train/'
    plt.figure(figsize=(10, 10))
    for i in gt:
        info = i.split(' ')
        img = pimg.imread(base_dir + info[0])
        plt.imshow(img)

        ign_ = [j.strip().split(' ')[1:] for j in ign if j.split(' ')[0] == info[0][:9]]
        if ign_:
            ign_box = [float(b) for b in ign_[0]]
            # print(ign_box)
            ign_box = np.array(ign_box, dtype=np.float32).reshape(-1, 4)
            for b in ign_box:
                rect = plt.Rectangle((b[0], b[1]), b[2] - b[0],
                                     b[3] - b[1], fill=False,
                                     edgecolor=(1, 0, 0),
                                     linewidth=1)
                plt.gca().add_patch(rect)

        bbox = [float(b) for b in info[1:]]
        boxes = np.array(bbox, dtype=np.float32).reshape(-1, 4)
        for b in boxes:
            rect = plt.Rectangle((b[0], b[1]), b[2] - b[0],
                                 b[3] - b[1], fill=False,
                                 edgecolor=(0, 1, 0),
                                 linewidth=1)
            plt.gca().add_patch(rect)
        plt.pause(1)
        plt.cla()


if __name__ == '__main__':
    test()