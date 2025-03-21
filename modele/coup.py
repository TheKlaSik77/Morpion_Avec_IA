class Coup:

    def __init__(self,tupple_coup,numero_joueur):
        """
        :param tupple_coup: coup sous la forme (ligne, colonne)
        """
        self.ligne = tupple_coup[0]
        self.colonne = tupple_coup[1]
        self.numero_joueur = numero_joueur

    def __str__(self):
        return f'Joueur {self.numero_joueur} joue en ({self.ligne},{self.colonne})'
    def get_ligne(self):
        return self.ligne

    def get_colonne(self):
        return self.colonne
