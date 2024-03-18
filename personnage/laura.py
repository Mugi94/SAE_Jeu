# ---------------
# Importations
# ---------------   
from __future__ import annotations
from personnage import Personnage
from capacite import Soin

import constants as const

class Laura(Personnage):
    
    def __init__(self):
        super().__init__("Laura Occideum",
                         100, 100, 4, 7, 
                         {"haute": [3], "faible": [1]},
                         Soin(), 
                         {
                             "carte": f"{const.PATH}/img/personnages/laura/lauracarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/laura/lauracartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/laura/laura.png"
                         })
    
    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)