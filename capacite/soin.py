from __future__ import annotations
from capacite import Capacite

class Soin(Capacite):
    """Capacité concrète de Soin"""

    def __init__(self):
        self.passif = False
        self.cooldown = 0

    def utiliser(self, personnage, cible):
        """Soigne un personnage ciblé"""
        print(f"{personnage} -> soin sur {cible}")
        cible.PV += int(personnage.PV_max * 0.20) # 20% des pv max d'un personnage
        
        # Si PV après soin dépasse les PV max, mettre les PV a PV max
        if cible.PV > cible.PV_max:
            cible.PV = cible.PV_max