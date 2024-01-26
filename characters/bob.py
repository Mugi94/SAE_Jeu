# ---------------
# Personnage Bob
# ---------------
from os import path
from personnage import Personnage


class Bob(Personnage):
    """Classe Bob, sous classe de Personnage"""

    # Constructeur
    def __init__(self):
        """
        Constructeur de la classe Bob, initialise les attributs.
        :param self: (Bob)
        :return: (None)
        """
        super().__init__()
        self._nom = "Bob bob"
        self._attaque = 3
        self._defense = 9
        self._typePers = 4
        self._typeInversePers = 2
        self._carte = f"{path}/img/personnages/bob/bobcarte.png"
        self._img = f"{path}/img/personnages/bob/bobimg.png"

    # -------------Méthodes-------------
    def recevoirCoup(self, dgts: int) -> int:
        """
        Recoie un coup et lance la capacité automatiquement
        :param self: (Bob)
        :param dgts: (int)
        :return: (int)
        :effet de bord: modifie _PV et lance une autre methode
        """
        degat = round(dgts - (self._defense / 2))
        degat = degat if degat >= 3 else 3
        self._PV = self._PV - degat
        if self._PV < 0:
            self._PV = 0
        return self.lanceCapacite(dgts)

    def lanceCapacite(self, dgts: int) -> int:
        """
        Renvoie les dégâts subit.
        :param self: (Bob)
        :param dgts: (int) les dégâts subit
        :return: (int)
        """
        return dgts
