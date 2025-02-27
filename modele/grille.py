# -*- coding: utf-8 -*-


class Grille:

    def __init__(self):
        self.grille = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def set_grille(self,nouvelle_grille):
        """
        Modifie la grille avec nouvelle_grille
        """
        self.grille = nouvelle_grille

    def poser_coup(self,ligne,colonne,numero_joueur):
        """
        Pose le coup de 'numero_joueur'
        Remplace la case grille[ligne][colonne] par numero_joueur'numero_joueur'
        """
        if self.grille[ligne][colonne] == 0:
            self.grille[ligne][colonne] = numero_joueur
            return True
        else :
            return False

    def a_gagne(self,numero_joueur):
        """
        Renvoie True si la grille est gagnée pour 'numéro_joueur'
        Renvoie False sinon
        """
        resultat = [
            all(emplacement == numero_joueur for emplacement in self.grille[0]),
            all(emplacement == numero_joueur for emplacement in self.grille[1]),
            all(emplacement == numero_joueur for emplacement in self.grille[2]),
            all(self.grille[i][0] == numero_joueur for i in range(3)),
            all(self.grille[i][1] == numero_joueur for i in range(3)),
            all(self.grille[i][2] == numero_joueur for i in range(3)),
            all(self.grille[i][i] == numero_joueur for i in range(3)),
            all(self.grille[0+i][2-i] == numero_joueur for i in range(3))
        ]

        if True in resultat:
            return True
        return False

    def est_nulle(self):
        """
        Renvoie True si partie est nulle
        Renvoie False sinon
        """
        if not self.a_gagne(1) and not self.a_gagne(2):
            for ligne in self.grille:
                for emplacement in ligne:
                    if emplacement == 0:
                        return False
            return True
        return False

    def get_grille(self):
        return self.grille