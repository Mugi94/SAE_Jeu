# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class AgentF(Personnage):
    
    def __init__(self):
        super().__init__('E2 | Agenf "F"',
                         100, 100, 10, 3, 
                         {
                             "haute": [1,4],
                             "faible": [2,3]
                         }, 

                         {
                            "nom": "???",
                            "type": "Support",
                            "description": "Augmente l'attaque d'un personnage",
                            "temps_rechargement": 2,
                            "passive": False,
                            "choix_necessaire": True,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/agentf/agentfcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/agentf/agentfcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/agentf/agentf.png"
                         })
    
    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        cible.ATK += 3
        
        if cible.ATK >= 25:
            cible.ATK = 25