from modele.joueur import Joueur

class IA (Joueur):

    def __init__(self):
        pass

    def joue(self, grille, ligne = None, colonne = None):
        raise NotImplementedError("Cette méthode doit être implémentée par une sous-classe.")