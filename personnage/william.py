# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class William(Personnage):
    
    def __init__(self):
        super().__init__("William Occideum",
                         100, 100, 10, 6, 
                         {"haute": [2], "faible": [3]}, 
                         None, 
                         {
                             "carte": f"{const.PATH}/img/personnages/william/williamcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/william/williamcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/william/william.png"
                         })
    
    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)