import os


class File_Manager:

    def __init__(self, path_directory):
        self.files_in_directory = os.listdir(path_directory)
        self.path_directory = path_directory
        self.directories = []
        self._list_directories()
        pass

    def show_files(self, path):
        for file in os.listdir(path):
            print(file)
        pass

    # Categorise les photo simialire dans leur dossier
    def categorize(self):

        array = dict()  # Dictionaire contenant toute les clés

        for file in self.files_in_directory:
            # On récupere le début de chaques nom
            debut_nom_fichier = file[0:4]

            if debut_nom_fichier in array:
                file_to_copy = open(self.path_directory +
                                    "/"+file, "rb")  # Open in binary
                file_where_to_copy = open(
                    self.path_directory+"/"+debut_nom_fichier+"/"+file, "wb")  # Open in binary
                binary = file_to_copy.read()
                file_where_to_copy.write(binary)
                file_to_copy.close()
                file_where_to_copy.close()

            else:
                # Si la clée n'existe pas alors on la créer
                array[debut_nom_fichier] = True
                # On crée l'entrée dans le dict
                os.makedirs(self.path_directory+"/"+debut_nom_fichier)
                file_to_copy = open(self.path_directory +
                                    "/"+file, "rb")  # Open in binary
                file_where_to_copy = open(
                    self.path_directory+"/"+debut_nom_fichier+"/"+file, "wb")  # Open in binary
                binary = file_to_copy.read()
                file_where_to_copy.write(binary)
                file_to_copy.close()
                file_where_to_copy.close()
        pass

    # Private function  for list all the directories
    def _list_directories(self):
        temp = []

        for file in os.listdir(self.path_directory):
            if file[0] != '.':
                temp.append(file)

        self.directories = temp

        return temp
