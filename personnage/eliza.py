# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage
import pygame

import constants as const

class Eliza(Personnage):
    
    def __init__(self):
        super().__init__("Dr. Eliza de Minerve",
                         100, 100, 5, 5, 
                         {
                             "haute": [4],
                             "faible": []
                         }, 

                         {
                            "nom": "Mental Out",
                            "type": "Special",
                            "description": "Controle un personnage et utilise sa capacité",
                            "temps_rechargement": 3,
                            "passive": False,
                            "choix_necessaire": True,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/eliza/elizacarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/eliza/elizacartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/eliza/eliza.png"
                         })

    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        if not cible.capacite['passive']:
            if not cible.capacite['choix_necessaire']:
                cible.lancerCapacite(ennemi, plateau, lieu, personnages, cible)