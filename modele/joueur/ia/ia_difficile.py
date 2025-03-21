from modele.coup import Coup
from modele.joueur.ia.ia import IA
from modele.joueur.ia.arbre.arbre_minimax import Arbre_Minimax
from modele.joueur.ia.arbre.noeud import Noeud

class IA_Difficile (IA):

    def __init__(self, numero_joueur):
        super().__init__(numero_joueur)
        self.arbre_minimax = None
        self.numero_joueur = numero_joueur

    def envoyer_coup_a_partie(self, grille):
        """
        L'ia choisi le meilleur coup parmi tous les coups possibles avec un algo minimax.
        """
        # On liste tous les coups possibles à jouer pour l'ia
        liste_coups_possibles = [Coup(tupple_emplacement,self.numero_joueur) for tupple_emplacement in grille.get_emplacements_cases_vides()]

        # On joue au centre si on est le premier coup (pour éviter trop de calculs).
        if len(liste_coups_possibles ) == 9 and self.numero_joueur == 1:
            return Coup((1,1),self.numero_joueur)

        else :
        # On crée un noeud avec l'état de la grille en cours et on crée l'arbre minimax avec ce noeud comme noeud initial.
            if self.arbre_minimax is None:
                self.arbre_minimax = Arbre_Minimax(grille, self.numero_joueur)
            else:
                self.arbre_minimax.mettre_a_jour_noeud_initiaux(grille)
            return self.arbre_minimax.envoie_coup_valeur_max()

