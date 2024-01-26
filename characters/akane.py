# -----------------
# Personnage Akane
# -----------------
from os import path
from personnage import Personnage


class Akane(Personnage):
    """Classe Akane, sous classe de Personnage"""

    # Constructeur
    def __init__(self):
        """
        Constructeur de la classe Akane, initialise les attributs.
        :param self: (Akane)
        :return: (None)
        """
        super().__init__()
        self._nom = "Akane Kagari"
        self._attaque = 8
        self._defense = 4
        self._typePers = 1
        self._typeInversePers = 4
        self._carte = f"{path}/img/personnages/akane/akanecarte.png"
        self._img = f"{path}/img/personnages/akane/akaneimg.png"
        self.capacite: bool = False

    # -------------Méthodes-------------
    def recevoirCoup(self, dgts: int) -> None:
        """
        Recoie un coup et lance la capacité automatiquement
        :param self: (Bob)
        :param dgts: (int)
        :return: (None)
        :effet de bord: modifie _PV et lance une autre methode
        """
        degat = round(dgts - (self._defense / 2))
        degat = degat if degat >= 3 else 3
        if self.capacite:
            self._PV -= degat
            self.capacite = False
        else:
            self._PV -= degat
        if self._PV < 0:
            self._PV = 0

    def lanceCapacite(self) -> None:
        """
        Réduit les dégats du prochain coup reçu.
        :param self: (Akane)
        :return: (None)
        """
        self.capacite = True
