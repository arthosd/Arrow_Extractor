import cv2
from Components.Component import Component


class Image:

    def __init__(self, directory_path, image_name):
        """
        Constructeur de la classe
        """

        # Image
        self.__directory = directory_path
        self.__image_name = image_name
        self.__image_path = directory_path+image_name
        self.__image = self.image = cv2.imread(
            directory_path+image_name, 0)

        # Composants
        self.__components = []
        self.__clustered = []

    def calculate_components(self, seuil_inferieur, seuil_superieur):
        """
        Calcule les composantes connexe de l'image
        """

        nb_component, labels, stats, centroid = cv2.connectedComponentsWithStats(
            self.__image, connectivity=8)

        # On itère dans tous les composents calculés
        for i in range(0, nb_component):
            # S'il est dans le seuil en terme de taille, on le choisit
            if stats[i, cv2.CC_STAT_AREA] > seuil_inferieur and stats[i, cv2.CC_STAT_AREA] < seuil_superieur:

                position = {  # Valeurs de position sur l'image
                    "x": stats[i, cv2.CC_STAT_LEFT],
                    "y": stats[i, cv2.CC_STAT_TOP],
                    "horizontal": stats[i, cv2.CC_STAT_WIDTH],
                    "vertical": stats[i, cv2.CC_STAT_HEIGHT],
                }

                data = {  # Données globale
                    'centroid': centroid[i],
                    'position': position,
                    'image_path': self.__image_path,
                    'area': stats[i, cv2.CC_STAT_AREA],
                    'image': self.__image,
                    'nom_image': self.__image_name,
                    'directory_path': self.__directory
                }

                self.__components.append(Component(data))

    # SETTERS ET GETTERS

    def get_directory(self):
        return self.__directory

    def get_image(self):
        return self.__image

    def get_image_name(self):
        return self.__image_name

    def get_path(self):
        return self.__image_path

    def get_components(self):
        return self.__components
