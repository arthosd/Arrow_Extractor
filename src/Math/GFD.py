import os
import numpy as np
import math


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

    def get_max_rad(self):

        width, height = self.image.shape  # Les dimensions de l'image
        centroid_x = self.centroid[0]-(width//2)
        centroid_y= self.centroid[1]-(height//2)
        candidates = [] # Va contenir les 4 candidats
        MAXRAD = 0.0

        find = False

        # On recherche sur le flan haut
        for y in range(0,height):
            if find == True:
                break

            for x in range(width):
                if self.image[x, y] != 0:  # Si on est sur du blanc
                    candidates.append((x-(width//2), y-(height//2))) # Top
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(width-1, 0, -1):
            if find == True:
                break
            for y in range(0, height):
                if self.image[y, x] != 0:
                    candidates.append((x-(width//2), y-(height//2)))# Right
                    find = True
                    break

        find = False

        # On recherche sur le flan bas
        for y in range(height-1, 0, -1):
            if find == True:
                break
            for x in range(width):
                if self.image[x, y] != 0:
                    candidates.append((x-(width//2), y-(height//2))) # Bottom
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(0, width, 1):
            if find == True:
                break
            for y in range(0, height, 1):
                if self.image[x, y] != 0:
                    candidates.append((x-(width//2), y-(height//2))) # Right
                    find = True
                    break

            for candidate in candidates:
                tmp = math.sqrt(math.pow(centroid_x-candidate[0],2)+math.pow(centroid_y-candidate[1],2))
                if tmp > MAXRAD:
                    MAXRAD = tmp
                    
        return MAXRAD

    # Deplace de "index" sur l'axes des x
    def _add_x(self, index):

        return self.origin["x"]+index

    # Deplace de "index" sur l'axes des x
    def _add_y(self, index):

        return self.origin["y"]+index

    """
    Retourne le centroid de l'image en question
    """

    def _get_centroiSd(self):
        return self.centroid

    def apply_gfd(self,m,n): 
        """
        Algorithme principale fourrier
        """
        width, height = self.image.shape # On récupère la taille de l'image
        MAXRAD = self.get_max_rad() # ON trouve la Maxrad de L'image
        
        x = np.linspace(-(width-1)//2, (width-1)//2, width)
        y = np.linspace(-(height-1)//2, (height-1)//2, height)

        X, Y = np.meshgrid(x, y)

        radius = np.sqrt(np.power(X, 2) + np.power(Y, 2)) / MAXRAD

        theta = np.arctan2(Y, X)
        theta[theta < 0] = theta[theta < 0] + (2 * np.pi)

        FR = np.zeros((m,n))
        FI = np.zeros((m,n))
        FD = np.zeros((m*n,1))

        i = 0

        for rad in range(m):
            for ang in range(n):
                tempR = self.image.dot(np.cos(2 * np.pi * rad * radius + ang * theta))
                tempI = self.image.dot(np.sin(2 * np.pi * rad * radius + ang * theta))
                FR[rad, ang] = np.sum(tempR)
                FI[rad, ang] = np.sum(tempI)

                if rad == 0 and ang == 0:
                    FD[i] = math.sqrt((2* (FR[0,0] * FR[0,0]))) / (np.pi* MAXRAD * MAXRAD)
                else:
                    FD[i] = math.sqrt((FR[rad, ang] * FR[rad, ang]) + (FI[rad, ang] * FI[rad, ang])) / (math.sqrt((2* (FR[0,0] * FR[0,0]))))
                    
                i = i + 1
                
        return FD
