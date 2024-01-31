# ---------------
# Importations
# ---------------
from __future__ import annotations
from abc import ABC
from capacite import Capacite


# ------------------
# Classe Personnage
# ------------------
class Personnage(ABC):
    """Classe abstraite Personnage"""

    # Constructeur
    def __init__(self: Personnage,
                 nom: str,
                 role: str,
                 pv: int,
                 pvmax: int,
                 attaque: int,
                 defense: int,
                 affinite: dict[str, list],
                 capacite: Capacite,
                 images: dict[str, str]):
        """Constructeur de la classe Personnage"""
        self._nom: str = nom
        self._role: str = role
        self._PV: int = pv
        self._PV_max: int = pvmax
        self._ATK: int = attaque
        self._DEF: int = defense
        self._affinite: dict[str, list] = affinite
        self._capacite: Capacite = capacite
        self._images: dict[str, str] = images


    # --------- Getters / Setters ---------
    @property
    def nom(self: Personnage) -> str: return self._nom
    
    @property
    def role(self: Personnage) -> str: return self._role

    @property
    def PV(self: Personnage) -> int: return self._PV
    
    @property
    def PV_max(self: Personnage) -> int: return self._PV_max
    
    @property
    def ATK(self: Personnage) -> int: return self._ATK
    
    @property
    def DEF(self: Personnage) -> int: return self._DEF
    
    @property
    def affinite(self: Personnage) -> dict[str, list]: return self._affinite
    
    @property
    def capacite(self: Personnage) -> Capacite: return self._capacite
    
    @property
    def images(self: Personnage) -> dict[str, str]: return self._images
    
    @PV.setter
    def PV(self: Personnage, pv: int) -> None:
        self._PV = pv if pv <= self._PV_max else self._PV_max
    # ------------------------------------

    def recevoirCoup(self, dgts, attaquant = None) -> None:
        """Méthode par défaut pour recevoir un coup"""
        degat = max(3, round(dgts * (1 - self._DEF / 100 * 0.5))) # Réduction de 50% de la défense
        self._PV -= degat
        if self._PV < 0:
            self._PV = 0

    def lancerAttaque(self, cible) -> None:
        """Méthode par défaut pour lancer une attaque"""
        cible.recevoirCoup(self._ATK)

    def __repr__(self: Personnage) -> str: return str(self._nom)