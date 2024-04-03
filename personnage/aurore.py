# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage

import constants as const

class Aurore(Personnage):
    
    def __init__(self):
        super().__init__("Aurore Thercieux",
                         100, 100, 10, 6, 
                         {
                             "haute": [1,4],
                             "faible": [2]
                         },

                         {
                            "nom": "Railgun",
                            "type": "Attaque",
                            "description": "Lance une puissante décharge électrique à l'ennemi",
                            "temps_rechargement": 3,
                            "passive": False,
                            "choix_necessaire": False,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/aurore/aurorecarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/aurore/aurorecartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/aurore/aurore.png"
                         })
    
    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        degats = self._ATK + (self._ATK * 0.5)

        # Vérification bonus de case
        if plateau.case(self._position).type == 'bonus':
            degats += 3
        elif plateau.case(self._position).type == 'malus':
            degats -= 3
        
        # Verification bonus de lieu
        if self._affinite['haute'] == lieu:
            degats += 2
        elif self._affinite['faible'] == lieu:
            degats -= 2

        degats = degats if degats > 1 else 1
        
        cible.recevoirCoup(degats)
        return degats