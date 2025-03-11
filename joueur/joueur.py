
class Joueur:

    def __init__(self, nom, numero_joueur):
        self.nom = nom

    def envoyer_coup_a_partie(self,grille):
        """
        Le client (joueur) envoie une proposition de coup au serveur (partie)
        :param grille: grille de jeu en l'état actuel
        :return: un coup viable qui sera ensuite vérifié par la partie
        """
        raise NotImplementedError("Fonction doit être implémentée dans classes filles")