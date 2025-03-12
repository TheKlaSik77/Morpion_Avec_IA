from modele import joueur as vue
from modele.joueur.joueur import Joueur
from exception.vue_non_definie_error import VueNonDefinieError

class Humain(Joueur):

    def __init__(self, nom, numero_joueur):
        super().__init__(nom, numero_joueur)
        self.vue = None

    def set_vue(self,type_vue):
        """
        :param type_vue: "Console" ou "Interface"
        set vue
        """
        self.vue = type_vue

    def envoyer_coup_a_partie(self, grille = None):
        """

        :param grille: est non utilisée pour le joueur qui se contente juste de proposer une case.
        :return:
        """
        if self.vue is None or (self.vue != "Console" and self.vue != "Interface"):
            raise VueNonDefinieError()
        if self.vue == "Console":
            return vue.saisir_coup_terminal()




