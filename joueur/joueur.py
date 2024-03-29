from __future__ import annotations
from random import randint
import pygame

class Joueur:
    def __init__(self, personnage, nom = 'Joueur'):
        self._nom = nom
        self._personnage = personnage

        self.de_lancer = False
        self.personnage_deplacer = False
        self.action = 0
        self.action_effectuer = False
        self.cooldown = personnage.capacite['temps_rechargement']

    @property
    def nom(self): return self._nom

    @property
    def personnage(self): return self._personnage

    @nom.setter
    def nom(self, nom): self._nom = nom

    @personnage.setter
    def personnage(self, personnage): self._personnage = personnage

    def lancer_de(self, bouton):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if bouton.checkForInput(mouse_pos) and click[0] == 1:
            self.de_lancer = True
            resultat_de = randint(1,6)
            print(f"{self._nom} lance un dé et a fait {resultat_de} !")
            return resultat_de

    def choix_deplacement(self, choix_possible, plateau, position):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for choix in choix_possible:
            personnage_case = choix + position % 16
            if personnage_case > 16:
                personnage_case -= 16

            if plateau.zone_cliquable[personnage_case].collidepoint(mouse_pos) and click[0] == 1:
                self.personnage_deplacer = True
                return choix

    def choix_action(self, bouton_attaque, bouton_capacite):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if bouton_attaque.checkForInput(mouse_pos) and click[0] == 1:
            return 1

        if bouton_capacite.checkForInput(mouse_pos) and click[0] == 1:
            if not (self._personnage.capacite['passive'] or self._personnage.capacite['active']):
                return 2

    def choix_capacite(self, plateau, personnages):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for personnage in personnages.keys():
            if personnages[personnage].collidepoint(mouse_pos) and click[0] == 1:
                return personnage

    def __repr__(self): return self._nom