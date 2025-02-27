from modele.joueur import Joueur

class Humain (Joueur):

    # Pas de def __init__ car memes attributs que Joueur

    def joue(self, grille, ligne, colonne):
        if grille.poser_coup(ligne,colonne,self.numero_joueur):
            print(f'Joueur {self.numero_joueur} joue en [{ligne},{colonne}]')
            return True
        else:
            return False

    def gagne(self,grille):
        return grille.a_gagne(self.numero_joueur)


