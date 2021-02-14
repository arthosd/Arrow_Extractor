from cv2 import cv2 as cv #Importing Opencv
import os


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../RESJPG/E11471-2342-9-7-1.jpg.pgm.jpg')

img = cv.imread(filename)# Reading Image

cv.imshow("Arrows", img)#Showing image
cv.waitKey(0)
