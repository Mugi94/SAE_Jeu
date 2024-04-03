# ---------------
# Importations
# ---------------   
from __future__ import annotations
from personnage import Personnage

import constants as const

class Akane(Personnage):

    def __init__(self):
        super().__init__("Akane Kagari",
                         100, 100, 5, 7, 
                         {
                             "haute": [1],
                             "faible": [4]
                         },
                         
                         {
                            "nom": "Offense Armor",
                            "type": "Defense",
                            "description": "Bloque la prochaine attaque subit",
                            "temps_rechargement": 1,
                            "passive": False,
                            "choix_necessaire": False,
                            "active": False
                         },
 
                         {
                             "carte": f"{const.PATH}/img/personnages/akane/akanecarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/akane/akanecartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/akane/akane.png"
                         })

    def recevoirCoup(self, dgts, attaquant, plateau, lieu) -> None:
        if self._est_protege:
            print(f"{self._nom} bloque l'attaque!")
            self._est_protege = False
            self._capacite['active'] = False
        else:
            super().recevoirCoup(dgts, attaquant, plateau, lieu)

    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi):
        self._est_protege = True
        self._capacite['active'] = True