from modele.grille import Grille
from joueur.humain.humain import Humain
from joueur.ia.ia_aleatoire import IA_Aleatoire
import vue.vue_console as console
from exception.vue_incorrecte import VueIncorrecte
from exception.numero_joueur_incorrect import NumeroJoueurIncorrect


class Partie:

    def __init__(self,nb_joueurs,type_vue):
        """
        :param nb_joueurs: 1 joueur = joueur vs ia | 2 joueurs = joueur vs joueur
        :param type_vue: Console ou Interface pour savoir comment joueur fait l'input
        """
        self.grille = Grille()
        if nb_joueurs == 1:
            self.joueur1 = Humain("Joueur 1",1)
            self.joueur1.set_vue(type_vue)

            self.joueur2 = IA_Aleatoire(2)
        else :
            self.joueur1 = Humain("Joueur 1",1)
            self.joueur1.set_vue(type_vue)

            self.joueur2 = Humain("Joueur 2",2)
            self.joueur2.set_vue(type_vue)

        self.type_vue = type_vue

    def derouler_partie(self):
        self.appeler_affichage_grille()
        tour = 1
        while not self.partie_terminee():
            # On met à jour le joueur en cours
            numero_joueur_en_cours = 1 if tour % 2 != 0 else 2

            # Le joueur joue et on teste si son coup est valide
            coup = self.get_joueur(numero_joueur_en_cours).envoyer_coup_a_partie(self.grille)
            coup_est_valide = self.grille.emplacement_est_vide(coup)

            while not coup_est_valide:
                print("Coup invalide, veuillez indiquez un autre coup\n")
                coup = self.get_joueur(numero_joueur_en_cours).envoyer_coup_a_partie(self.grille)
                coup_est_valide = self.grille.emplacement_est_vide(coup)

            self.grille.poser_coup(coup,numero_joueur_en_cours)
            self.appeler_affichage_grille()
            tour += 1

    def get_joueur(self,numero_joueur):
        if numero_joueur == 1:
            return self.joueur1
        elif numero_joueur == 2:
            return self.joueur2
        else:
            raise NumeroJoueurIncorrect()

    def appeler_affichage_grille(self):
        """
        Affiche la vue correspondante selon le type_vue
        """
        if self.type_vue == "Console":
            console.afficher_grille(self.grille.get_grille())
        else:
            raise VueIncorrecte()

    def afficher_coup_invalide(self):
        """
        Affiche que le coup est invalide selon la vue choisie
        """
        if self.type_vue == "Console":
            print("Le coup renseigné est invalide.")
        else:
            raise VueIncorrecte()

    def partie_terminee(self):
        """
        Teste si la partie est terminée et affiche le nom du gagnant ou match nul si l'un d'eux l'a gagné.
        :return:
        """
        if self.grille.a_gagne(1):
            print(f"Victoire de {self.joueur1.nom}")
            return True
        elif self.grille.a_gagne(2):
            print(f"Victoire de {self.joueur2.nom}")
            return True
        elif self.grille.est_nulle():
            print("Match nul")
            return True
        return False




