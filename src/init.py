from Components.Image import Image

image = Image("/home/elie/Documents/Projet/Fac/Arrow_Extractor/RESJPG/E110/", "E1106402.jpg.pgm.jpg")
image.init_components(500)

tab = image.composants # Tout les composants

for i in range (0, len(tab)):
    tab[i].write_component("/home/elie/Documents/Projet/Fac/Arrow_Extractor/test/"+str(i)+".jpg")
    tab[i].apply_gfd(4,5)
    r = tab[i].write_gfd("/home/elie/Documents/Projet/Fac/Arrow_Extractor/image/test"+str(i)+".txt")
    print (r)