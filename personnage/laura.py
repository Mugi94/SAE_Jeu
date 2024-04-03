# ---------------
# Importations
# ---------------   
from __future__ import annotations
from personnage import Personnage

import constants as const

class Laura(Personnage):
    
    def __init__(self):
        super().__init__("Laura Occideum",
                         100, 100, 5, 6, 
                         {
                             "haute": [3, 2],
                             "faible": [1]
                         },
                         
                         {
                            "nom": "Healing Touch",
                            "type": "Support",
                            "description": "Soigne un personnage choisi à 30% des PV max",
                            "temps_rechargement": 3,
                            "passive": False,
                            "choix_necessaire": True,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/laura/lauracarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/laura/lauracartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/laura/laura.png"
                         })
    
    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        soin = (self._PV_max * 0.30)
        
        # Vérification bonus de case
        if plateau.case(self._position).type == 'bonus':
            soin += (self._PV_max * 0.05)
        elif plateau.case(self._position).type == 'malus':
            soin -= (self._PV_max * 0.05)
        
        # Verification bonus de lieu
        if self._affinite['haute'] == lieu:
            soin += (self._PV_max * 0.05)
        elif self._affinite['faible'] == lieu:
            soin -= (self._PV_max * 0.05)
        
        cible.PV += int(soin)