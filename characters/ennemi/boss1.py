from ennemi import Ennemi


class Boss1(Ennemi):
    """Class Boss1, le premier Ennemi"""

    # Constructeur
    def __init__(self):
        """
        Constructeur de la classe Boss1, déclare les attributs.
        :param self: (Boss1)
        :return: (None)
        """
        super().__init__()
        self._PV = 300
        self._img = "img/ennemi/boss1.png"

    def lanceAttaque(self) -> int:
        """
        Lance une attaque propre au Boss1
        :param self: (Boss1)
        :return: (int)
        """
        return self._attaque
