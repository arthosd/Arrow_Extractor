import os
import cv2
import json
import numpy as np


class Image:
    
    def __init__(self, directory_path, image_name):

        self.image_path = directory_path+"/"+image_name
        self.directory_path = directory_path
        self.image_name = image_name
        self.image = cv2.imread(directory_path+"/"+image_name,0)
        self.stats = None
        self.nb_component = None

        pass

        """
        Récupère les composantes connexe à partir d'une de l'image chargé
        """
    def get_connected_component (self):

        self.nb_component , labels, self.stats, centroid = cv2.connectedComponentsWithStats(self.image,connectivity=4)

        pass

    def write_components (self,seuil,index):

        compteur = 0
        sizeX, sizeY = self.image.shape

        for i in range (0, self.nb_component):
            if self.stats[i,cv2.CC_STAT_AREA] > seuil : #Si on est au dessus du seuil
                newImage = np.zeros((sizeX,sizeY))
                debutX = self.stats[i,cv2.CC_STAT_LEFT]
                debutY = self.stats[i,cv2.CC_STAT_TOP]
                horizontal = self.stats[i,cv2.CC_STAT_WIDTH]
                vertical = self.stats[i,cv2.CC_STAT_HEIGHT]
                
                for x in range(debutX, debutX+horizontal):
                    for y in range(debutY, debutY+vertical):
                        newImage [y,x] = self.image[y,x]

                cv2.imwrite(self.directory_path+"/"+"connex"+str(i*index/2)+'.jpg',newImage)

            else:
                compteur = compteur +1

        return compteur