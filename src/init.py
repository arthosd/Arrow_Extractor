import os
import cv2
from Components.Image import Image
from Math.GFD import GFD

image = Image("/home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E110/", "test.jpg") 
image.get_connected_component()
centroids = image.get_centroid(500) # On récupère les centroids
stats = image.stats # les stats de l'image
gfd = GFD(centroids[0],stats,image.image)


#var = gfd.get_max_rad()

var = gfd.apply_gfd(6,5)

print (var)

