from modele.joueur.joueur import Joueur


class IA(Joueur):

    def __init__(self, numero_joueur):
        super().__init__("IA", numero_joueur)

    def envoyer_coup_a_partie(self, grille):
        raise NotImplementedError("Fonction doit être implémentée dans classes filles")