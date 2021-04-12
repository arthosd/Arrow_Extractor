

def read_gfd(file_path):
    """
    On transforme les fichiers en tableau de float
    """
    tab = []  # Le tableau qui va contenir les floats

    with open(file_path, "r", encoding="utf8", errors='ignore') as fichier:

        while True:

            line = fichier.readline()  # On lit une ligne

            if not line:
                break

            tab.append(float(line))

    return tab


def convert_float_array(array):
    """
    Convertit un tableau numpy en tableau de float
    """
    tab = []  # Va contenir toutes les nouvelles valeures

    # On converti tous les items dans les arrays
    for item in array:

        value = float(item)
        tab.append(value)

    return tab
