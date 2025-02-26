from modele.grille import Grille
import unittest

class TestGrille(unittest.TestCase):

    def test_initialiser_grille(self):
        """
        Vérifie que la grille est correctement initialisée
        """
        grille = Grille()
        grille_test = [[0,0,0],
                       [0,0,0],
                       [0,0,0]
                       ]
        self.assertEqual(grille.grille, grille_test)

    def tester_set_grille(self):
        grille = Grille()
        nouvelle_grille = [
            [1,0,0],
            [0,1,0],
            [2,0,0]
        ]
        grille.set_grille(nouvelle_grille)
        self.assertEqual(grille.grille,nouvelle_grille)

    def tester_poser_coup_valide(self):
        grille = Grille()
        grille_test = [
            [1,0,0],
            [0,1,0],
            [2,0,0]
        ]
        resultat_bon = grille.poser_coup(0,1,2)
        self.assertTrue(resultat_bon)
        self.assertEqual(grille.grille[0][1],2)
        resultat_echec = grille.poser_coup(0,1,1)
        self.assertFalse(resultat_echec)
        self.assertEqual(grille.grille[0][1], 2)


if __name__ == "__main__":
    unittest.main()