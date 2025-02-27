
class Joueur:

    def __init__(self,numero_joueur):
        self.numero_joueur = numero_joueur
        pass

    def joue(self, grille, ligne, colonne):
        if grille.poser_coup(ligne,colonne,self.numero_joueur):
            print(f'Joueur {self.numero_joueur} joue en [{ligne},{colonne}]')
            return True
        else:
            return False

    def gagne(self,grille):
        return grille.a_gagne(self.numero_joueur)


