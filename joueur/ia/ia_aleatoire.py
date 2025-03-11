import random
from joueur.ia.ia import IA
from modele.coup import Coup

class IA_Aleatoire(IA):

    def __init__(self, numero_joueur):
        super().__init__(numero_joueur)

    def envoyer_coup_a_partie(self, grille):
        """
        Choisi un coup aléatoire parmi les emplacements disponibles
        :param grille:
        :return: un coup
        """
        liste_emplacements_vides = grille.get_emplacements_cases_vides()
        index_aleatoire = random.randint(0, len(liste_emplacements_vides) - 1)
        return Coup(liste_emplacements_vides[index_aleatoire])

