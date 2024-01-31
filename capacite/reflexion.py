# ---------------
# Importations
# ---------------   
from __future__ import annotations
from capacite import Capacite

class Reflexion(Capacite):
    """Capacité concrète de reflexion"""
    
    def __init__(self):
        self.passif = True
        self.cooldown = 0
    
    def utiliser(self, personnage, cible, dgts):
        print(f"{personnage} renvoie les {dgts} de dégats reçu")
        cible.recevoirCoup(dgts)