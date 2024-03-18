# ---------------
# Importations
# ---------------
from __future__ import annotations
from ennemi import Ennemi
from random import choice

import constants as const

class Lucifer(Ennemi):
    
    def __init__(self):
        super().__init__("Lucifer",
                         350, 350, 10, 10,
                         f"{const.PATH}/img/ennemi/lucifer.png")
    
    def lancerAttaque(self, plateau):
        personnage_cible = choice(plateau.personnages)

        # Attaquer la case du personnage cible
        case_cible = personnage_cible.position
        self.attaqueCase(case_cible)

        # Attaque la case de devant
        case_cible = personnage_cible.position + 1
        if case_cible > plateau.TAILLE:
            case_cible = 1
        self.attaqueCase(case_cible)

        # Attaque la case de derriere
        case_cible = personnage_cible.position - 1
        if case_cible < 1:
            case_cible = 16
        self.attaqueCase(case_cible)

        return 0