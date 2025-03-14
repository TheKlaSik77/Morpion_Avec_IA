from modele.coup import Coup
from modele.grille import Grille
from modele.joueur.ia.arbre.arbre_minimax import Arbre_Minimax
from modele.joueur.joueur import Joueur

# Todo :
grille = Grille()
grille.poser_coup(Coup((0,0),1))
arbre = Arbre_Minimax(grille, 2)