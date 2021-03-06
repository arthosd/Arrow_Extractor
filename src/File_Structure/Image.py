import os
import cv2
import numpy as np
import json


class Image :
    
    def __init__(self,list_of_dir,path):

        self.directories = list_of_dir# Liste des repertoires contenant les images
        self.path_to_write = path# Il faut lui rajouter un dossier
        self.data = {} #Dict where all the images data will be written

        pass


    def _imshow_components(self,labels):
        label_hue = np.uint8(179*labels/np.max(labels))
        blank_ch = 255*np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

        labeled_img[label_hue==0] = 0

        cv2.imshow('labeled.png', labeled_img)
        cv2.waitKey()

    def _connected_compomnent (self):
        
        pass