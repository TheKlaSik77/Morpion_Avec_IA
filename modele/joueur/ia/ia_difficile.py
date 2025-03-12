from modele.coup import Coup
from modele.joueur.ia.arbre.arbre_minimax import ArbreMinimax
from modele.joueur.ia.ia import IA
from modele.joueur.ia.arbre.arbre_minimax import ArbreMinimax
from modele.joueur.ia.arbre.noeud import Noeud

class IA_Difficile (IA):

    def __init__(self, numero_joueur):
        super().__init__(numero_joueur)


    def envoyer_coup_a_partie(self, grille):
        """
        L'ia choisi le meilleur coup parmi tous les coups possibles avec un algo minimax.
        """
        # On liste tous les coups possibles à jouer pour l'ia
        liste_coups_possibles = [Coup(tupple_emplacement) for tupple_emplacement in grille.get_emplacements_cases_vides()]

        # On crée un noeud avec l'état de la grille en cours et on crée l'arbre minimax avec ce noeud comme noeud initial.
        noeud_initial = Noeud(grille)
        arbre_minimax = ArbreMinimax(noeud_initial)