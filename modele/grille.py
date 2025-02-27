# -*- coding: utf-8 -*-


class Grille:

    def __init__(self):
        self.grille = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def set_grille(self,nouvelle_grille):
        self.grille = nouvelle_grille

    def poser_coup(self,ligne,colonne,numero_joueur):
        """
        Pose le coup du joueur 1
        """
        if self.grille[ligne][colonne] == 0:
            self.grille[ligne][colonne] = numero_joueur
            return True
        else :
            return False