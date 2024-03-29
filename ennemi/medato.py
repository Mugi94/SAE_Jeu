# ---------------
# Importations
# ---------------
from __future__ import annotations
from ennemi import Ennemi
from random import choice

import constants as const

class Medato(Ennemi):
    
    def __init__(self):
        super().__init__('"Fake god" Medato Amadeus',
                         400, 400, 10, 10,
                         f"{const.PATH}/img/ennemi/medato.png")
    
    def lancerAttaque(self, plateau, lieu):
        degat = self._ATK
        perso_cible = choice(plateau.personnages)
        case_cible = plateau.personnages_case(perso_cible.position)
        cases_attaque = [perso_cible.position]
        
        self.attaqueCase(case_cible, plateau, lieu)

        for autre_personnage in plateau.personnages:
            if not isinstance(autre_personnage, type(perso_cible)):
                if autre_personnage.position not in cases_attaque:
                    cases_attaque.append(autre_personnage.position)
                    autre_personnage.recevoirCoup(round(degat*0.3), self, plateau, lieu)

        return 0