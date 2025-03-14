from __future__ import annotations      # Permet de contourner le problème empêchant d'indiquer noeud_pere comme type Noeud

import copy
from modele.coup import Coup
from modele.grille import Grille

GAGNE = 1
NUL = 0
PERD = -1

class Noeud:

    def __init__(self,etat_grille : Grille, coup : Coup, noeud_pere : 'Noeud', numero_joueur_en_cours, numero_joueur_base):
        """

        :param etat_grille: copie l'objet Grille passé en paramètre
        :param coup: Coup joué sur le noeud
        :param noeud_pere: Noeud père (None si noeud est un noeud initial)
        :param numero_joueur_en_cours: (numero_du_joueur qui joue le coup sur ce noeud
        :param numero_joueur_base:
        """
        self.coup = coup
        self.etat_grille = copy.deepcopy(etat_grille)
        self.valeur = None
        self.noeud_pere = noeud_pere
        self.liste_noeuds_fils = []
        self.numero_joueur_en_cours = numero_joueur_en_cours
        self.numero_joueur_base = numero_joueur_base

    def developper_fils(self):
        """
        Crée les fils du noeud ou si cas fin de partie, attribue la valeur à noeud
        """
        # On teste si le noeud est en cas de fin de partie sinon il reste à None
        self.valeur = self.tester_victoire_defaite_ou_nul_noeuds()

        if self.valeur is None:
            liste_emplacements_vides = self.etat_grille.get_emplacements_cases_vides()

            for emplacement in liste_emplacements_vides:
                # On crée un noeud pour chaque emplacement, avec son coup, sa grille et son noeud parent.
                self.liste_noeuds_fils.append(
                    Noeud(self.etat_grille, Coup(emplacement, 1 if self.numero_joueur_en_cours == 2 else 1),
                          self,1 if self.numero_joueur_en_cours == 2 else 2,self.numero_joueur_base))

    def tester_victoire_defaite_ou_nul_noeuds(self):
        if self.etat_grille.a_gagne(self.numero_joueur_base):
            return 1
        elif self.numero_joueur_base != self.numero_joueur_en_cours and self.etat_grille.a_gagne(self.numero_joueur_en_cours):
            return -1
        elif self.etat_grille.est_nulle():
            return 0
        else:
            return None




