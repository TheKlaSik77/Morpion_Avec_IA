class NumeroJoueurIncorrect(Exception):
    """exception levée quand la vue n'est pas définie"""

    def __init__(self, message="Le numéro de joueur renseigné est incorrect."):
        self.message = message
        super().__init__(self.message)