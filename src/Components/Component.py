import numpy as np
import cv2
from Math.GFD import GFD
import configparser
import os


class Component:

    def __init__(self, data, index):

        # Fichier de config
        self.__config = configparser.ConfigParser()
        self.__config.read("src/Config/config.cfg")

        self.__labels = data['label']                     # Les labels
        self.__index = index                              # L'index du composants
        self.__data = data                                # Données de l'image
        self.__gfd = []                                   # Les Valeurs du GFD
        self.__position = data['position']                # positions centroids
        self.__image = data['image']                      # L'image de l'IMAGE
        self.__image_component = self._copy_in_image()    # L'image du composants
        self.__gfd_size = 0                               # La taille du GFD

    def apply_gfd(self):
        """
        Applique la fonction GFD sur le composent
        """
        image = self.__image_component
        gfd = GFD(self.__data, image)

        reponse = gfd.gfd()

        self.__gfd = reponse[1]
        self.__gfd_size = reponse[0]

    def _copy_in_image(self):  # A RE ECRIRE C'EST JUSTE POUR LE TEST
        """
        Met dans une image la zone du composant
        """
        newImage = np.zeros(
            (self.__position['horizontal']+1, self.__position['vertical']+1))

        for x in range(self.__position['x'], self.__position['x']+self.__position['horizontal']):
            for y in range(self.__position['y'], self.__position['y']+self.__position['vertical']):
                newImage[x-self.__position['x'], y -
                         self.__position['y']] = 255 if self.__labels[y, x] == self.__index else 0

        return newImage

    # GETTERS / SETTERS

    def get_data(self):
        return self.__data

    def get_gfd(self):
        return self.__gfd

    def get_image_component(self):
        return self.__image_component

    def get_gfd_size(self):
        return self.__gfd_size
