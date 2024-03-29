from __future__ import annotations
from bouton import Bouton
from menu.choix_personnage_menu import choix_personnage_menu
import pygame
import sys

import constants as const


def choix_nombre_joueurs(screen, stats):
    width = screen.get_width()
    height = screen.get_height()

    menu_button = pygame.image.load(const.MENU_BUTTON)
    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 105)
    text_font = pygame.font.SysFont("Helvetic", 50)

    taille_bordure = 2

    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0,0))

        title_bord = title_font.render("La Cité Academique", True, (255, 255, 255))
        title = title_font.render("La Cité Academique", True, (239, 114, 52)) # (10, 170, 225)

        title_bord_rect = title_bord.get_rect(center=(const.WIDTH//2, 100))
        title_rect = title.get_rect(center=(const.WIDTH//2, 100))
        
        for x_offset in range(-taille_bordure, taille_bordure + 1):
            for y_offset in range(-taille_bordure, taille_bordure + 1):
                screen.blit(title_bord, (title_bord_rect.x + x_offset, title_bord_rect.y + y_offset))
        
        screen.blit(title, title_rect)

        choix_2_joueurs = Bouton(menu_button, (width*0.5, 250), "2 JOUEURS", text_font, "black", "White")
        choix_3_joueurs = Bouton(menu_button, (width*0.5, 400), "3 JOUEURS", text_font, "black", "White")
        choix_4_joueurs = Bouton(menu_button, (width*0.5, 550), "4 JOUEURS", text_font, "black", "White")
        for button in [choix_2_joueurs, choix_3_joueurs, choix_4_joueurs]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if choix_2_joueurs.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 2, stats)
                    run = False

                if choix_3_joueurs.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 3, stats)
                    run = False

                if choix_4_joueurs.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 4, stats)
                    run = False

        pygame.display.update()


def choix_partie_menu(screen, stats):
    menu_button = pygame.image.load(const.MENU_BUTTON)
    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 105)
    text_font = pygame.font.SysFont("Helvetic", 50)

    taille_bordure = 2

    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        title_bord = title_font.render("La Cité Academique", True, (255, 255, 255))
        title = title_font.render("La Cité Academique", True, (239, 114, 52)) # (10, 170, 225)

        title_bord_rect = title_bord.get_rect(center=(const.WIDTH//2, 100))
        title_rect = title.get_rect(center=(const.WIDTH//2, 100))
        
        for x_offset in range(-taille_bordure, taille_bordure + 1):
            for y_offset in range(-taille_bordure, taille_bordure + 1):
                screen.blit(title_bord, (title_bord_rect.x + x_offset, title_bord_rect.y + y_offset))
        
        screen.blit(title, title_rect)

        solo_button = Bouton(menu_button, (640, 250), "SOLO", text_font, "black", "White")
        multi_button = Bouton(menu_button, (640, 400), "MULTIJOUEUR", text_font, "black", "White")
        back_button = Bouton(menu_button, (640, 550), "RETOUR", text_font, "black", "White")
        for button in [solo_button, multi_button, back_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo_button.checkForInput(mouse_pos):
                    choix_personnage_menu(screen, 1, stats)
                    run = False

                if multi_button.checkForInput(mouse_pos):
                    choix_nombre_joueurs(screen, stats)
                    run = False

                if back_button.checkForInput(mouse_pos):
                    run = False

        pygame.display.update()