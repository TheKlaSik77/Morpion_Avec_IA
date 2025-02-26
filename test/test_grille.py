from models import Grille
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

if __name__ == "__main__":
    unittest.main()