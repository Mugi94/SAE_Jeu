from __future__ import annotations
from bouton import Bouton
from joueur import Joueur
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


def choix_personnage_menu(screen, nombre_joueurs, stats):
    width = screen.get_width()
    height = screen.get_height()

    background = pygame.image.load(const.MENU_PERSONNAGE)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 75)
    text_font = pygame.font.SysFont("Helvetic", 50)
    input_font = pygame.font.SysFont("Helvetic", 40)
    character_name_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 65)
    character_info_font = pygame.font.SysFont("Helvetic", 40)

    next_img = pygame.image.load(const.BOUTON_SUIVANT)
    previous_img = pygame.image.load(const.BOUTON_PRECEDENT)

    text_box = pygame.Rect(155, 200, 184, 32)

    tab_joueurs = []
    joueur_actuel_index = 0
    input_joueur = ''
    input_actif = False

    indice_choix = 0
    personnages_disponible = [
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
    
    personnages_pris = []

    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        personnage = personnages_disponible[indice_choix]

        title = title_font.render(f"Choisissez un personnage", True, (255,255,255)) ; title_rect = title.get_rect(center=(width*0.5, height*0.14))
        screen.blit(title, title_rect)

        # ---- Nom du joueur ----
        if input_actif:
            pygame.draw.rect(screen, (255, 255, 255), text_box, 2)
        else:
            pygame.draw.rect(screen, (144, 144, 144), text_box, 2)

        input_nom_joueur = input_font.render(f"Saisissez votre nom : ", True, (255,255,255)) ; input_rect = input_nom_joueur.get_rect(center=(width*0.15, height*0.25))
        screen.blit(input_nom_joueur, input_rect)
        
        nom_joueur = input_font.render(input_joueur, True, (255,255,255))
        screen.blit(nom_joueur, (text_box.x + 4, text_box.y + 3))
        
        text_box.w = max(185, nom_joueur.get_width() + 10)

        # ---- Infos personnage ----
        # -- Nom
        character_name = character_name_font.render(f"{personnage}", True, (255,255,255)) ; character_name_rect = character_name.get_rect(center=(width*0.6, height*0.25))
        screen.blit(character_name, character_name_rect)

        # -- Carte
        if personnage not in personnages_pris:
            character_image = pygame.image.load(personnage.images['carte'])
        else:
            character_image = pygame.image.load(personnage.images['carte_grise'])
        character_image = pygame.transform.scale(character_image, (character_image.get_width() * 1.15, character_image.get_height() * 1.15))
        screen.blit(character_image, (width*0.12, height*0.35))

        # -- Attaque et défense
        character_stat = character_info_font.render(f"Attaque = {personnage.ATK} | Défense = {personnage.DEF}", True, (255,255,255)) ; character_stat_rect = character_stat.get_rect(center=(width*0.6, height*0.4))
        screen.blit(character_stat, character_stat_rect)
        
        # -- Capacité
        capacite_name = character_info_font.render(f"Capacité = {personnage.capacite['nom']}", True, (255,255,255)) ; capacite_name_rect = capacite_name.get_rect(center=(width*0.6, height*0.5))
        screen.blit(capacite_name, capacite_name_rect)
        
        capacite_info = character_info_font.render(f"{personnage.capacite['description']}", True, (255,255,255)) ; capacite_info_rect = capacite_info.get_rect(center=(width*0.6, height*0.55))
        screen.blit(capacite_info, capacite_info_rect)

        # -- Affinité
        for stage, lieu in const.STAGES.items():
            lieu_img = pygame.image.load(lieu)
            lieu_img = pygame.transform.scale(lieu_img, (lieu_img.get_width() * 0.15, lieu_img.get_height() * 0.15))
            screen.blit(lieu_img, (stage*lieu_img.get_width() + 195, height*0.65))
            
            if stage in personnage.affinite["haute"]:
                affinite_img = pygame.image.load(const.LIEU_CONTENT)
            elif stage in personnage.affinite["faible"]:
                affinite_img = pygame.image.load(const.LIEU_PAS_CONTENT)
            else:
                affinite_img = pygame.image.load(const.LIEU_NEUTRE)
            screen.blit(affinite_img, (stage*lieu_img.get_width() + 285, height*0.81))

        # ---- Boutons ----
        confirm_button = Bouton(None, (width*0.5, height*0.9), "Confirmer", text_font, "white", "black")
        previous_button = Bouton(previous_img, (width*0.04, height*0.5), "", text_font, "white", "white")
        next_button = Bouton(next_img, (width-50, height*0.5), "", text_font, "white", "white")

        for button in [confirm_button, previous_button, next_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        # ---- Evenements ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if previous_button.checkForInput(mouse_pos):
                    indice_choix = previous(indice_choix, personnages_disponible)

                if next_button.checkForInput(mouse_pos):
                    indice_choix = next(indice_choix, personnages_disponible)

                if confirm_button.checkForInput(mouse_pos):
                    if input_joueur != '' and personnage not in personnages_pris:
                        if joueur_actuel_index == nombre_joueurs-1:
                            tab_joueurs.append(Joueur(personnage, input_joueur))
                            lancement_partie_menu(screen, tab_joueurs, personnages_disponible, stats)
                            run = False
                        else:
                            personnages_pris.append(personnage)
                            tab_joueurs.append(Joueur(personnage, input_joueur))
                            input_joueur = ''
                            indice_choix = 0
                            joueur_actuel_index += 1
                
                if text_box.collidepoint(mouse_pos):
                    input_actif = True
                else:
                    input_actif = False
            
            # - Saisie du nom
            if event.type == pygame.KEYDOWN:
                if input_actif:
                    if event.key == pygame.K_BACKSPACE:
                        input_joueur = input_joueur[:-1]
                    else:
                        input_joueur += event.unicode

        pygame.display.update()