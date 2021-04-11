import numpy as np
import cv2
from Math.GFD import GFD
import os


class Component:

    def __init__(self, data):
        self.__data = data
        self.__gfd = []
        # A EFFACER
        self.position = data['position']
        self.image = data['image']

    def apply_gfd(self, m, n):
        """
        Applique la fonction GFD sur le composent
        """
        gfd = GFD(self.__data)
        self.gfd = gfd.gfd(m, n)
        print(self.gfd)

    def copy_in_image(self, index):  # A RE ECRIRE C'EST JUSTE POUR LE TEST
        """
        Met dans une image la zone du composant
        """
        newImage = np.zeros(
            (self.position['horizontal']+1, self.position['vertical']+1))

        for x in range(self.position['x'], self.position['x']+self.position['horizontal']):
            for y in range(self.position['y'], self.position['y']+self.position['vertical']):
                newImage[x-self.position['x'], y -
                         self.position['y']] = self.image[y, x]

        cv2.imwrite("image"+str(index)+".jpg", newImage)

    # GETTERS / SETTERS

    def get_data(self):
        return self.__data

    def get_gfd(self):
        return self.__gfd
