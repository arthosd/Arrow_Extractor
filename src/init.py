import os
from File_Structure.FileManager import *

manager = File_Manager(
    "/home/elie/Documents/Fac/Projet/Arrow_Extractor/RESJPG")

for file in manager.directories:
    print(file)
