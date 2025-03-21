import copy
from modele.coup import Coup
from modele.joueur.ia.arbre.noeud import Noeud
from modele.grille import Grille

class Arbre_Minimax:

    def __init__(self, grille_initiale : Grille, numero_joueur_base):
        self.grille_initiale = copy.deepcopy(grille_initiale)
        self.noeuds_initiaux : list[Noeud] = []
        self.numero_joueur_base = numero_joueur_base
        self.creer_noeuds_initiaux()
        self.creer_branches()
        self.calculer_valeurs_noeuds_initiaux()



    def creer_noeuds_initiaux(self):
        """
        Crée un noeud différent pour chaque emplacement libre de la grille.
        """
        liste_emplacements_vides = self.grille_initiale.get_emplacements_cases_vides()
        for emplacement in liste_emplacements_vides:
            # On crée un noeud pour chaque emplacement, avec son coup, sa grille et son noeud parent (ici None, car initiaux).
            self.noeuds_initiaux.append(Noeud(self.grille_initiale, Coup(emplacement, self.numero_joueur_base),self.numero_joueur_base))


    def creer_branches(self):
        """
        Crée toutes les branches possibles pour tous les noeuds initiaux
        :return:
        """
        for noeud_initial in self.noeuds_initiaux:
            noeud_initial.developper_fils()

    # FIXME: Temps d'exécution beaucoup trop long
    def calculer_valeurs_noeuds_initiaux(self):
        """
        Attribue toutes les valeurs à tous les noeuds issus de chaque noeud initial
        """


        liste_noeud_valeur_nulle = [noeud for noeud in self.noeuds_initiaux if noeud.valeur is None]

        # Tant que la liste n'est pas vide, cela signifie qu'il reste des noeuds dont la valeur est vide.
        while len(liste_noeud_valeur_nulle) != 0:
            for noeud_valeur_nulle in liste_noeud_valeur_nulle:

                if all(noeud_fils.valeur is not None for noeud_fils in noeud_valeur_nulle.liste_noeuds_fils):
                    if noeud_valeur_nulle.coup.numero_joueur == self.numero_joueur_base:
                        noeud_valeur_nulle.valeur = min(noeud_fils.valeur for noeud_fils in noeud_valeur_nulle.liste_noeuds_fils)
                    else:
                        noeud_valeur_nulle.valeur = max(noeud_fils.valeur for noeud_fils in noeud_valeur_nulle.liste_noeuds_fils)
                    liste_noeud_valeur_nulle.remove(noeud_valeur_nulle)

                else :
                    for noeud_fils in noeud_valeur_nulle.liste_noeuds_fils:
                        if noeud_fils.valeur is None:
                            liste_noeud_valeur_nulle.append(noeud_fils)

    def envoie_coup_valeur_max(self):
        """
        :return:
        """
        index_coup_max = 0
        for index_noeud in range (1, len(self.noeuds_initiaux)):
            if self.noeuds_initiaux[index_noeud].valeur > self.noeuds_initiaux[index_coup_max].valeur:
                index_coup_max = index_noeud

        return self.noeuds_initiaux[index_coup_max].coup

    def afficher_arbre(self):
        """
        Affiche l'arbre de décision servant pour le debug de la fonction.
        """
        niveau_actuel = 0
        liste_noeud_a_afficher : list[(Noeud, int)] = []
        for noeud_initial in self.noeuds_initiaux:
            liste_noeud_a_afficher.append((noeud_initial,niveau_actuel))

        n = 0
        while len(liste_noeud_a_afficher) != 0:

            noeud, niveau = liste_noeud_a_afficher.pop(-1)
            noeud.afficher_noeud(niveau)

            while noeud.valeur is None:
                for noeud_fils in noeud.liste_noeuds_fils:
                    niveau_actuel += 1
                    liste_noeud_a_afficher.append((noeud_fils,niveau_actuel))
                print(f'longueur liste noeud a afficher : {len(liste_noeud_a_afficher)}')
                noeud, niveau = liste_noeud_a_afficher.pop(-1)
                noeud.afficher_noeud(niveau)

    def mettre_a_jour_noeud_initiaux(self,nouvelle_grille):
        for noeud_initial in self.noeuds_initiaux:
            for noeud_fils in noeud_initial.liste_noeuds_fils:
                if nouvelle_grille == noeud_fils.etat_grille:
                    self.noeuds_initiaux = noeud_fils.liste_noeuds_fils
                    return