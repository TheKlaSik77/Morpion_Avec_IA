class VueIncorrecte(Exception):
    """exception levée quand la vue n'est pas définie"""

    def __init__(self, message="La vue indiquée est incorrecte. Seules \"Console\" ou \"Interface\" sont des vues correctes."):
        self.message = message
        super().__init__(self.message)
