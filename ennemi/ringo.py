# ---------------
# Importations
# ---------------
from __future__ import annotations
from ennemi import Ennemi
from random import choice

import constants as const

class Ringo(Ennemi):

    def __init__(self):
        super().__init__("Ringo",
                         300, 300, 10, 10,
                         f"{const.PATH}/img/ennemi/ringo.png")

    def lancerAttaque(self, plateau):
        perso_cible = choice(plateau.personnages)
        case_cible  = plateau.case(perso_cible.position)
        self.attaqueCase(case_cible)
        return 0