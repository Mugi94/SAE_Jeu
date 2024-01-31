from __future__ import annotations
from capacite import Capacite

class Reduction(Capacite):
    """Capacité concrète de Reduction"""

    def __init__(self):
        self.passif = False
        self.cooldown = 2

    def utiliser(self, personnage, dgts):
        """Réduit les dégats qu'un personnage à reçu"""
        print(f"{personnage} -> réduction de dégats, degat recu = {dgts} et a subit {int(dgts * 0.5)}")
        personnage.PV -= int(dgts * 0.5)