from modele.grille import Grille
from modele.humain import Humain


class Partie:

    def __init__(self,nb_joueurs):
        if nb_joueurs == 1:
            pass
            self.grille = Grille()
            self.joueur1 = Humain(1)
            #self.joueur2 = IA()
        else :
            self.grille = Grille()
            self.joueur1 = Humain(1)
            self.joueur2 = Humain(2)

    def joueur_joue(self,ligne,colonne,numero_joueur):
        if numero_joueur == 1:
            while not self.joueur1.joue(self.grille,ligne,colonne):
                print("Coup Invalide")
                return False
            return True
        else:
            while not self.joueur2.joue(self.grille,ligne,colonne):
                print("Coup Invalide")
                return False
            return True

    def partie_terminee(self):
        if self.joueur1.gagne(self.grille):
            print("Victoire du Joueur 1")
            return True
        elif self.joueur2.gagne(self.grille):
            print("Victoire du Joueur 2")
            return True
        elif self.grille.est_nulle():
            print("Match nul")
            return True
        return False




