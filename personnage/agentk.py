# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class AgentK(Personnage):
    
    def __init__(self):
        super().__init__('D1 | Agenf "K"',
                         100, 100, 10, 6, 
                         {"haute": [2], "faible": [3]}, 
                         None, 
                         {
                             "carte": f"{const.PATH}/img/personnages/agentk/agentkcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/agentk/agentkcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/agentk/agentk.png"
                         })
    
    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)