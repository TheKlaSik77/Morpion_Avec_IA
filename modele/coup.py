class Coup:

    def __init__(self,tupple_coup):
        """
        :param tupple_coup: coup sous la forme (ligne, colonne)
        """
        self.ligne = tupple_coup[0]
        self.colonne = tupple_coup[1]

    def get_ligne(self):
        return self.ligne

    def get_colonne(self):
        return self.colonne
