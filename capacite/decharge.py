from __future__ import annotations
from capacite import Capacite

class Decharge(Capacite):
    """Capacité concrète de Décharge"""
    
    def __init__(self):
        self.passif = False
        self.cooldown = 3

    def utiliser(self, personnage, cible):
        """Soigne un personnage ciblé"""
        print(f"{personnage} -> decharge sur {cible}")
        cible.recevoirCoup(personnage.ATK + (personnage.ATK/2))