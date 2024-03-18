# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class Erika(Personnage):
    
    def __init__(self):
        super().__init__("Erika Nishimura",
                         100, 100, 10, 6, 
                         {"haute": [2], "faible": [3]}, 
                         None, 
                         {
                             "carte": f"{const.PATH}/img/personnages/erika/erikacarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/erika/erikacartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/erika/erika.png"
                         })
    
    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)