from Components.Image import Image
from Components.Component import Component
from File_Structure.FileManager import File_Manager
from File_Structure.Target import Target
import numpy as np
import os


target = Target()

# On load l'image
image = Image("/home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E110/",
              "E1106402.jpg.pgm.jpg")

# On calcul les composantes connexe
image.calculate_components(1500, 8500)
image.calculate_gfds()
# image.save_data(target.path)
image.clustrize(2)
