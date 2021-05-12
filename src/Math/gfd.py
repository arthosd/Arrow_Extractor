import numpy as np
import math
import configparser

config = configparser.ConfigParser()
config.read("src/Config/config.cfg")


def get_max_rad(image_component, cx, cy):

    width, height = image_component.shape
    centroid_x = cx
    centroid_y = cy

    candidates = []
    MAXRAD = 0.0

    find = False

    for y in range(0, height):
        if find == True:
            break

        for x in range(width):
            if image_component[x, y] != 0:  # Si on est sur du blanc
                candidates.append((x, y))  # Top
                find = True
                break

    find = False
    # On recherche sur le flan droit
    for x in range(width-1, 0, -1):
        if find == True:
            break
        for y in range(0, height):
            if image_component[x, y] != 0:
                candidates.append((x, y))  # Right
                find = True
                break

    find = False

    # On recherche sur le flan bas
    for y in range(height-1, 0, -1):
        if find == True:
            break
        for x in range(width):
            if image_component[x, y] != 0:
                candidates.append((x, y))  # Bottom
                find = True
                break

    find = False
    # On recherche sur le flan droit
    for x in range(0, width, 1):
        if find == True:
            break
        for y in range(0, height, 1):
            if image_component[x, y] != 0:
                candidates.append((x, y))  # Right
                find = True
                break

        for candidate in candidates:
            tmp = math.sqrt(
                math.pow(centroid_x-candidate[0], 2)+math.pow(centroid_y-candidate[1], 2))
            if tmp > MAXRAD:
                MAXRAD = tmp

    return MAXRAD


def gfd(image_component, cx, cy):

    m = int(config.get("GFD", "rad"))                  # Radian
    n = int(config.get("GFD", "ang"))                  # Ang

    image = image_component                            # Image
    width, height = image.shape                        # Taille de l'image

    gfd_numbers = np.zeros((m*n, 1))                   # Les valeurs GFD
    FR = np.zeros((m, n))                              # FD partie réelle
    FI = np.zeros((m, n))                              # FD partie imag

    MAXRAD = get_max_rad(image, cx, cy)                # La radian Maximal

    # Le centroid
    centroid = {"x": cx,
                "y": cx
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

                    if image[x, y] == 255:

                        FR[rad, ang] = FR[rad, ang] + 1 * \
                            math.cos(2 * math.pi * rad *
                                     (radius / MAXRAD) + ang * theta)

                        FI[rad, ang] = FR[rad, ang] - 1 * \
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

    tab = []  # Un tableau de float

    for item in gfd_numbers:
        value = float(item)
        tab.append(value)

    return (m*n, tab)
