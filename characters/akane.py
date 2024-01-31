# ---------------
# Importations
# ---------------
from __future__ import annotations
from personnage import Personnage
from capacite import Reduction


class Akane(Personnage):

    def __init__(self):
        super().__init__("Akane Kagari", "Défense",
                         100, 100, 4, 7,
                         {"haute": [1], "faible": [4]},
                         Reduction(),
                         {"carte": "carte.png", "icone": "icone.png"})

        self.capacite_active = False

    def lancerAttaque(self, cible) -> None:
        super().lancerAttaque(cible)

    def recevoirCoup(self, dgts) -> None:
        if self.capacite_active:
            self.capacite.utiliser(self, dgts)
            self.capacite_active = False
        else:
            super().recevoirCoup(dgts)

    def lancerCapacite(self):
        self.capacite_active = True
