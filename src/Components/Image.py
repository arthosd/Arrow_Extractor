import os
import cv2
import json
import numpy as np


class Image:

    def __init__(self, directory_path, image_name):

        self.image_path = directory_path+"/"+image_name
        self.directory_path = directory_path
        self.image_name = image_name
        self.image = cv2.imread(directory_path+"/"+image_name, 0)
        self.stats = None
        self.nb_component = None
        self.centroid = None

        pass

    def get_centroid(self, seuil):

        centroid = []  # Tableau qui va contenir les centroids

        for connected_component in range(self.nb_component):
            if self.stats[connected_component, cv2.CC_STAT_AREA] > seuil:
                # On l'ajoute dans le tableau
                centroid.append(self.centroid[connected_component])

        return centroid

    """
    Récupère les composantes connexe à partir d'une de l'image chargé
    """

    def get_connected_component(self):

        self.nb_component, labels, self.stats, self.centroid = cv2.connectedComponentsWithStats(
            self.image, connectivity=4)

        pass

    def write_components(self, seuil_inferieur, index):

        compteur = 0

        for i in range(0, self.nb_component):
            if self.stats[i, cv2.CC_STAT_AREA] > seuil_inferieur:  # Si on est au dessus du seuil
                debutX = self.stats[i, cv2.CC_STAT_LEFT]
                debutY = self.stats[i, cv2.CC_STAT_TOP]
                horizontal = self.stats[i, cv2.CC_STAT_WIDTH]
                vertical = self.stats[i, cv2.CC_STAT_HEIGHT]
                newImage = np.zeros((horizontal+1, vertical+1))

                for x in range(debutX, debutX+horizontal):
                    for y in range(debutY, debutY+vertical):
                        newImage[x-debutX, y-debutY] = self.image[y, x]

                cv2.imwrite(self.directory_path+"/"+"connex" +
                            str(i*index/2)+'.jpg', newImage)

            else:
                compteur = compteur + 1

        return compteur

    """
    Fonction à ré écrire
    """

    def reconstruct_image(self, seuil, index):

        compteur = 0
        sizeX, sizeY = self.image.shape

        for i in range(0, self.nb_component):
            if self.stats[i, cv2.CC_STAT_AREA] > seuil:  # Si on est au dessus du seuil
                newImage = np.zeros((sizeX, sizeY))
                debutX = self.stats[i, cv2.CC_STAT_LEFT]
                debutY = self.stats[i, cv2.CC_STAT_TOP]
                horizontal = self.stats[i, cv2.CC_STAT_WIDTH]
                vertical = self.stats[i, cv2.CC_STAT_HEIGHT]

                for x in range(debutX, debutX+horizontal):
                    for y in range(debutY, debutY+vertical):
                        newImage[y, x] = self.image[y, x]

                cv2.imwrite(self.directory_path+"/"+"connex" +
                            str(i*index/2)+'.jpg', newImage)

            else:
                compteur = compteur + 1

        return compteur
