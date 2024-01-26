from ennemi import Ennemi
from os import path
from personnage import Personnage
from plateau import Plateau
from random import choice


class Boss3(Ennemi):
    """Class Boss3, le premier Ennemi"""

    # Constructeur
    def __init__(self):
        """
        Constructeur de la classe Boss3, déclare les attributs.
        :param self: (Boss3)
        :return: (None)
        """
        super().__init__()
        self._PV = 350
        self._img = f"{path}/img/ennemi/boss3.png"

    def lanceAttaque(self) -> int:
        """
        Lance une attaque propre au Boss3
        :param self: (Boss3)
        :return: (int)
        """
        return self._attaque

    def AttaqueSpeciale(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
        """
        Attaque une case contenant un personnage et les cases a coté.
        :param plateau: (Plateau)
        :param ennemi: (Ennemi)
        :return: (tuple) le plateau et ennemi apres attaque
        :effet de bord: modifie les personnages plateau et l'ennemi optionnellement
        """
        from main import attaqueCase
        
        # Degat envoyé sur un personnage
        degat: int = ennemi.lanceAttaque()
        perso_cible: Personnage = choice(plateau.getPersosPlateau())
        
        # Attaquer la case du personnage cible
        attaqueCase(plateau.getPersosCase(perso_cible.getCaseNum()), ennemi, degat)
        
        # Attaque la case de devant
        # Vérification case suivante dans le plateau
        if (perso_cible.getCaseNum() + 1) <= plateau.TAILLE:
            attaqueCase(plateau.getPersosCase(perso_cible.getCaseNum() + 1), ennemi, degat)
        else: # Sinon on reviens a la case 1
            attaqueCase(plateau.getPersosCase(1), ennemi, degat)
        
        # Attaque la case de derriere
        # Vérification case derriere dans le plateau
        if (perso_cible.getCaseNum() - 1) >= 1:
            attaqueCase(plateau.getPersosCase(perso_cible.getCaseNum() - 1), ennemi, degat)
        else: # Sinon on est a la case 16
            attaqueCase(plateau.getPersosCase(16), ennemi, degat)
        
        return plateau, ennemi