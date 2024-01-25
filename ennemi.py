# --------------
# Classe Ennemis
# --------------
class Ennemi:
    """Classe Ennemi"""

    def __init__(self: Ennemi):
        """
        Constructeur de la classe Ennemi, déclare les attributs.
        :param self: (Ennemi)
        :return: (None)
        """
        self._PV: int
        self._attaque: int = 10
        self._defense: int = 10
        self._img: str

    def getPV(self: Ennemi) -> int:
        """
        Renvoie les points de vie d'un ennemi.
        :param self: (Ennemi)
        :return: (int)
        """
        return self._PV

    def getATK(self: Ennemi) -> int:
        """
        Renvoie l'attaque d'un ennemi.
        :param self: (Ennemi)
        :return: (int)
        """
        return self._attaque

    def getImg(self: Ennemi) -> str:
        """
        Renvoie le chemin de l'image d'un ennemi.
        :param self: (Ennemi)
        :return: (String)
        """
        return self._img

    def recevoirCoup(self: Ennemi, dgts: int) -> None:
        """
        Recoie un coup selon les degats subits.
        :param self: (Ennemi)
        :param dgts: (int)
        :return: (None)
        :effet de bord: modifie _PV et lance une autre methode
        """
        degat = round(dgts - (self._defense / 2))
        degat = degat if degat >= 1 else 1
        self._PV -= degat
        if self._PV < 0:
            self._PV = 0