# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage
from capacite import Decharge


class Aurore(Personnage):

    def __init__(self):
        super().__init__("Aurore Thercieux", "Attaque",
                         100, 100, 10, 6,
                         {"haute": [2], "faible": [3]},
                         Decharge(),
                         {"carte": "carte.png", "icone": "icone.png"})

    def lancerAttaque(self, cible) -> None:
        super().lancerAttaque(cible)

    def recevoirCoup(self, dgts) -> None:
        super().recevoirCoup(dgts)

    def lancerCapacite(self, cible):
        self._capacite.utiliser(cible)
