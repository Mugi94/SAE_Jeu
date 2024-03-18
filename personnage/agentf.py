# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class AgentF(Personnage):
    
    def __init__(self):
        super().__init__('E2 | Agenf "F"',
                         100, 100, 10, 6, 
                         {"haute": [2], "faible": [3]}, 
                         None, 
                         {
                             "carte": f"{const.PATH}/img/personnages/agentf/agentfcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/agentf/agentfcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/agentf/agentf.png"
                         })
    
    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)