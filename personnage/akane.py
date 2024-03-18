# ---------------
# Importations
# ---------------   
from __future__ import annotations
from personnage import Personnage
from capacite import Reduction

import constants as const

class Akane(Personnage):

    def __init__(self):
        super().__init__("Akane Kagari",
                         100, 100, 4, 7, 
                         {"haute": [1], "faible": [4]},
                         Reduction(), 
                         {
                             "carte": f"{const.PATH}/img/personnages/akane/akanecarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/akane/akanecartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/akane/akane.png"
                         })

        self.capacite_active = False

    def recevoirCoup(self, dgts, attaquant) -> None:
        if self.capacite_active:
            self.capacite.utiliser(self, dgts)
            self.capacite_active = False
        else:
            super().recevoirCoup(dgts, attaquant)

    def lancerCapacite(self):
        self.capacite_active = True