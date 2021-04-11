import numpy as np
import math


class GFD:

    def __init__(self, composant_data, image_component):
        self.__composant = composant_data
        self.__image_component = image_component

    def _get_max_rad(self):

        width, height = self.__image_component.shape
        centroid_x = self.__composant['centroid'][0] - (width // 2)
        centroid_y = self.__composant['centroid'][1] - (height // 2)

        candidates = []
        MAXRAD = 0.0

        find = False

        for y in range(0, height):
            if find == True:
                break

            for x in range(width):
                if self.__image_component[x, y] != 0:  # Si on est sur du blanc
                    candidates.append((x-(width//2), y-(height//2)))  # Top
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(width-1, 0, -1):
            if find == True:
                break
            for y in range(0, height):
                if self.__image_component[x, y] != 0:
                    candidates.append((x-(width//2), y-(height//2)))  # Right
                    find = True
                    break

        find = False

        # On recherche sur le flan bas
        for y in range(height-1, 0, -1):
            if find == True:
                break
            for x in range(width):
                if self.__image_component[x, y] != 0:
                    candidates.append((x-(width//2), y-(height//2)))  # Bottom
                    find = True
                    break

        find = False
        # On recherche sur le flan droit
        for x in range(0, width, 1):
            if find == True:
                break
            for y in range(0, height, 1):
                if self.__image_component[x, y] != 0:
                    candidates.append((x-(width//2), y-(height//2)))  # Right
                    find = True
                    break

            for candidate in candidates:
                tmp = math.sqrt(
                    math.pow(centroid_x-candidate[0], 2)+math.pow(centroid_y-candidate[1], 2))
                if tmp > MAXRAD:
                    MAXRAD = tmp

        return MAXRAD

    def gfd(self, m, n):

        image = self.__image_component                     # Image
        gfd_numbers = np.zeros((m*n, 1))                   # Les valeurs GFD
        FR = np.zeros((m, n))                              # FD partie réelle
        FI = np.zeros((m, n))                              # FD partie imag
        width, height = self.__composant['image'].shape    # Taille de l'image
        MAXRAD = self._get_max_rad()                       # La radian Maximal
        centroid = {"x": self.__composant["centroid"][0],  # Le centroid
                    "y": self.__composant["centroid"][1]
                    }

        # Polar Fourier transform
        for rad in range(0, m):
            for ang in range(0, n):

                for x in range(0, width):
                    for y in range(0, height):

                        radius = math.sqrt(
                            math.pow((x-centroid["x"]), 2) + (math.pow((y-centroid["y"]), 2)))

                        theta = math.atan2(
                            (y - centroid["x"]), (x - centroid["y"]))

                        if theta < 0:
                            theta = theta + (2*math.pi)

                        FR[rad, ang] = FR[rad, ang] + image[x, y] * \
                            math.cos(2 * math.pi * rad *
                                     (radius / MAXRAD) + ang * theta)

                        FI[rad, ang] = FR[rad, ang] - image[x, y] * \
                            math.sin(2 * math.pi * rad *
                                     (radius / MAXRAD) + ang * theta)

        # On calcule GFD

        DC = None

        for rad in range(0, m):
            for ang in range(0, n):

                if rad == 0 and ang == 0:
                    DC = math.sqrt(
                        math.pow(FR[0, 0], 2) + math.pow(FR[0, 0], 2))

                    gfd_numbers[0] = DC / (math.pi * math.pow(MAXRAD, 2))

                else:
                    gfd_numbers[rad*n + ang] = (math.sqrt(
                        math.pow(FR[rad, ang], 2)) + math.sqrt(math.pow(FI[rad, ang], 2))) / DC

        return gfd_numbers
