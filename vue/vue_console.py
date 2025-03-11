
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

def afficher_grille(grille):
    ligne0 = "    1   2   3\n"
    ligne1 = f"A\t{croix_ou_rond(grille[0][0])} | {croix_ou_rond(grille[0][1])} | {croix_ou_rond(grille[0][2])} \n"
    ligne2 = "   ------------\n"
    ligne3 = f"B\t{croix_ou_rond(grille[1][0])} | {croix_ou_rond(grille[1][1])} | {croix_ou_rond(grille[1][2])} \n"
    ligne4 = "   ------------\n"
    ligne5 = f"C\t{croix_ou_rond(grille[2][0])} | {croix_ou_rond(grille[2][1])} | {croix_ou_rond(grille[2][2])} \n"


    print(ligne0 + ligne1 + ligne2 + ligne3 + ligne4 + ligne5)

