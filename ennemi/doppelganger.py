# ---------------
# Importations
# ---------------
from __future__ import annotations
from ennemi import Ennemi
from random import choice, randint

import constants as const

class Doppelganger(Ennemi):
    
    def __init__(self):
        super().__init__("Aurore's doppelganger",
                         325, 325, 10, 10,
                         f"{const.PATH}/img/ennemi/doppelganger.png")
    
    def lancerAttaque(self, plateau):
        perso_cible = choice(plateau.personnages)
        case_cible = plateau.case(perso_cible.position)
        self.attaqueCase(case_cible)

        for _ in range(4):
            num_case = randint(1, plateau.TAILLE)
            case = plateau.case(num_case)

            if case.personnages != []:
                if perso_cible not in case.personnages:
                    self.attaqueCase(case)

        return 0