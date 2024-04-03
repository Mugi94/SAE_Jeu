# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class William(Personnage):
    
    def __init__(self):
        super().__init__("William Occideum",
                         100, 100, 4, 7, 
                         {
                             "haute": [2],
                             "faible": [3]
                         },

                         {
                            "nom": "Heaven Canceller",
                            "type": "Support",
                            "description": "Réanime un seul personnage au sol à 50% de ses pv max",
                            "temps_rechargement": None,
                            "passive": False,
                            "choix_necessaire": True,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/william/williamcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/william/williamcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/william/william.png"
                         })
    
    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        if cible.PV <= 0:
            cible.PV = int(cible.PV_max / 2)