# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class AgentK(Personnage):
    
    def __init__(self):
        super().__init__('D1 | Agenf "K"',
                         100, 100, 3, 10, 
                         {
                             "haute": [2,3],
                             "faible": [1,4]
                         },

                         {
                            "nom": "???",
                            "type": "Support",
                            "description": "Augmente la défense d'un personnage",
                            "temps_rechargement": 2,
                            "passive": False,
                            "choix_necessaire": True,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/agentk/agentkcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/agentk/agentkcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/agentk/agentk.png"
                         })
    
    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        cible.DEF += 3
        
        if cible.DEF >= 25:
            cible.DEF = 25