from __future__ import annotations
from bouton import Bouton
from menu.choix_personnage_menu import choix_personnage_menu
import pygame
import sys

import constants as const

def choix_partie_menu(screen, stats):
    menu_button = pygame.image.load(const.MENU_BUTTON)
    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 75)
    text_font = pygame.font.SysFont("Helvetic", 50)

    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        title = title_font.render("La Cité Academique", True, (255,255,255)) ; title_rect = title.get_rect(center=(const.WIDTH//2, 100))
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
                    choix_personnage_menu(screen, stats)
                    run = False

                if multi_button.checkForInput(mouse_pos):
                    print("Multijoueur")

                if back_button.checkForInput(mouse_pos):
                    run = False

        pygame.display.update()