
class Vue_Console:

    def __init__(self):
        pass

    @staticmethod
    def traitement_entree(entree):
        """
        Prends des coordoonées (ex : A2) en paramètre et renvoie un numéro de ligne et numéro de colonne
        """
        if len(entree) != 2 or (entree[0].upper() < 'A' or entree[0].upper() > 'C') or (entree[1] < '1' or entree[1] > '3'):
            return False

        ligne, colonne = 0,0
        match entree[0].upper():
            case 'A':
                ligne = 0
            case 'B':
                ligne = 1
            case 'C':
                ligne = 2

        colonne = int(entree[1]) - 1

        return ligne,colonne

    @staticmethod
    def saisir_coup():
        entree = input("Entrer la ligne puis la colonne (exemple : A2) : ")
        coup = Vue_Console.traitement_entree(entree)
        while not coup:
            print('Entrée incorrecte! Veuillez réessayer \n')
            entree = input("Entrer la ligne puis la colonne (exemple : A2) : ")
            coup = Vue_Console.traitement_entree(entree)
        return coup

    @staticmethod
    def afficher_grille(grille):

        ligne1 = f" {grille[0][0]} | {grille[0][1]} | {grille[0][2]} \n"
        ligne2 = "-----------\n"
        ligne3 = f" {grille[1][0]} | {grille[1][1]} | {grille[1][2]} \n"
        ligne4 = "-----------\n"
        ligne5 = f" {grille[2][0]} | {grille[2][1]} | {grille[2][2]} \n"


        return ligne1 + ligne2 + ligne3 + ligne4 + ligne5
