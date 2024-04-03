# ---------------
# Importations
# ---------------
from __future__ import annotations
from ennemi import Ennemi
from random import choice
import pygame

import constants as const

class Lucifer(Ennemi):
    
    def __init__(self):
        super().__init__("Lucifer",
                         350, 350, 10, 10,
                         f"{const.PATH}/img/ennemi/idk.png")
    
    def lancerAttaque(self, screen, plateau, lieu):
        case_attaque = pygame.image.load(const.CASE_ATTAQUE)
        
        personnage_cible = choice(plateau.personnages)

        # Attaquer la case du personnage cible
        numero_case = personnage_cible.position
        case_cible = plateau.case(numero_case)
        self.attaqueCase(case_cible, plateau, lieu)

        # Attaque la case de devant
        numero_case = personnage_cible.position + 1
        if numero_case > plateau.TAILLE:
            numero_case = 1
        case_cible = plateau.case(numero_case)
        self.attaqueCase(case_cible, plateau, lieu)

        # Attaque la case de derriere
        numero_case = personnage_cible.position - 1
        if numero_case < 1:
            numero_case = 16
        case_cible = plateau.case(numero_case)
        self.attaqueCase(case_cible, plateau, lieu)
        
        screen.blit(case_attaque, plateau.zone_cliquable[personnage_cible.position - 1])
        screen.blit(case_attaque, plateau.zone_cliquable[personnage_cible.position])
        screen.blit(case_attaque, plateau.zone_cliquable[personnage_cible.position + 1])
        return 0