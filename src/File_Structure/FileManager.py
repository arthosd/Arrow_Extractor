import os

class File_Manager : 

    def __init__(self,path_directory):
        self.files_in_directory = os.listdir(path_directory)
        self.path_directory = path_directory
        pass

    def show_files (self):
        for file in self.files_in_directory:
            print(file)
        pass

    def categorize (self):

        array = dict()# Dictionaire contenant toute les clés

        for file in self.files_in_directory:  
             debut_nom_fichier = file[0:4]#On récupere le début de chaques nom

             if array.has_key(debut_nom_fichier) == True :
                 file_to_copy = file(self.path_directory+"/"+file,"rb")# Open in binary
                 file_where_to_copy = file(self.path_directory+"/"+debut_nom_fichier+"/"+file,"wb")#Open in binary