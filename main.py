from controleur.controleur import Controleur

def main():
    # vues possibles : "console" et "interface"
    vue_choisie = "console"
    controleur = Controleur(vue_choisie)
    controleur.deroulement()

if __name__ == "__main__":

    main()