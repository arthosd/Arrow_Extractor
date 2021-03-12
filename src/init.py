import os
from File_Structure.Image import Image
from File_Structure.FileManager import File_Manager

"""dossier = File_Manager('/home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E110')

images = dossier.files_in_directory #On récupère les images

compteur = 1

for item in images :
    image = Image(dossier.path_directory,item) # On crée une image
    image.get_connected_component()# On récupère les connected component
    image.write_components(1000, compteur)
    compteur = compteur +1"""


