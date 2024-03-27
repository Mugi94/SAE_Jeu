# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage
from capacite import Decharge

import constants as const

class Aurore(Personnage):
    
    def __init__(self):
        super().__init__("Aurore Thercieux",
                         100, 100, 10, 6, 
                         {
                             "haute": [2],
                             "faible": [3]
                         }, 
                         
                         {
                            "nom": "Décharge"
                         },
                         
                         {
                             "carte": f"{const.PATH}/img/personnages/aurore/aurorecarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/aurore/aurorecartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/aurore/aurore.png"
                         })
    
    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)