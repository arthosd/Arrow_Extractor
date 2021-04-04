import os
import numpy as np
import math


class GFD:

    def __init__(self, composant):
        self.composant = composant

    def _get_max_rad(self):

        width, height = self.composant['image'].shape
        centroid_x = self.composant['centroid'][0] - (width // 2)
        centroid_y = self.composant['centroid'][1] - (height // 2)

        candidates = []
        MAXRAD = 0.0

        find = False

        for y in range(0, height):
            if find == True:
                break

            for x in range(width):
                if self.composant['image'][x, y] != 0:  # Si on est sur du blanc
                    candidates.append((x-(width//2), y-(height//2)))  # Top
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(width-1, 0, -1):
            if find == True:
                break
            for y in range(0, height):
                if self.composant['image'][y, x] != 0:
                    candidates.append((x-(width//2), y-(height//2)))  # Right
                    find = True
                    break

        find = False

        # On recherche sur le flan bas
        for y in range(height-1, 0, -1):
            if find == True:
                break
            for x in range(width):
                if self.composant['image'][x, y] != 0:
                    candidates.append((x-(width//2), y-(height//2)))  # Bottom
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(0, width, 1):
            if find == True:
                break
            for y in range(0, height, 1):
                if self.composant['image'][x, y] != 0:
                    candidates.append((x-(width//2), y-(height//2)))  # Right
                    find = True
                    break

            for candidate in candidates:
                tmp = math.sqrt(
                    math.pow(centroid_x-candidate[0], 2)+math.pow(centroid_y-candidate[1], 2))
                if tmp > MAXRAD:
                    MAXRAD = tmp

        return MAXRAD

    def apply_gfd(self, m, n):
        """
        Algorithme principale GFD
        """
        width, height = self.composant['image'].shape  # On récupère la taille de l'image
        MAXRAD = self._get_max_rad()  # ON trouve la Maxrad de L'image

        x = np.linspace(-(width-1)//2, (width-1)//2, width)
        y = np.linspace(-(height-1)//2, (height-1)//2, height)

        X, Y = np.meshgrid(x, y)

        radius = np.sqrt(np.power(X, 2) + np.power(Y, 2)) / MAXRAD

        theta = np.arctan2(Y, X)
        theta[theta < 0] = theta[theta < 0] + (2 * np.pi)

        FR = np.zeros((m, n))
        FI = np.zeros((m, n))
        FD = np.zeros((m*n, 1))

        i = 0

        for rad in range(m):
            for ang in range(n):
                tempR = self.composant['image'].dot(
                    np.cos(2 * np.pi * rad * radius + ang * theta))
                tempI = self.composant['image'].dot(
                    np.sin(2 * np.pi * rad * radius + ang * theta))
                FR[rad, ang] = np.sum(tempR)
                FI[rad, ang] = np.sum(tempI)

                if rad == 0 and ang == 0:
                    FD[i] = math.sqrt((2 * (FR[0, 0] * FR[0, 0]))
                                      ) / (np.pi * MAXRAD * MAXRAD)
                else:
                    FD[i] = math.sqrt((FR[rad, ang] * FR[rad, ang]) + (FI[rad, ang]
                                      * FI[rad, ang])) / (math.sqrt((2 * (FR[0, 0] * FR[0, 0]))))

                i = i + 1

        return FD
