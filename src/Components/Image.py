import os
import cv2
import numpy as np
from Components.Component import Component

class Image :
    def __init__(self,directory_path,image_name):
        self.directory_path = directory_path # Le chemin du repertoire
        self.image_name = image_name # 
        self.image_path = directory_path+image_name# Le chemin de l'image
        self.image = cv2.imread(directory_path+image_name,0) # L'image en lecture
        self.composants = [] # On va contenir les composants de l'image

    
    """
    Récupère composants connexe
    """
    def _get_connected_component (self):
        return cv2.connectedComponentsWithStats(self.image, connectivity=8)

    """
    Crée les composants
    """
    def init_components (self,seuil_inferieur):

        nb_component, labels, stats, centroid = self._get_connected_component() # Récupère les composantes connexes

        # On crée toutes les composantes connexes
        for i in range(0, nb_component):
            if stats[i, cv2.CC_STAT_AREA] > seuil_inferieur:
                position = {
                    "x" : stats[i, cv2.CC_STAT_LEFT],
                    "y" : stats[i, cv2.CC_STAT_TOP],
                    "horizontal" : stats[i, cv2.CC_STAT_WIDTH],
                    "vertical" : stats[i, cv2.CC_STAT_HEIGHT],
                }

                data = {
                    'centroid' : centroid[i],
                    'position' : position,
                    'image_path' : self.image_path,
                    'area' : stats[i, cv2.CC_STAT_AREA],
                    'image' : self.image,
                    'nom_image' : self.image_name,
                    'directory_path' : self.directory_path
                }

                self.composants.append(Component(data))
        