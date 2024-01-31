# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage
from capacite import Soin


class Laura(Personnage):

    def __init__(self):
        super().__init__("Laura Occideum", "Support",
                         100, 100, 4, 7,
                         {"haute": [3], "faible": [1]},
                         Soin(),
                         {"carte": "carte.png", "icone": "icone.png"})

    def lancerAttaque(self, cible) -> None:
        super().lancerAttaque(cible)

    def recevoirCoup(self, dgts) -> None:
        super().recevoirCoup(dgts)

    def lancerCapacite(self, cible):
        self._capacite.utiliser(self, cible)
