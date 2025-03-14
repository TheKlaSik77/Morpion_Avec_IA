from modele.coup import Coup

def traitement_entree(entree):
    """
    Prend en paramètre une chaîne de format XY (par exemple : A2),
    et retourne une paire de coordonnées ligne-colonne correspondante.
    """
    if len(entree) != 2 or not ('A' <= entree[0].upper() <= 'C') or not ('1' <= entree[1] <= '3'):
        return False

    ligne = ord(entree[0].upper()) - ord('A')  # Convertit 'A', 'B', 'C' en 0, 1, 2
    colonne = int(entree[1]) - 1  # Convertit '1', '2', '3' en 0, 1, 2

    return ligne, colonne


def saisir_coup_terminal():
    """
    Teste si le format du coup est valide, redemande un input tant qu'il ne l'est pas, puis renvoie le coup
    :return: (numéro de ligne, numéro de colonne)
    """
    entree = input("Entrer la ligne puis la colonne (exemple : A2) : ")
    coup = traitement_entree(entree)
    while not coup:
        print('Entrée incorrecte! Veuillez réessayer \n')
        entree = input("Entrer la ligne puis la colonne (exemple : A2) : ")
        coup = traitement_entree(entree)
    return Coup(coup)