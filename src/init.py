from Components.Image import Image
from Components.Component import Component
from File_Structure.FileManager import File_Manager
from File_Structure.Target import Target
import numpy as np
import os

fm = File_Manager()
target = Target()

# On liste toutes les
for key, path in fm.subdirectories.items():
    files = os.listdir(path)

    for file in files:                          # On traite chaque fichier

        image = Image(path, file)               # On ouvre l'image
        image.calculate_components(250, 10000)  # On calcul les CC

        if len(image.get_components()) != 0:
            image.calculate_gfds()              # On calcul les GFDs
            image.clusterize()                  # On clusterize
            image.save_data(target.path)        # On enregistre les données
