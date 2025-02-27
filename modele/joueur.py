class Joueur:

    def __init__(self,numero_joueur):
        self.numero_joueur = numero_joueur
        pass

    def joue(self, grille, ligne, colonne):
        raise NotImplementedError("Cette méthode doit être implémentée par une sous-classe.")

    def gagne(self,grille):
        return grille.a_gagne(self.numero_joueur)