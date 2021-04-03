import os
import configparser

class Target :

    def __init__(self):

        config = configparser.ConfigParser()
        config.read("src/Config/config.cfg")

        self.path = config.get("RESSOURCES", "target_directory")
        self.subdirectories = dict ()
        self.subdirectories_name = []


    """
    Initialise la classe
    """
    def _init(self) :
        self._verify_target_directory()
        self._save_sub_directories()
        self._list_sub_directories()



    """
    Créer le répertoire cible s'il n'existe pas
    """
    def _create_target_directory (self):

        created = True

        try :
            os.mkdir(self.path)
        except OSError :
            print ("WARNING : Un problème est survenue durant la création du repertoire")
            created = False

        return created

    """
    Vérifie que le repoertoire cible existe
    """
    def _verify_target_directory (self):

        # Si le repertoire n'existe pas, on le créer
        if os.path.exists(self.path) == False:
            self._create_target_directory(self.path)

    """
    Liste les repertoires du repertoire source. (Et créer une dictionnaire pour les garder en mémoire)
    """
    def _save_sub_directories (self):
        for file in os.listdir(self.directory_path):
            if file[0] != '.':
                if os.path.isdir(self.directory_path+"/"+file) == True :
                    self.subdirectories [file] = self.directory_path+"/"+file+"/"
    
    """
    Listes et enregistre les NOMS des répoertoires dans la classe
    """
    def _list_sub_directories (self) :

        for file in os.listdir(self.directory_path):
            if file[0] != '.':
                if os.path.isdir(self.directory_path+"/"+file) == True :
                    self.subdirectories_name.append(file)

        return self.subdirectories_name

    """
    Créer un subdirectory
    """
    def create_subdirectory (self, directory_name):

        if os.path.exists(self.path+"/"+directory_name) == False:
            os.mkdir(self.path+"/"+directory_name)
            self.subdirectories_name.append(directory_name)
            self.subdirectories_name[name] = self.path+"/"+directory_name+"/"


    