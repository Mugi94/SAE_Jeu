# ---------------
# Importations
# ---------------   
from __future__ import annotations
from personnage import Personnage
from capacite import Reflexion

import constants as const

class Bob(Personnage):

    def __init__(self):
        super().__init__("Bob Bob",
                         100, 100, 4, 7, 
                         {"haute": [1], "faible": [4]},
                         Reflexion(), 
                         {
                             "carte": f"{const.PATH}/img/personnages/bob/bobcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/bob/bobcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/bob/bob.png"
                         })

    def recevoirCoup(self, dgts, attaquant) -> None:
        degat = max(3, round(dgts * (1 - self._DEF / 100 * 0.5)))
        self._PV -= degat
        if self._PV < 0:
            self._PV = 0