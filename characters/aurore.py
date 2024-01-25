# ------------------
# Personnage Aurore
# ------------------
from personnage import Personnage


class Aurore(Personnage):
    """Classe Aurore, sous classe de Personnage"""

    # Constructeur
    def __init__(self: Aurore):
        """
        Constructeur de la classe Aurore, initialise les attributs.
        :param self: (Aurore)
        :return: (None)
        """
        super().__init__()
        self._nom = "Aurore Thercieux"
        self._attaque = 10
        self._defense = 6
        self._typePers = 2
        self._typeInversePers = 3
        self._carte = f"{PATH}/img/personnages/aurore/aurorecarte.png"
        self._img = f"{PATH}/img/personnages/aurore/auroreimg.png"

    # -------------Méthodes-------------
    def lanceCapacite(self: Aurore) -> int:
        """
        Renvoie les dégâts envoyé de la compétence du personnage.
        :param self: (Aurore)
        :return: (int)
        """
        return round(self._attaque + (self._attaque/2))
