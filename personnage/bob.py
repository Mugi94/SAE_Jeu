# ---------------
# Importations
# ---------------   
from __future__ import annotations
from personnage import Personnage

import constants as const

class Bob(Personnage):

    def __init__(self):
        super().__init__("Bob Bob",
                         100, 100, 3, 8, 
                         {
                             "haute": [1],
                             "faible": [3]
                         },

                         {
                            "nom": "Accelerator",
                            "type": "Defense",
                            "description": "Renvoie une partie des dégâts reçu",
                            "temps_rechargement": 0,
                            "passive": True,
                            "choix_necessaire": False,
                            "active": False
                         },

                         {
                             "carte": f"{const.PATH}/img/personnages/bob/bobcarte.png",
                             "carte_grise": f"{const.PATH}/img/personnages/bob/bobcartegrise.png",
                             "icone": f"{const.PATH}/img/personnages/bob/bob.png"
                         })

    def recevoirCoup(self, dgts, attaquant, plateau, lieu) -> None:
        degat = max(3, round(dgts * (1 - self._DEF / 100 * 0.5)))
        self._PV -= degat
        if self._PV < 0:
            self._PV = 0

        self.lancerCapacite(attaquant, plateau, lieu, degat)

    def lancerCapacite(self, cible, plateau, lieu, degat):
        # Vérification bonus de case
        if plateau.case(self._position).type == 'bonus':
            degat += 2
        elif plateau.case(self._position).type == 'malus':
            degat -= 2

        # Verification bonus de lieu
        if self._affinite['haute'] == lieu:
            degat += 3
        elif self._affinite['faible'] == lieu:
            degat -= 3
        
        print(f"{self._capacite['nom']} de {self._nom} s'est activé")
        cible.recevoirCoup(degat)