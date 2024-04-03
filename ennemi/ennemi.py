# ---------------
# Importations
# ---------------
from __future__ import annotations
from abc import ABC, abstractmethod
from pygame.font import SysFont
from pygame.image import load
import pygame

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
                 image: str):
        """Constructeur de la classe Ennemi"""
        self._nom: str = nom
        self._PV: int = pv
        self._PV_max: int = pvmax
        self._ATK: int = attaque
        self._DEF: int = defense
        self._image: str = image


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
    def image(self: Ennemi) -> str: return self._image

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
    def lancerAttaque(self, plateau, cible, lieu) -> None:
        pass
    
    def attaqueCase(self, case, plateau, lieu):
        for personnage in case.personnages:
            personnage.recevoirCoup(self._ATK, self, plateau, lieu)
    
    def draw(self, screen):
        game_font = SysFont("Helvetic", 30)
        width = screen.get_width()
        height = screen.get_height()

        ennemi_nom = game_font.render(self._nom, True, (0, 0, 0))
        ennemi_image = load(self._image)
        
        pourcentage_pv = min((self._PV / self._PV_max), 1.0)
        taille_barre_vie = int(pourcentage_pv * 432)
        pygame.draw.rect(screen, (255,136,0), (424, 144, (self._PV_max * 144) / 100, 25))
        pygame.draw.rect(screen, (0,204,204), (424, 144, taille_barre_vie, 25))

        screen.blit(ennemi_image, (width*0.41, height*0.26))
        screen.blit(ennemi_nom, ennemi_nom.get_rect(center=(width*0.5, height*0.22)))

    def __repr__(self: Ennemi) -> str: return str(self._nom)