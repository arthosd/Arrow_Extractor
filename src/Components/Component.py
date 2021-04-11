import os
from Math.GFD import GFD
import numpy as np
import cv2
import configparser


class Component:

    def __init__(self, data):

        # Pour la lecture du fichier de config
        config = configparser.ConfigParser()
        config.read("src/Config/config.cfg")

        self.data = data
        self.centroid = data['centroid']  # Centroid du composants
        # Position dans du composant dans l'image
        self.position = data['position']
        self.image_path = data['image_path']  # Le chemin de l'image
        self.area = data['area']  # La superficie du composant
        self.gfd = []  # Va contenir le gfd du composant
        self.image = data['image']
        self.directory = data['directory_path']
        self.nom_image = data["nom_image"]  # Le nom de l'image
        self.target_directory = config.get("RESSOURCES", "target_directory")

    """
    Ecrire le composant dans une image
    """

    def write_component(self, target_path, numero_composant):
        # On écrit le composant

        if os.path.exists(target_path) == False:
            os.mkdir(target_path)

        newImage = np.zeros(
            (self.position['horizontal']+1, self.position['vertical']+1))

        for x in range(self.position['x'], self.position['x']+self.position['horizontal']):
            for y in range(self.position['y'], self.position['y']+self.position['vertical']):
                newImage[x-self.position['x'], y -
                         self.position['y']] = self.image[y, x]

        cv2.imwrite(target_path+"/composant" +
                    str(numero_composant)+".jpg", newImage)

    """
    Ecris les résultats dans un fichier
    """

    def write_gfd(self, target_directory, numero_composant):
        if len(self.gfd) == 0:
            return False

        if os.path.exists(target_directory) == False:
            os.mkdir(target_directory)

        file = open(target_directory+"/composant" +
                    str(numero_composant)+".gfd.resultat", "w")

        for number in self.gfd:
            to_write = float(number)
            file.write(str(to_write)+"\n")

        return True

    """
    Applique le GFD sur le composant
    """

    def apply_gfd(self, m, n):

        gfd = GFD(self.data)
        self.gfd = gfd.apply_gfd(m, n)

    """
    Ecrit toutes les données dans un dossier
    """

    def write_components(self, index):

        target_directory = self.target_directory + self.nom_image
        # print(target_directory)

        # Si le dossier n'existe pas
        if os.path.exists(self.target_directory) == False:
            os.mkdir(self.target_directory)  # On créer le dossier

        if os.path.exists(target_directory) == False:
            os.mkdir(target_directory)

        # On écrit l'image
        self.write_component(target_directory+"/image", index)
        # On écrit le gfd
        self.write_gfd(target_directory+"/gfd", index)
