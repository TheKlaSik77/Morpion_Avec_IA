import time
from modele.coup import Coup
from modele.grille import Grille
from modele.joueur.ia.arbre.arbre_minimax import Arbre_Minimax
from modele.joueur.joueur import Joueur
import vue.vue_console as vue


# Fonction utilitaire pour convertir une durée en secondes en minutes et secondes
def afficher_temps(duree):
    minutes = int(duree // 60)
    secondes = int(duree % 60)
    return f"{minutes}m {secondes}s"



#
# grille = Grille()
# grille.poser_coup(Coup((0,0),1))
# grille.poser_coup(Coup((1,1),2))
# grille.poser_coup(Coup((2,2),1))
#
# arbre = Arbre_Minimax(grille,2)
# grille.poser_coup(Coup((2,1),2))
# grille.poser_coup(Coup((2,0),1))
# arbre.mettre_a_jour_noeud_initiaux(grille)
#
# vue.afficher_grille(grille)
# print("-----------------------------")
# for noeud in arbre.noeuds_initiaux:
#     vue.afficher_grille(noeud.etat_grille)

# start_time = time.time()  # Capturer le temps de départ
# grille.poser_coup(Coup((0,0),1))
# vue.afficher_grille(grille.grille)
# arbre = Arbre_Minimax(grille, 2)
# arbre.creer_noeuds_initiaux()
# end_time = time.time()
# print(f"noeuds_initiaux crées en {afficher_temps(end_time - start_time)}")
#
# # Mesurer le temps de création des branches
# start_time = time.time()
# arbre.creer_branches()  # Long (sur grille vide : 15s)
# end_time = time.time()
# print(f"branches créées en {afficher_temps(end_time - start_time)}")
#
# # Calculer valeurs
# start_time = time.time()
# arbre.calculer_valeurs_noeuds_initiaux()    # Très long
# end_time = time.time()
# print(f"calcul fait en {afficher_temps(end_time - start_time)}")

# # Afficher l'arbre
# start_time = time.time()
# arbre.afficher_arbre()
# end_time = time.time()
# print(f"arbre affiché en {afficher_temps(end_time - start_time)}")

# # Envoyer le coup
# start_time = time.time()
# print(arbre.envoie_coup_valeur_max())
# end_time = time.time()
# print(f"coup envoyé en {afficher_temps(end_time - start_time)}")
