from __future__ import annotations      # Permet de contourner le problème empêchant d'indiquer noeud_pere comme type Noeud
import copy
from modele.coup import Coup
from modele.grille import Grille
import vue.vue_console as vue

class Noeud:

    def __init__(self,etat_grille : Grille, coup : Coup, numero_joueur_base):
        """

        :param etat_grille: copie l'objet Grille passée en paramètre
        :param coup: Coup joué sur le noeud
        :param numero_joueur_base:
        """
        self.coup = coup
        self.etat_grille = copy.deepcopy(etat_grille)
        self.etat_grille.poser_coup(self.coup)
        self.liste_noeuds_fils : list[Noeud] = []
        self.numero_joueur_base = numero_joueur_base
        self.valeur = self.tester_victoire_defaite_ou_nul_noeuds()


    #FIXME: Temps d'exécution beaucoup trop long
    def developper_fils(self):
        """
        Crée les fils du noeud plus efficacement sans récursion inutile.
        """

        if self.valeur is None:
            liste_emplacements_vides = self.etat_grille.get_emplacements_cases_vides()

            for emplacement in liste_emplacements_vides:
                # On crée un noeud pour chaque emplacement, avec son coup, sa grille et son noeud parent.
                self.liste_noeuds_fils.append(
                    Noeud(self.etat_grille, Coup(emplacement, 1 if self.coup.numero_joueur == 2 else 2),self.numero_joueur_base))

            for noeud_fils in self.liste_noeuds_fils:
                noeud_fils.developper_fils()


    def tester_victoire_defaite_ou_nul_noeuds(self):

        joueur_adverse = 1 if self.numero_joueur_base == 2 else 1

        if self.etat_grille.a_gagne(self.numero_joueur_base):
            return 1
        elif self.etat_grille.a_gagne(joueur_adverse):
            return -1
        elif self.etat_grille.est_nulle():
            return 0
        else:
            return None


    def afficher_noeud(self,niveau_actuel):
        print(f'Niveau : {niveau_actuel}\n')
        vue.afficher_grille(self.etat_grille.grille)
        print(f'valeur du noeud : {self.valeur}')
        print("------------------------------")





