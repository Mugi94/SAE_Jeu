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

                         {
                            "nom": "Materialize",
                            "type": "Support",
                            "description": "Ajoute une case bonus à sa position si la case est neutre",
                            "temps_rechargement": 2,
                            "passive": False,
                            "choix_necessaire": False,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/erika/erikacarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/erika/erikacartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/erika/erika.png"
                         })
    
    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        if plateau.case(self._position).type == 'neutre':
            plateau.case(self._position).type = 'bonus'