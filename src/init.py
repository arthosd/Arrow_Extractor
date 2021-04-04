from Components.Image import Image
from Components.Component import Component
from File_Structure.FileManager import File_Manager
from File_Structure.Target import Target
import os

fm = File_Manager()  # A retirer peut etre
target = Target()  # idem

for key, path in fm.subdirectories.items():
    files = os.listdir(path)  # Pour tout les fichier dans les subdirectories

    for file in files:  # On traite chaque fichier

        image = Image(path, file)  # On déclare une nouvelle image
        image.init_components(200)  # On apllique les initialisations
        composant_images = image.composants  # Récupère les composants de chaques l'image

        compteur = 0

        for composant in composant_images:
            composant.apply_gfd(5, 3)  # On calcul gfd de chaque composants
            # On écrit les images et les fichiers
            composant.write_components(compteur)
            compteur = compteur + 1
