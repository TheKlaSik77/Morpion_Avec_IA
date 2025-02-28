
class Vue_Console:

    def __init__(self):
        pass

    @staticmethod
    def traitement_entree(entree):
        """
        Prend en paramètre une chaîne de format XY (par exemple : A2), 
        et retourne une paire de coordonnées ligne-colonne correspondante.
        """
        if len(entree) != 2 or not ('A' <= entree[0].upper() <= 'C') or not ('1' <= entree[1] <= '3'):
            return False
    
        ligne = ord(entree[0].upper()) - ord('A')  # Convertit 'A', 'B', 'C' en 0, 1, 2
        colonne = int(entree[1]) - 1  # Convertit '1', '2', '3' en 0, 1, 2
    
        return ligne, colonne

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
    def croix_ou_rond(nombre):
        """
        renvoie un espace pour 0, X pour 1 et O pour 2
        """
        match nombre:
            case 0:
                return ' '
            case 1:
                return 'X'
            case 2:
                return 'O'

    @staticmethod
    def afficher_grille(grille):
        ligne0 = "   1    2    3\n"
        ligne1 = f"A\t{Vue_Console.croix_ou_rond(grille[0][0])} | {Vue_Console.croix_ou_rond(grille[0][1])} | {Vue_Console.croix_ou_rond(grille[0][2])} \n"
        ligne2 = "   ------------\n"
        ligne3 = f"B\t{Vue_Console.croix_ou_rond(grille[1][0])} | {Vue_Console.croix_ou_rond(grille[1][1])} | {Vue_Console.croix_ou_rond(grille[1][2])} \n"
        ligne4 = "   ------------\n"
        ligne5 = f"C\t{Vue_Console.croix_ou_rond(grille[2][0])} | {Vue_Console.croix_ou_rond(grille[2][1])} | {Vue_Console.croix_ou_rond(grille[2][2])} \n"


        print(ligne0 + ligne1 + ligne2 + ligne3 + ligne4 + ligne5)

