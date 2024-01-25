from ennemi import Ennemi


class Boss2(Ennemi):
    """Class Boss2, le premier Ennemi"""

    # Constructeur
    def __init__(self: Boss2):
        """
        Constructeur de la classe Boss2, déclare les attributs.
        :param self: (Boss2)
        :return: (None)
        """
        super().__init__()
        self._PV = 325
        self._img = f"{PATH}/img/ennemi/boss2.png"

    def lanceAttaque(self: Boss2) -> int:
        """
        Lance une attaque propre au Boss2
        :param self: (Boss2)
        :return: (int)
        """
        return self._attaque
