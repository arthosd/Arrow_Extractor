import os
import configparser


class File_Manager:

    def __init__(self):

        config = configparser.ConfigParser()
        config.read("src/Config/config.cfg")

        # On récupère le chemin du src images du fichier de config
        self.directory_path = config.get("RESSOURCES", "src_directory")
        self.subdirectories = dict()
        self.subdirectories_name = []

        self._init()

    def _init(self):
        """
        initialise les attibuts de liste
        """
        self._save_sub_directories()
        self._list_sub_directories()

    def _save_sub_directories(self):
        """
        Liste les repertoires du repertoire source. (Et créer une dictionnaire pour les garder en mémoire)
        """

        for file in os.listdir(self.directory_path):
            if file[0] != '.':
                if os.path.isdir(self.directory_path+"/"+file) == True:
                    self.subdirectories[file] = self.directory_path + \
                        "/"+file+"/"

    def _list_sub_directories(self):
        """
        Listes et enregistre les NOMS des répoertoires dans la classe
        """

        for file in os.listdir(self.directory_path):
            if file[0] != '.':
                if os.path.isdir(self.directory_path+"/"+file) == True:
                    self.subdirectories_name.append(file)

        return self.subdirectories_name

    def get_subDirectory_path(self, directory_name):
        """
        Retourne le chemin d'un sous dossier
        """
        return self.subdirectories(directory_name)
