from Components.Component import Component
from sklearn.cluster import KMeans
from Utils.Utils import convert_float_array

import numpy as np
import cv2
import os


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

    def calculate_gfds(self):
        """
        Fait le calcul de toutes les composantes connexe de l'image
        """

        for item in self.__components:
            item.apply_gfd(5, 4)

    def save_data(self, directory_path):
        """
        Sauvegarde l'image et les valeurs du GFD dans le fichier
        """

        main_image_directory_path = directory_path+self.__image_name
        images_directory_path = main_image_directory_path+"/images"
        gfd_directory_path = main_image_directory_path+"/gfd"

        # Vérification de tout les repertoires

        if os.path.exists(main_image_directory_path) == False:
            os.mkdir(main_image_directory_path)

        if os.path.exists(images_directory_path) == False:
            os.mkdir(images_directory_path)

        if os.path.exists(gfd_directory_path) == False:
            os.mkdir(gfd_directory_path)

        for index in range(0, len(self.__components)):  # Pour tout les composants
            self._save_gfd(index, gfd_directory_path+"/")
            self._save_component_image(index, images_directory_path+"/")

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

    def clustrize(self, nombre_cluster):
        """
        Clusterize les données et les stock dans l'array en attribut
        """
        nb_cluster = nombre_cluster
        # On déclare le tableau que contient les données
        gfd = np.zeros(
            (len(self.__components), int(self.__components[0].get_gfd_size())))
        compteur = 0

        # Pour tout les composants on récupère les GFDs
        for item in self.__components:
            gfd[compteur, ] = item.get_gfd()
            compteur = compteur + 1

        model = KMeans(n_clusters=nb_cluster)
        model.fit(gfd)
        print(model.labels_)

        """ 
        model = KMeans(n_clusters=nb_cluster)  # on déclare notre model
        model.fit(gfd)"""

        """
        array = target.get_all_gfd_files()

        ##Lis les fichiers pour créer une liste de liste de float
        gfd = []
        for element in array:
            path = element['gfd']
            with open(path, 'r') as filein:
                values = filein.readlines()
                for i in range(values):
                    values[i] = float(values[i])
                gfd.append(values)

        ## K-means (nombre de clusters souhaités en paramètre)
        model = KMeans(8).fit(gfd)

        for i in range(len(array)):
            array[i]['label'] = model[i]
        """

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
