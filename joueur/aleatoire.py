from __future__ import annotations
from joueur import Joueur
from random import randint, choice
import time

class Aleatoire(Joueur):  
    def __init__(self, personnage):
        if personnage is not None:
            self._nom = personnage.nom
        else:
            self._nom = "Aleatoire"
        self._personnage = personnage

        self.de_lancer = False
        self.personnage_deplacer = False
        self.action_effectuer = False

    @property
    def nom(self): return self._nom

    @property
    def personnage(self): return self._personnage

    @nom.setter
    def nom(self, nom): self._nom = nom
    
    @personnage.setter
    def personnage(self, personnage): self._personnage = personnage
    
    def lancer_de(self, bouton):
        self.de_lancer = True
        resultat_de = randint(1,6)
        print(f"{self._nom} lance un dé et a fait {resultat_de} !")
        return resultat_de
    
    def choix_deplacement(self, choix_possible, plateau, position):
        time.sleep(1)
        self.personnage_deplacer = True
        return choice(choix_possible)

    def choix_action(self, bouton_attaque, bouton_capacite):
        time.sleep(1)
        self.action_effectuer = True
        return choice([1])

    def __repr__(self): return self._nom