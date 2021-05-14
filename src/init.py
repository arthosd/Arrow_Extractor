from Components.Image import Image
from Components.Component import Component
from File_Structure.FileManager import File_Manager
from File_Structure.Target import Target
import configparser
import numpy as np
import os

# Configuration
config = configparser.ConfigParser()
config.read("src/Config/config.cfg")

# File managing
fm = File_Manager()
target = Target()
compteur = 1

# On liste toutes les
dir = fm.subdirectories.items()
for key, path in dir:
    files = os.listdir(path)

    nb_files = len(dir)

    for file in files:                          # On traite chaque fichier
        image = Image(path, file)               # On ouvre l'image
        print("=================== "+image.get_image_name() +
              " =================== "+str(compteur)+"/"+str(nb_files))

        si = int(config.get("FILTRE", "si"))
        ss = int(config.get("FILTRE", "ss"))

        print("Getting connected components with size filter : " +
              str(si)+" "+str(ss)+" ...")
        image.calculate_components(si, ss)      # On calcul les CC

        if len(image.get_components()) != 0:
            print("\t - Processing GFDs ...")
            image.calculate_gfds()              # On calcul les GFDs
            print("\t - Clusterizing ...")
            image.clusterize()                  # On clusterize
            print("\t - Saving results ...")
            image.save_data(target.path)        # On enregistre les données

        print(" ")
        compteur += 1
