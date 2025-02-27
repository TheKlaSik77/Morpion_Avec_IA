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

    def tester_poser_coup_valide_invalide(self):
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

    def tester_a_gagne(self):
        grille = Grille()
        grilles_test_true = [
            [
                [1,1,1],
                [0,1,0],
                [2,0,0]
            ],[
                [1,2,1],
                [1,1,1],
                [2,0,0]
            ],[
                [2,1,1],
                [0,2,0],
                [1,1,1]
            ],[
                [1,2,1],
                [1,2,0],
                [1,1,2]
            ],[
                [2,1,1],
                [0,1,0],
                [2,1,1]
            ],[
                [2,1,1],
                [0,2,1],
                [1,2,1]
            ],[
                [1,2,1],
                [0,1,0],
                [2,1,1]
            ],[
                [2,1,1],
                [0,1,0],
                [1,2,1]
            ]
        ]
        grilles_test_false = [
            [
                [2, 1, 1],
                [1, 2, 2],
                [1, 2, 1]
            ],
            [
                [0, 0, 1],
                [0, 0, 0],
                [1, 0, 2]
            ]
        ]
        for assertion in grilles_test_true:
            grille.set_grille(assertion)
            self.assertTrue(grille.a_gagne(1))
        for assertion in grilles_test_false:
            grille.set_grille(assertion)
            self.assertFalse(grille.a_gagne(1))

    def tester_est_nulle(self):
        grille = Grille()
        grilles_test_false = [
            [
                [2, 1, 1],
                [1, 0, 2],
                [1, 2, 1]
            ],
            [
                [0, 0, 2],
                [0, 2, 0],
                [1, 1, 1]
            ]
        ]
        grilles_test_true = [
            [2, 1, 1],
            [1, 2, 2],
            [1, 2, 1]
        ]
        for assertion in grilles_test_false:
            grille.set_grille(assertion)
            self.assertFalse(grille.est_nulle())
        grille.set_grille(grilles_test_true)
        self.assertTrue(grille.est_nulle())

if __name__ == "__main__":
    unittest.main()