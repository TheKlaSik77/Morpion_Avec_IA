import copy
from modele.coup import Coup
from modele.joueur.ia.arbre.noeud import Noeud
from modele.grille import Grille

class Arbre_Minimax:

    def __init__(self, grille_initiale : Grille, numero_joueur_base):
        self.grille_initiale = copy.deepcopy(grille_initiale)
        self.noeuds_initiaux = []
        self.numero_joueur_base = numero_joueur_base

    def creer_noeuds_initiaux(self):
        """
        Crée un noeud différent pour chaque emplacement libre de la grille.
        """
        liste_emplacements_vides = self.grille_initiale.get_emplacements_cases_vides()
        for emplacement in liste_emplacements_vides:
            # On crée un noeud pour chaque emplacement, avec son coup, sa grille et son noeud parent (ici None, car initiaux).
            self.noeuds_initiaux.append(Noeud(self.grille_initiale, Coup(emplacement, self.numero_joueur_base), None))

    def creer_branches(self):
        """
        Crée toutes les branches possibles pour tous les noeuds initiaux
        :return:
        """
        for noeud_initial in self.noeuds_initiaux:
            noeud_initial.developper_branches()

    def calculer_valeurs_noeuds_initiaux(self):
        """
        Attribue toutes les valeurs à tous les noeuds issus de chaque noeud initial
        """
        for noeud_initial in self.noeuds_initiaux:
            noeud_initial.calculer_valeurs_noeuds_fils()
            valeur_noeud_initial = 0
            for fils in noeud_initial.liste_noeuds_fils:
                valeur_noeud_initial += fils.valeur
            noeud_initial.valeur = valeur_noeud_initial

    def envoie_coup_valeur_max(self):

        index_coup_max = 0
        for index_noeud in range (1, len(self.noeuds_initiaux)):
            if self.noeuds_initiaux[index_noeud].valeur > self.noeuds_initiaux[index_coup_max].valeur:
                index_coup_max = index_noeud

        return self.noeuds_initiaux[index_coup_max].coup

