import os
import cv2
import numpy as np
import json
import math
from scipy.ndimage.measurements import label

class Image :
    
    def __init__(self,image_path):

        self.image_path = image_path
        self.labels = None
        self.num_labels = None
        self.image = cv2.imread(image_path,0)

        pass

    def remove_connected_comp(self,segmented_img, connected_comp_diam_limit=20):
        """
        Remove connected components of a binary image that are less than smaller than specified diameter.
        :param segmented_img: Binary image.
        :param connected_comp_diam_limit: Diameter limit
        :return:
        """
        img = segmented_img.copy()
        structure = np.ones((3, 3), dtype=np.int)
        labeled, n_components = label(img, structure)
        for i in range(n_components):
            ixy = np.array(list(zip(*np.where(labeled == i))))
            x1, y1 = ixy[0]
            x2, y2 = ixy[-1]
            dst = math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
            if dst < connected_comp_diam_limit:
                for u, v in ixy:
                    img[u, v] = 0
        return img

    def imshow_components(self,labels):
        label_hue = np.uint8(179*labels/np.max(labels))
        blank_ch = 255*np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

        labeled_img[label_hue==0] = 0

        cv2.imshow('labeled.png', labeled_img)
        cv2.waitKey()

    def find_connected_component (self):

        self.num_labels ,self.labels = cv2.connectedComponents(self.image)
        print (self.labels.dtype)

        pass