from ennemi import Ennemi


class Boss3(Ennemi):
    """Class Boss3, le premier Ennemi"""

    # Constructeur
    def __init__(self: Boss3):
        """
        Constructeur de la classe Boss3, déclare les attributs.
        :param self: (Boss3)
        :return: (None)
        """
        super().__init__()
        self._PV = 350
        self._img = f"{PATH}/img/ennemi/boss3.png"

    def lanceAttaque(self: Boss3) -> int:
        """
        Lance une attaque propre au Boss3
        :param self: (Boss3)
        :return: (int)
        """
        return self._attaque
