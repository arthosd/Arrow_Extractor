import os
from Math.GFD import GFD
import numpy as np
import cv2

class Component :

    def __init__(self, data):
        self.data = data
        self.centroid = data['centroid'] # Centroid du composants
        self.position = data['position'] # Position dans du composant dans l'image
        self.image_path = data['image_path'] # Le chemin de l'image
        self.area = data['area'] # La superficie du composant
        self.gfd = [] # Va contenir le gfd du composant
        self.image = data['image']
        self.directory = data['directory_path']

    """
    Ecrire le composant dans une image
    """
    def write_component(self, image_path):
        # On écrit le composant

        newImage = np.zeros((self.position['horizontal']+1, self.position['vertical']+1))

        for x in range(self.position['x'], self.position['x']+self.position['horizontal']):
            for y in range(self.position['y'], self.position['y']+self.position['vertical']):
                newImage[x-self.position['x'], y-self.position['y']] = self.image[y, x]

        cv2.imwrite(image_path, newImage)

    """
    Ecris les résultats dans un fichier
    """
    def write_gfd (self,file_path):
        if len(self.gfd) == 0:
            return False
        
        with open(file_path, "w") as file:
            for number in self.gfd:
                file.write(str(number)+'\n')

        return True

    """
    Applique le GFD sur le composant
    """
    def apply_gfd (self,m,n):

        gfd = GFD(self.data)
        self.gfd = gfd.apply_gfd(m,n)