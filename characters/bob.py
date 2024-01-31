# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage
from capacite import Reflexion


class Bob(Personnage):

    def __init__(self):
        super().__init__("Bob Bob", "Défense",
                         100, 100, 4, 7,
                         {"haute": [1], "faible": [4]},
                         Reflexion(),
                         {"carte": "carte.png", "icone": "icone.png"})

    def lancerAttaque(self, cible) -> None:
        super().lancerAttaque(cible)

    def recevoirCoup(self, dgts, attaquant) -> None:
        degat = max(3, round(dgts * (1 - self._DEF / 100 * 0.5)))
        self._PV -= degat
        if self._PV < 0:
            self._PV = 0
        self.capacite.utiliser(attaquant, dgts)
