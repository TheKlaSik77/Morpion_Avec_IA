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

    def poser_coup(self,coup,numero_joueur):
        """
        Pose le coup de 'numero_joueur'
        Remplace la case grille[ligne][colonne] par numero_joueur'numero_joueur'
        """
        self.grille[coup.ligne][coup.colonne] = numero_joueur

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

    def get_emplacements_cases_vides(self):
        """
        Retourne la liste de tous les emplacements dont la case est vide sur la grille
        """
        liste_emplacements_cases_vides = []
        for i in range (3):
            for j in range(3):
                if self.grille[i][j] == 0:
                    liste_emplacements_cases_vides.append((i,j))
        return liste_emplacements_cases_vides

    def emplacement_est_vide(self,coup):
        """
        Teste si le joueur peut jouer à l'emplacement envoyé
        """
        if (coup.ligne,coup.colonne) in self.get_emplacements_cases_vides():
            return True
        return False