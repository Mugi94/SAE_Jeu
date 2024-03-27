from __future__ import annotations
from bouton import Bouton
from personnage import *
from menu.lancement_partie_menu import lancement_partie_menu
import pygame
import sys

import constants as const

def previous(indice, personnages):
    indice -= 1
    if indice < 0:
        indice = len(personnages) - 1
    return indice

def next(indice, personnages):
    indice += 1
    if indice >= len(personnages):
        indice = 0
    return indice

def choix_personnage_menu(screen, stats):
    background = pygame.image.load(const.MENU_PERSONNAGE)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 75)
    text_font = pygame.font.SysFont("Helvetic", 50)
    character_name_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 65)
    character_info_font = pygame.font.SysFont("Helvetic", 40)
    
    next_img = pygame.image.load(const.BOUTON_SUIVANT)
    previous_img = pygame.image.load(const.BOUTON_PRECEDENT)

    personnage_disponible = [
        Aurore(),
        Akane(),
        Laura(),
        Bob(),
        William(),
        Erika(),
        AgentF(),
        AgentK(),
        Eliza()
    ]

    indice_choix = 0

    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        title = title_font.render("Choississez un personnage", True, (255,255,255)) ; title_rect = title.get_rect(center=(const.WIDTH*0.5, const.HEIGHT*0.14))
        screen.blit(title, title_rect)

        personnage_choisi = personnage_disponible[indice_choix]


        # Infos personnage
        # Nom
        character_name = character_name_font.render(f"{personnage_choisi}", True, (255,255,255)) ; character_name_rect = character_name.get_rect(center=(const.WIDTH*0.6, const.HEIGHT*0.25))
        screen.blit(character_name, character_name_rect)

        # Carte
        character_image = pygame.image.load(personnage_choisi.images['carte'])
        character_image = pygame.transform.scale(character_image, (character_image.get_width() * 1.15, character_image.get_height() * 1.15))
        screen.blit(character_image, (const.WIDTH*0.12, const.HEIGHT*0.35))

        # Attaque et défense
        character_stat = character_info_font.render(f"Attaque = {personnage_choisi.ATK} | Défense = {personnage_choisi.DEF}", True, (255,255,255)) ; character_stat_rect = character_stat.get_rect(center=(const.WIDTH*0.6, const.HEIGHT*0.4))
        screen.blit(character_stat, character_stat_rect)
        
        # Capacité
        capacite_name = character_info_font.render(f"Capacité = ???", True, (255,255,255)) ; capacite_name_rect = capacite_name.get_rect(center=(const.WIDTH*0.6, const.HEIGHT*0.5))
        screen.blit(capacite_name, capacite_name_rect)
        
        capacite_info = character_info_font.render(f"Informations de la capacité", True, (255,255,255)) ; capacite_info_rect = capacite_info.get_rect(center=(const.WIDTH*0.6, const.HEIGHT*0.55))
        screen.blit(capacite_info, capacite_info_rect)
        
        # Affinité
        for stage, lieu in const.STAGES.items():

            lieu_img = pygame.image.load(lieu)
            lieu_img = pygame.transform.scale(lieu_img, (lieu_img.get_width() * 0.15, lieu_img.get_height() * 0.15))
            screen.blit(lieu_img, (stage*lieu_img.get_width() + 195, const.HEIGHT*0.65))
            
            if stage in personnage_choisi.affinite["haute"]:
                affinite_img = pygame.image.load(const.LIEU_CONTENT)
            elif stage in personnage_choisi.affinite["faible"]:
                affinite_img = pygame.image.load(const.LIEU_PAS_CONTENT)
            else:
                affinite_img = pygame.image.load(const.LIEU_NEUTRE)
            screen.blit(affinite_img, (stage*lieu_img.get_width() + 285, const.HEIGHT*0.81))

        confirm_button = Bouton(None, (const.WIDTH*0.5, const.HEIGHT*0.9), "Confirmer", text_font, "white", "black")
        previous_button = Bouton(previous_img, (const.WIDTH*0.04, const.HEIGHT*0.5), "", text_font, "white", "white")
        next_button = Bouton(next_img, (const.WIDTH-50, const.HEIGHT*0.5), "", text_font, "white", "white")

        for button in [confirm_button, previous_button, next_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if previous_button.checkForInput(mouse_pos):
                    indice_choix = previous(indice_choix, personnage_disponible)

                if next_button.checkForInput(mouse_pos):
                    indice_choix = next(indice_choix, personnage_disponible)

                if confirm_button.checkForInput(mouse_pos):
                    print(f"Personnage choisi = {personnage_choisi}")
                    lancement_partie_menu(screen, personnage_choisi, personnage_disponible, stats)
                    run = False

        pygame.display.update()