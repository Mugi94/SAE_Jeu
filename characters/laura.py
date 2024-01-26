# -----------------
# Personnage Laura
# -----------------
from os import path
from personnage import Personnage


class Laura(Personnage):
    """Classe Laura, sous classe de Personnage"""

    # Constructeur
    def __init__(self):
        """
        Constructeur de la classe Laura, initialise les attributs.
        :param self: (Laura)
        :return: (None)
        """
        super().__init__()
        self._nom = "Laura Occideum"
        self._attaque = 4
        self._defense = 7
        self._typePers = 3
        self._typeInversePers = 1
        self._carte = f"{path}/img/personnages/laura/lauracarte.png"
        self._img = f"{path}/img/personnages/laura/lauraimg.png"
        self.capacite: bool = False

    # -------------Méthodes-------------
    def lanceCapacite(self, pers: Personnage) -> None:
        pers._PV += 20
        if pers.getPV() > 100:
            pers._PV = 100