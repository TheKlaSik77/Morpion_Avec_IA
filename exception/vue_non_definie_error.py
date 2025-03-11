class VueNonDefinieError(Exception):
    """exception levée quand la vue n'est pas définie"""

    def __init__(self, message="La vue n'est pas définie"):
        self.message = message
        super().__init__(self.message)
