from controleur.partie import Partie

def main():
    # vues possibles : "Console" et "Interface"
    type_vue = "Console"
    partie = Partie(1,type_vue)
    partie.derouler_partie()

if __name__ == "__main__":

    main()