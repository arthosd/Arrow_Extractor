import os
import numpy as np
import Math


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
        candidates = [] # Va contenir les 4 candidats
        MAXRAD = None

        find = False

        # On recherche sur le flan haut
        for y in range(height):
            if find == True:
                break

            for x in range(width):
                if self.image[x, y] != 0:  # Si on est sur du blanc
                    candidates.append((x, y)) # Top
                    find = True
                    break

        find = False
        # On recherche sur le flan gauche
        for x in range(width-1, 0, -1):
            if find == True:
                break
            for y in range(0, height):
                if self.image[y, x] != 0:
                    candidates.append((x, y))# Right
                    find = True
                    break

        find = False

        # On recherche sur le flan bas
        for y in range(height-1, 0, -1):
            if find == True:
                break
            for x in range(height):
                if self.image[x, y] != 0:
                    candidates.append((x, y)) # Bottom
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(0, width, 1):
            if find == True:
                break
            for y in range(0, height, 1):
                if self.image[x, y] != 0:
                    candidates.append((x, y)) # Right
                    find = True
                    break

        for candidate in candidates:
            print(candidate[0])

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

    def _get_centroid(self):
        return self.centroid

    def apply_gfd(self,m,n):
        """
        Algorithme principale fourrier
        """
        N = self.image.shape[1] # On récupère la largeur de l'image
        MAXRAD = _get_max_rad() # Il faut modifier l'algorithme avant
        
        x = y = np.linspace(-(N-1)//2, (N-1)//2, N)
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
                tempR = image.dot(np.cos(2 * np.pi * rad * radius + ang * theta))
                tempI = image.dot(np.sin(2 * np.pi * rad * radius + ang * theta))
                FR[rad, ang] = np.sum(tempR)
                FI[rad, ang] = np.sum(tempI)

                if rad == 0 and ang == 0:
                    FD[i] = Math.sqrt((2* (FR[0,0] * FR[0,0]))) / (np.pi* MAXRAD * MAXRAD)
                else:
                    FD[i] = Math.sqrt((FR[rad, ang] * FR[rad, ang]) + (FI[rad, ang] * FI[rad, ang])) / (Math.sqrt((2* (FR[0,0] * FR[0,0]))))
                    
                i = i + 1
        return FD
