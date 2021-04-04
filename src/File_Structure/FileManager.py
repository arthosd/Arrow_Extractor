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

    """
    initialise les attibuts de liste
    """

    def _init(self):
        self._save_sub_directories()
        self._list_sub_directories()

    """
    Liste les repertoires du repertoire source. (Et créer une dictionnaire pour les garder en mémoire)
    """

    def _save_sub_directories(self):

        for file in os.listdir(self.directory_path):
            if file[0] != '.':
                if os.path.isdir(self.directory_path+"/"+file) == True:
                    self.subdirectories[file] = self.directory_path + \
                        "/"+file+"/"

    """
    Listes et enregistre les NOMS des répoertoires dans la classe
    """

    def _list_sub_directories(self):

        for file in os.listdir(self.directory_path):
            if file[0] != '.':
                if os.path.isdir(self.directory_path+"/"+file) == True:
                    self.subdirectories_name.append(file)

        return self.subdirectories_name

    """
    Retourne le chemin d'un sous dossier
    """

    def get_subDirectory_path(self, directory_name):
        return self.subdirectories(directory_name)
