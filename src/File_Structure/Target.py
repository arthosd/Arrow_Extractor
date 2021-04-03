import os

class Target :

    def __init__(self, target_directory):
        self.path = target_directory

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
    def verify_target_directory (self):

        # Si le repertoire n'existe pas, on le créer
        if os.path.exists(self.path) == False:
            self._create_target_directory(self.path)

    