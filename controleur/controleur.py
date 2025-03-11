from controleur.partie import Partie
from vue.vue_console import Vue_Console

class Controleur:

    def __init__(self,vue,nb_joueurs):
        self.partie = Partie(nb_joueurs)
        if vue == "console":
            self.vue = Vue_Console()

    def deroulement_joueur(self):
        """
        Déroule la partie jusqu'à la fin
        """
        self.vue.afficher_grille(self.partie.grille.get_grille())
        tour = 1
        while not self.partie.partie_terminee():
            # On met à jour le joueur en cours
            numero_joueur_en_cours = 1 if tour % 2 != 0 else 2
            ligne, colonne = self.vue.saisir_coup()
            coup_valide = self.partie.joueur_joue(ligne, colonne, numero_joueur_en_cours)
            while not coup_valide:
                ligne, colonne = self.vue.saisir_coup()
                coup_valide = self.partie.joueur_joue(ligne, colonne, numero_joueur_en_cours)
            self.vue.afficher_grille(self.partie.grille.get_grille())
            tour += 1

    def deroulement_IA(self):
        """
        Déroule la partie jusqu'à la fin
        """
        self.vue.afficher_grille(self.partie.grille.get_grille())
        tour = 1
        while not self.partie.partie_terminee():
            # On met à jour le joueur en cours
            numero_joueur_en_cours = 1 if tour % 2 != 0 else 2

            ligne, colonne = self.vue.saisir_coup()

            coup_valide = self.partie.joueur_joue(ligne, colonne, numero_joueur_en_cours)
            while not coup_valide:
                ligne, colonne = self.vue.saisir_coup()
                coup_valide = self.partie.joueur_joue(ligne, colonne, numero_joueur_en_cours)
            self.vue.afficher_grille(self.partie.grille.get_grille())
            tour += 1


