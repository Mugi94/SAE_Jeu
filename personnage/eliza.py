# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class Eliza(Personnage):
    
    def __init__(self):
        super().__init__("Dr. Eliza de Minerve",
                         100, 100, 10, 6, 
                         {"haute": [2], "faible": [3]}, 
                         None, 
                         {
                             "carte": f"{const.PATH}/img/personnages/eliza/elizacarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/eliza/elizacartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/eliza/eliza.png"
                         })
    
    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)