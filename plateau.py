from __future__ import annotations
from random import choice, randrange
from personnage import *
from pygame.image import load
from pygame import Rect
import os

import constants as const

class Case:
    def __init__(self, type_case = "neutre"):
        self._type = type_case
        self._personnages = []
        self._image = f"{const.PATH}/img/cases/case_{type_case}.png"


    # ------------ Getters/setters ------------
    @property
    def type(self): return self._type

    @property
    def personnages(self): return self._personnages

    @property
    def image(self): return self._image
    
    @type.setter
    def type(self, type):
        self._type = type
        self._image = f"{const.PATH}/img/cases/case_{type}.png"
    # -----------------------------------------

    def placePersonnage(self, personnage):
        self._personnages.append(personnage)

    def enlevePersonnage(self, personnage):
        self._personnages.remove(personnage)

    def __repr__(self): return f'{self._type} = {self._personnages}'


class Plateau:
    TAILLE = 16

    def __init__(self, personnages, nb_bonus = 3, nb_malus = 3):
        self._cases = [Case() for _ in range (Plateau.TAILLE)]
        self.ajoutBonus(nb_bonus, nb_malus)
        self._zone_cliquable = {}
        
        for i in range(int(Plateau.TAILLE/4)):
            self._zone_cliquable[i+1] = Rect(((i*144) + 280, 0), (144,144))
            
        for j in range(int(Plateau.TAILLE/4)):
            self._zone_cliquable[int(Plateau.TAILLE/4) + j + 1] = Rect((856, (j*144)), (144,144))
            
        for k in reversed(range(int(Plateau.TAILLE/4))):
            self._zone_cliquable[2 * int(Plateau.TAILLE/4) + k + 1] = Rect(((int(Plateau.TAILLE/4 - k-1)*144) + 424, 576), (144,144))
            
        for l in reversed(range(int(Plateau.TAILLE/4))):
            self._zone_cliquable[3 * int(Plateau.TAILLE/4) + l + 1] = Rect((280, (int(Plateau.TAILLE/4 - l-1)*144) + 144), (144,144))
        
        position_init = [1, 5, 9, 13]
        
        for index, personnage in enumerate(personnages):
            self.ajouter_personnage(personnage, position_init[index])
            print(f"Ajout de {personnage} à la case {position_init[index]}")

    @property
    def personnages(self):
        liste = []
        for case in self._cases:
            liste.extend(case.personnages)
        return liste
    
    @property
    def zone_cliquable(self): return self._zone_cliquable

    def case(self, position):
        return self._cases[position - 1]

    def personnages_case(self, position):
        return self._cases[position - 1].personnages

    def ajoutBonus(self, bonus, malus):
        maxBonus = bonus
        maxMalus = malus

        while (maxBonus + maxMalus) > 0:
            indice = randrange(Plateau.TAILLE)

            if self._cases[indice].type == 'neutre':
                caseAlea = Case(choice(["bonus", "malus"]))

                if caseAlea.type == "bonus" and (maxBonus > 0):
                    self._cases[indice] = caseAlea
                    maxBonus = maxBonus - 1

                elif (maxMalus > 0) and caseAlea.type == "malus":
                    self._cases[indice] = caseAlea
                    maxMalus = maxMalus - 1

    def ajouter_personnage(self, personnage, position):
        position = position % Plateau.TAILLE
        self._cases[position - 1].personnages.append(personnage)
        personnage.position = position


    def deplacer_personnage(self, personnage, nombre_cases):
        self.case(personnage.position).personnages.remove(personnage)

        if(personnage.position + nombre_cases) % Plateau.TAILLE == 0:
            self.ajouter_personnage(personnage, Plateau.TAILLE)
        else:
            self.ajouter_personnage(personnage, (personnage.position + nombre_cases) % Plateau.TAILLE)

        print(f"{personnage} s'est deplacé(e) de {nombre_cases} case(s)")

    def draw(self, screen):
        taille_case = load(self.case(1).image).get_width()

        for i in range(int(Plateau.TAILLE/4)):
            affichage_case = load(self.case(i+1).image)
            case_position = ((i*taille_case) + 280, 0)
            screen.blit(affichage_case, case_position)

            personnages = self.case(i+1).personnages
            if len(personnages) == 1:
                position = (((i*144) + (280 + 144/4), 144/4))
                screen.blit(load(personnages[0].images['icone']), position)

            elif len(personnages) == 2:
                positions = [
                    ((i*144) + 285, 144/4),
                    ((i*144) + (280 + 144/2), 144/4)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])
   
            elif len(personnages) == 3:
                positions = [
                    ((i*144) + (280 + 144/4), 5),
                    ((i*144) + 285, 144/2),
                    ((i*144) + (280 + 144/2), 144/2)
                ]                
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

            elif len(personnages) == 4:
                positions = [
                    ((i*144) + 285, 5),
                    ((i*144) + (280 + 144/2), 5),
                    ((i*144) + 285, 144/2),
                    ((i*144) + (280 + 144/2), 144/2)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])


        for j in range(int(Plateau.TAILLE/4)):
            affichage_case = load(self.case(j+5).image)
            case_position = (856, (j*taille_case))
            screen.blit(affichage_case, case_position)

            personnages = self.case(j+5).personnages
            if len(personnages) == 1:
                position = ((861 + 144/4, (j*144) + 144/4))
                screen.blit(load(personnages[0].images['icone']), position)

            elif len(personnages) == 2:
                positions = [
                    (861, (j*144) + 144/4),
                    (861 + 144/2, (j*144) + 144/4)
                ]                
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

            elif len(personnages) == 3:
                positions = [
                    (861 + 144/4, (j*144) + 5),
                    (861, (j*144) + 144/2),
                    (861 + 144/2, (j*144) + 144/2)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

            elif len(personnages) == 4:
                positions = [
                    (861, (j*144) + 5),
                    (861 + 144/2, (j*144) + 5),
                    (861, (j*144) + 144/2 + 5),
                    (861 + 144/2, (j*144) + 144/2 + 5)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])


        for k in reversed(range(int(Plateau.TAILLE/4))):
            case_position = (((Plateau.TAILLE/4 - k-1)*144) + 424, 576)
            affichage_case = load(self.case(k+9).image)
            screen.blit(affichage_case, case_position)

            personnages = self.case(k+9).personnages
            if len(personnages) == 1:
                position = (((Plateau.TAILLE/4 - k-1)*144) + 429 + 144/4, 581 + 144/4)
                screen.blit(load(personnages[0].images['icone']), position)

            elif len(personnages) == 2:
                positions = [
                    (((Plateau.TAILLE/4 - k-1)*144) + 429, 581 + 144/4),
                    (((Plateau.TAILLE/4 - k-1)*144) + 429 + 144/2, 581 + 144/4)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

            elif len(personnages) == 3:
                positions = [
                    (((Plateau.TAILLE/4 - k-1)*144) + 429 + 144/4, 581),
                    (((Plateau.TAILLE/4 - k-1)*144) + 429, 581 + 144/2),
                    (((Plateau.TAILLE/4 - k-1)*144) + 429 + 144/2, 581 + 144/2)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

            elif len(personnages) == 4:
                positions = [
                    (((Plateau.TAILLE/4 - k-1)*144) + 429, 581),
                    (((Plateau.TAILLE/4 - k-1)*144) + 429 + 144/2, 581),
                    (((Plateau.TAILLE/4 - k-1)*144) + 429, 581 + 144/2),
                    (((Plateau.TAILLE/4 - k-1)*144) + 429 + 144/2, 651)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])


        for l in reversed(range(int(Plateau.TAILLE/4))):
            case_position = (280, ((Plateau.TAILLE/4 - l-1)*144) + 144)
            affichage_case = load(self.case(l+13).image)
            screen.blit(affichage_case, case_position)

            personnages = self.case(l+13).personnages
            if len(personnages) == 1:
                position = (285 + 144/4, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5 + 144/4)
                screen.blit(load(personnages[0].images['icone']), position)
            
            elif len(personnages) == 2:
                positions = [
                    (285, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5 + 144/4),
                    (285 + 144/2, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5 + 144/4)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

            elif len(personnages) == 3:
                positions = [
                    (285 + 144/4, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5),
                    (285, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5 + 144/2),
                    (285 + 144/2, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5 + 144/2)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

            elif len(personnages) == 4:
                positions = [
                    (285, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5),
                    (285 + 144/2, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5),
                    (285, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5 + 144/2),
                    (285 + 144/2, ((Plateau.TAILLE/4 - l-1)*144) + 144 + 5 + 144/2)
                ]
                for index, personnage in enumerate(personnages):
                    screen.blit(load(personnage.images['icone']), positions[index])

    def __repr__(self):
        rep = ""
        for index, case in enumerate(self._cases):
            rep += f"Case n°{index + 1}: {case}\n"
        return rep