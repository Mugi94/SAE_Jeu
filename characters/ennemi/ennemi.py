# ---------------
# Importations
# ---------------
from __future__ import annotations
from abc import ABC, abstractmethod

# ------------------
# Classe Personnage
# ------------------
class Ennemi(ABC):
    """Classe abstraite Ennemi"""

    # Constructeur
    def __init__(self: Ennemi,
                 nom: str,
                 pv: int,
                 pvmax: int,
                 attaque: int,
                 defense: int,
                 image: dict[str, str]):
        """Constructeur de la classe Ennemi"""
        self._nom: str = nom
        self._PV: int = pv
        self._PV_max: int = pvmax
        self._ATK: int = attaque
        self._DEF: int = defense
        self._images: dict[str, str] = image


    # --------- Getters / Setters ---------
    @property
    def nom(self: Ennemi) -> str: return self._nom

    @property
    def PV(self: Ennemi) -> int: return self._PV

    @property
    def PV_max(self: Ennemi) -> int: return self._PV_max

    @property
    def ATK(self: Ennemi) -> int: return self._ATK

    @property
    def DEF(self: Ennemi) -> int: return self._DEF
    
    @property
    def images(self: Ennemi) -> dict[str, str]: return self._images

    @PV.setter
    def PV(self: Ennemi, pv: int) -> None:
        self._PV = pv if pv <= self._PV_max else self._PV_max

    # ------------------------------------

    def recevoirCoup(self: Ennemi, dgts: int) -> None:
        degat = round(dgts * (1 - self._DEF / 100 * 0.5))
        self._PV -= degat
        if self._PV < 0:
            self._PV = 0

    @abstractmethod
    def lancerAttaque(self, plateau, cible) -> None:
        pass

    def __repr__(self: Ennemi) -> str: return str(self._nom)