from ennemi import Ennemi


class Boss4(Ennemi):
    """Class Boss1, le premier Ennemi"""

    # Constructeur
    def __init__(self: Boss4):
        """
        Constructeur de la classe Boss4, déclare les attributs.
        :param self: (Boss4)
        :return: (None)
        """
        super().__init__()
        self._PV = 400
        self._img = f"{PATH}/img/ennemi/boss4.png"

    def lanceAttaque(self: Boss4) -> int:
        """
        Lance une attaque propre au Boss4
        :param self: (Boss4)
        :return: (int)
        """
        return self._attaque
