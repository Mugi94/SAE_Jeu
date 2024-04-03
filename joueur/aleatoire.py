from random import randint, choice
from joueur import Joueur
import pygame

class Aleatoire(Joueur):
    def __init__(self, personnage):
        if personnage is not None:
            self._nom = personnage.nom
        else:
            self._nom = "Aleatoire"
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
    def personnage(self, personnage): 
        self._nom = personnage.nom
        self._personnage = personnage
    
    def lancer_de(self, bouton):
        self.de_lancer = True
        return randint(1,6)
    
    def choix_deplacement(self, choix_possible, plateau, position):
        pygame.time.wait(1000)
        self.personnage_deplacer = True
        return choice(choix_possible)

    def choix_action(self, bouton_attaque, bouton_capacite):
        pygame.time.wait(1000)
        self.action_effectuer = True
        return choice([1,2])
    
    def choix_capacite(self, plateau, personnages):
        pygame.time.wait(1000)
        return choice(list(personnages.keys()))