from random import choice, randint
from ennemi import Ennemi
from os import path
from personnage import Personnage
from plateau import Plateau


class Boss2(Ennemi):
    """Class Boss2, le premier Ennemi"""

    # Constructeur
    def __init__(self):
        """
        Constructeur de la classe Boss2, déclare les attributs.
        :param self: (Boss2)
        :return: (None)
        """
        super().__init__()
        self._PV = 325
        self._img = f"{path}/img/ennemi/boss2.png"

    def lanceAttaque(self) -> int:
        """
        Lance une attaque propre au Boss2
        :param self: (Boss2)
        :return: (int)
        """
        return self._attaque
    
    def AttaqueSpeciale(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
        """
        Attaque une case contenant un personnage et 5 cases au hasard.
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

        # Attaquer 5 cases au hasard
        for _ in range(4):
            # Récuperer une case au hasard
            num_case = randint(1, plateau.TAILLE)
            case = plateau.getCase(num_case)

            # Si la case contient des personnages et que le personnage cible n'est pas présent
            if case.getPersonnages() != []:
                if not perso_cible in case.getPersonnages():
                    # Attaquer la case
                    attaqueCase(case.getPersonnages(), ennemi, degat)

        return plateau, ennemi
