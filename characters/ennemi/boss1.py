from os import path
from random import choice
from ennemi import Ennemi
from personnage import Personnage
from plateau import Plateau


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
        self._img = f"{path}/img/ennemi/boss1.png"

    def lanceAttaque(self) -> int:
        """
        Lance une attaque propre au Boss1
        :param self: (Boss1)
        :return: (int)
        """
        return self._attaque

    def AttaqueSpeciale(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
        """
        Attaque une case contenant un personnage.
        :param plateau: (Plateau)
        :param ennemi: (Ennemi)
        :return: (tuple) le plateau et ennemi apres attaque
        :effet de bord: modifie les personnages plateau et l'ennemi optionnellement
        """
        
        from main import attaqueCase
                
        # Degat envoyé sur un personnage
        degat: int = ennemi.lanceAttaque()
        perso_cible: Personnage = choice(plateau.getPersosPlateau())
        case_perso_cible: list[Personnage] = plateau.getPersosCase(perso_cible.getCaseNum())

        # Attaquer la case du personnage cible
        attaqueCase(case_perso_cible, ennemi, degat)

        return plateau, ennemi