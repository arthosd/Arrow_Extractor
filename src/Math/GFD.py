import os
import numpy as np


class GFD:

    """
    Récupère un composant pour faire un traitement de GFD
    """

    def __init__(self, centroid, stats, image):

        self.image = image  # On récupère les pixels de l'image
        self.centroid = centroid  # on récupère le centroid de l'
        self.stats = stats  # Toutes les statistiques concerant l'image
        # L'origin de la base sur laquelle nous allons travailler
        # self.origin = {"x": centroid[0], "y": centroid[1]}

        pass

    """
        Récuèpre le rad maximal
    """

    def _get_max_rad(self):

        width, height = self.image.shape  # Les dimensions de l'image
        candidates = {"top": None, "right": None, "bottom": None,
                      "left": None}  # Garde les candidates des sommets

        find = False

        # On recherche sur le flan haut
        for y in range(height):
            if find == True:
                break

            for x in range(width):
                if self.image[x, y] != 0:  # Si on est sur du blanc
                    candidates["top"] = (x, y)
                    find = True
                    break

        find = False
        # On recherche sur le flan gauche
        for x in range(width-1, 0, -1):
            if find == True:
                break
            for y in range(0, height):
                if self.image[y, x] != 0:
                    candidates["right"] = (x, y)
                    find = True
                    break

        find = False

        # On recherche sur le flan bas
        for y in range(height-1, 0, -1):
            if find == True:
                break
            for x in range(height):
                if self.image[x, y] != 0:
                    candidates["bottom"] = (x, y)
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(0, width, 1):
            if find == True:
                break
            for y in range(0, height, 1):
                if self.image[x, y] != 0:
                    candidates["left"] = (x, y)
                    find = True
                    break

        return candidates

    # Deplace de "index" sur l'axes des x
    def _add_x(self, index):

        return self.origin["x"]+index

    # Deplace de "index" sur l'axes des x
    def _add_y(self, index):

        return self.origin["y"]+index

    """
    Retourne le centroid de l'image en question
    """

    def _get_centroid(self):
        return self.centroid

    def apply_gfd(self):
        """
        Algorithme principale fourrier
        """
        pass
