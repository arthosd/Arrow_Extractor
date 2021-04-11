from Components.Image import Image
from Components.Component import Component
from File_Structure.FileManager import File_Manager
from File_Structure.Target import Target
import numpy as np
import os

image = Image("/home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E110/",
              "E1106402.jpg.pgm.jpg")  # On ouvre l'image

image.calculate_components(1500, 8500)  # On calcul tout les composant


gfd = image.calculate_components_gfd(6)

print(gfd)
