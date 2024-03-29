# ---------------
# Importations
# ---------------
from __future__ import annotations
from abc import ABC

# ------------------
# Classe Personnage
# ------------------
class Personnage(ABC):
    """Classe abstraite Personnage"""

    # Constructeur
    def __init__(self: Personnage,
                 nom: str,
                 pv: int,
                 pvmax: int,
                 attaque: int,
                 defense: int,
                 affinite: dict,
                 capacite: dict,
                 images: dict):
        """Constructeur de la classe Personnage"""
        self._nom: str = nom
        self._PV: int = pv
        self._PV_max: int = pvmax
        self._ATK: int = attaque
        self._DEF: int = defense
        self._affinite: dict = affinite
        self._capacite: dict = capacite
        self._images: dict = images
        self._position: int
        self._est_protege: bool = False

    # --------- Getters / Setters ---------
    @property
    def nom(self: Personnage) -> str: return self._nom

    @property
    def PV(self: Personnage) -> int: return self._PV
    
    @property
    def PV_max(self: Personnage) -> int: return self._PV_max
    
    @property
    def ATK(self: Personnage) -> int: return self._ATK
    
    @ATK.setter
    def ATK(self: Personnage, attaque) -> None: self._ATK = attaque

    @property
    def DEF(self: Personnage) -> int: return self._DEF
    
    @DEF.setter
    def DEF(self: Personnage, defense) -> None: self._DEF = defense
    
    @property
    def affinite(self: Personnage) -> dict: return self._affinite
    
    @property
    def capacite(self: Personnage) -> dict: return self._capacite
    
    @property
    def images(self: Personnage) -> dict: return self._images
    
    @PV.setter
    def PV(self: Personnage, pv: int) -> None:
        self._PV = pv

    @property
    def position(self: Personnage) -> int: return self._position

    @position.setter
    def position(self: Personnage, position) -> None: self._position = position
    
    @property
    def est_protege(self: Personnage) -> None: return self._est_protege
    
    @est_protege.setter
    def est_protege(self: Personnage, protection) -> None: self._est_protege = protection
    # ------------------------------------

    def recevoirCoup(self, dgts, attaquant, plateau, lieu) -> None:
        """Méthode par défaut pour recevoir un coup"""
        degat = max(3, round(dgts * (1 - self._DEF / 100 * 0.5))) # Réduction de 50% de la défense
        self._PV -= degat
        if self._PV < 0:
            self._PV = 0

    def lancerAttaque(self, cible, plateau, etape) -> None:
        """Méthode par défaut pour lancer une attaque"""
        degats = self._ATK

        # Bonus affinite
        if etape in self._affinite["haute"]:
            degats += 2
        elif etape in self._affinite["faible"]:
            degats -= 2

        # Bonus position
        if plateau.case(self._position).type == 'bonus':
            degats += 3

        # Sinon si case malus, retirer degats
        elif plateau.case(self._position).type == 'malus':
            degats -= 3
        
        degats = degats if degats > 1 else 1
        cible.recevoirCoup(degats)
        return degats

    def lancerCapacite(self, cible, plateau, lieu, personnages, ennemi, choix, degat):
        pass

    def __repr__(self: Personnage) -> str: return self._nom