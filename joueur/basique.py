from random import randint, choice
from joueur import Joueur
import pygame

class Basique(Joueur):
    def __init__(self, personnage):
        if personnage is not None:
            self._nom = personnage.nom
        else:
            self._nom = "Basique"
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
        
        cases_bonus = []
        cases_malus = []
        cases_neutre = []
        
        # Récupérer les cases possibles
        for choix in choix_possible:
            indice = (choix + position) % 16
            if indice == 0:
                indice = 16

            # Ajouter le choix que le joueur doit faire pour arriver a la case voulu
            if plateau.case(indice).type == 'bonus':
                cases_bonus.append(choix)

            elif plateau.case(indice).type == 'malus':
                cases_malus.append(choix)
            
            else:
                cases_neutre.append(choix)
        

        # Choisir les cases vers ou se déplacer selon ce qu'on a
        if cases_bonus != []:
            choix_joueur = choice(cases_bonus)
        
        elif cases_neutre != []:
            choix_joueur = choice(cases_neutre)
        
        else:
            choix_joueur = choice(cases_malus)

        self.personnage_deplacer = True
        return choix_joueur

    def choix_action(self, bouton_attaque, bouton_capacite):
        pygame.time.wait(1000)
        self.action_effectuer = True
        return choice([1,2])
    
    def choix_capacite(self, plateau, personnages):
        pygame.time.wait(1000)
        liste_personnages = list(personnages.keys())
        
        if self.personnage.capacite['nom'] == 'Healing Touch':
            choix = liste_personnages[0]
            for personnage in liste_personnages:
                if personnage.PV < choix.PV:
                    choix = personnage
            return choix

        if self.personnage.capacite['nom'] == 'Heaven Canceller':
            liste_choix = []
            for personnage in liste_personnages:
                if personnage.PV == 0:
                    liste_choix.append(personnage)
            return choice(liste_choix)

        return choice(list(personnages.keys()))