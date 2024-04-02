# ---------------
# Importations
# ---------------
from __future__ import annotations
from ennemi import Ennemi
from random import choice
import pygame

import constants as const

class Medato(Ennemi):
    
    def __init__(self):
        super().__init__('"Fake god" Medato Amadeus',
                         400, 400, 10, 10,
                         f"{const.PATH}/img/ennemi/medato.png")
    
    def lancerAttaque(self, screen, plateau, lieu):
        case_attaque = pygame.image.load(const.CASE_ATTAQUE)

        degat = self._ATK
        perso_cible = choice(plateau.personnages)
        case_cible = plateau.case(perso_cible.position)
        cases_attaque = [case_cible]
        
        self.attaqueCase(case_cible, plateau, lieu)
        screen.blit(case_attaque, plateau.zone_cliquable[perso_cible.position])

        for autre_personnage in plateau.personnages:
            if not isinstance(autre_personnage, type(perso_cible)):
                case_personnage = plateau.case(autre_personnage.position)
                
                if case_personnage not in cases_attaque:
                    cases_attaque.append(case_personnage)
                    autre_personnage.recevoirCoup(round(degat*0.3), self, plateau, lieu)
                    screen.blit(case_attaque, plateau.zone_cliquable[autre_personnage.position])
        return 0