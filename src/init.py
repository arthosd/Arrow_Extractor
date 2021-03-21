from Components.Image import Image

image = Image("/home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E110/", "E1106402.jpg.pgm.jpg")
image.init_components(500)


for composant in image.composants:
    composant.apply_gfd(4,3)
    for gf in composant.gfd:
        print (gf)