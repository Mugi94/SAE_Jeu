from random import choice
from characters.bob import Bob
from ennemi import Ennemi
from main import attaqueCase
from personnage import Personnage
from plateau import Plateau


class Boss4(Ennemi):
    """Class Boss1, le premier Ennemi"""

    # Constructeur
    def __init__(self: Boss4):
        """
        Constructeur de la classe Boss4, déclare les attributs.
        :param self: (Boss4)
        :return: (None)
        """
        super().__init__()
        self._PV = 400
        self._img = f"{PATH}/img/ennemi/boss4.png"

    def lanceAttaque(self: Boss4) -> int:
        """
        Lance une attaque propre au Boss4
        :param self: (Boss4)
        :return: (int)
        """
        return self._attaque

    def AttaqueSpeciale(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
        """
        Attaque une case contenant un personnage cible et la case des autres personnages avec les dégats réduits.
        :param plateau: (Plateau)
        :param ennemi: (Ennemi)
        :return: (tuple) le plateau et ennemi apres attaque
        :effet de bord: modifie les personnages plateau et l'ennemi optionnellement
        """
        # Degat envoyé sur un personnage
        degat: int = ennemi.lanceAttaque()
        perso_cible: Personnage = choice(plateau.getPersosPlateau())
        case_perso_cible: list[Personnage] = plateau.getPersosCase(perso_cible.getCaseNum())

        # Liste des cases deja attaque
        num_cases_attaque: list[int] = [perso_cible.getCaseNum()]

        # Attaque la case du personnage cible
        attaqueCase(case_perso_cible, ennemi, degat)

        # Pour les autres personnages du plateau
        for perso in plateau.getPersosPlateau():
            if not isinstance(perso, type(perso_cible)):

                # Si la case n'a pas deja été attaqué
                if perso.getCaseNum() not in num_cases_attaque:
                    num_cases_attaque.append(perso.getCaseNum())

                    # Vérification que l'ennemi ne recoie pas des coup renvoyé
                    if isinstance(perso, Bob):
                        ennemi.recevoirCoup(perso.recevoirCoup(round(degat*0.3)))
                    else: perso.recevoirCoup(round(degat*0.3))

        return plateau, ennemi