from Components.Component import Component
from sklearn.cluster import KMeans

import numpy as np
import configparser
import cv2
import os


class Image:

    def __init__(self, directory_path, image_name):
        """
        Constructeur de la classe
        """
        # Configuration
        self.__config = configparser.ConfigParser()
        self.__config.read("src/Config/config.cfg")

        # Image
        self.__directory = directory_path
        self.__image_name = image_name
        self.__image_path = directory_path+image_name
        self.__image = self.image = cv2.imread(
            directory_path+image_name, 0)

        # Composants
        self.__components = []
        self.__clustered = []

    def invert_color(self):
        """
        Inverse la couleur de l'image.
        """
        temp_image = (255 - self.__image)
        cv2.imwrite(self.__image_path+".inverted.jpg", temp_image)

    def calculate_components(self, seuil_inferieur, seuil_superieur):
        """
        Calcule les composantes connexes de l'image
        """

        # On binarize l'image avec un seuil de 50
        ret, self.__image = cv2.threshold(
            self.__image, 50, 255, cv2.THRESH_BINARY)

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
                    'directory_path': self.__directory,
                    'label': labels
                }

                self.__components.append(Component(data, i))

    def calculate_gfds(self):
        """
        Fait le calcul de toutes les composantes connexe de l'image
        """

        for item in self.__components:
            item.apply_gfd()

    def save_data(self, directory_path):
        """
        Sauvegarde l'image et les valeurs du GFD dans le fichier
        """

        main_image_directory_path = directory_path+self.__image_name
        images_directory_path = main_image_directory_path+"/images"
        gfd_directory_path = main_image_directory_path+"/gfd"
        cluster_directory = main_image_directory_path+"/cluster"

        # Vérification de tout les répertoires

        if os.path.exists(main_image_directory_path) == False:
            os.mkdir(main_image_directory_path)

        if os.path.exists(images_directory_path) == False:
            os.mkdir(images_directory_path)

        if os.path.exists(gfd_directory_path) == False:
            os.mkdir(gfd_directory_path)

        if os.path.exists(cluster_directory) == False:
            os.mkdir(cluster_directory)

        for index in range(0, len(self.__components)):  # Pour tout les composants
            self._save_gfd(index, gfd_directory_path+"/")
            self._save_component_image(index, images_directory_path+"/")

        self._save_cluster(cluster_directory+"/")

    def _save_cluster(self, path):
        """
        Sauvegarde les clusters dans un sous dossier
        """

        # On crée les subdirectories
        for i in range(0, int(self.__config.get("CLUSTER", "nombre_cluster"))):
            if os.path.exists(path+"cluster"+str(i)) == False:
                os.mkdir(path+"cluster"+str(i))
            else:
                print("\t"+path+"cluster"+str(i) + " already exist")

        if len(self.__clustered) > 0:
            for index, component in enumerate(self.__components):
                self._save_component_image(
                    index, path+"cluster"+str(self.__clustered[index])+"/")

    def _save_gfd(self, index, path):
        """
        Sauvegarde les valeurs du gfd du composents à l'index index
        """

        gfd_to_write = self.__components[index].get_gfd()  # Les gfd à écrire

        with open(path+"gfd"+str(index)+".txt", "w") as fichier:

            for value in gfd_to_write:
                val = float(value)
                fichier.write(str(val)+"\n")

    def _save_component_image(self, index, path):
        """
        Sauvegarde l'image du composents à l'index index
        """

        # Image à copier
        image_to_write = self.__components[index].get_image_component()
        # On écrit l'image
        cv2.imwrite(path+"image"+str(index)+".jpg", image_to_write)

    def clusterize(self, save=False, target_path=None):
        """
        Clusterize les données et les stock dans l'array en attribut
        """
        size = int(self.__config.get("GFD", "rad")) * \
            int(self.__config.get("GFD", "ang"))

        nb_cluster = int(self.__config.get("CLUSTER", "nombre_cluster"))
        # On déclare le tableau que contient les données
        gfd = np.zeros(
            (len(self.__components), size))

        # Pour tout les composants on récupère les GFDs
        for compteur, item in enumerate(self.__components):
            gfd[compteur, ] = item.get_gfd()

        if len(self.__components) >= nb_cluster:

            model = KMeans(n_clusters=nb_cluster)
            model.fit(gfd)
            self.__clustered = model.labels_

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
