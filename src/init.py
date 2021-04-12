from Components.Image import Image
from Components.Component import Component
from File_Structure.FileManager import File_Manager
from File_Structure.Target import Target
import numpy as np
import os

target = Target()

# On load l'image
image = Image("//home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E110/",
              "E1106400.jpg.pgm.jpg")

image.invert_color()

"""
# On calcul les composantes connexe
image.calculate_components(1500, 8500)
# ON calcul les gfd des composantes connexes
image.calculate_gfds()
# On clusturize
image.clustrize()
# On sauvegarde les résultats dans le target
image.save_data(target.path)"""
