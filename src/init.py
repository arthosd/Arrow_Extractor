import os
import cv2
from Components.Image import Image
from Math.GFD import GFD

image = Image("/home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E111/", "connex1221.5.jpg") 
image.get_connected_component()
centroids = image.get_centroid(500) # On récupère les centroids
stats = image.stats # les stats de l'image

gfd = GFD(centroids[0],stats,image.image)
rad = gfd.get_max_rad()