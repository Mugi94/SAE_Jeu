# ---------------
# Importations
# ---------------
from __future__ import annotations
from ennemi import Ennemi
from random import choice
import pygame

import constants as const

class Ringo(Ennemi):

    def __init__(self):
        super().__init__("Ringo",
                         300, 300, 10, 10,
                         f"{const.PATH}/img/ennemi/ringo.png")

    def lancerAttaque(self, screen, plateau, lieu):
        case_attaque = pygame.image.load(const.CASE_ATTAQUE)

        perso_cible = choice(plateau.personnages)
        case_cible  = plateau.case(perso_cible.position)
        self.attaqueCase(case_cible, plateau, lieu)

        position_cible = perso_cible.position
        if position_cible == 0 : position_cible = 16
        screen.blit(case_attaque, plateau.zone_cliquable[position_cible])
        return 0