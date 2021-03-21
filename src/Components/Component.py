import os
from Math.GFD import GFD

class Component :

    def __init__(self, data):
        self.data = data
        self.centroid = data['centroid'] # Centroid du composants
        self.position = data['position'] # Position dans du composant dans l'image
        self.image_path = data['image_path'] # Le chemin de l'image
        self.area = data['area'] # La superficie du composant
        self.gfd = [] # Va contenir le gfd du composant
        self.image = data['image']
        self.directory = data['directory_path']
        self.is_fleche = None

    """
    Ecrire le composant dans une image
    """
    def write_component(self,path):
        # ON écrit le composant
        pass

    """
    Ecris les résultats dans un fichier
    """
    def write_gfd (self):
        # On écrit dans un fichier
        pass

    """
    Applique le GFD sur le composant
    """
    def apply_gfd (self,m,n):

        gfd = GFD(self.data)
        self.gfd = gfd.apply_gfd(m,n)