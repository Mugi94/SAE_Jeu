from __future__ import annotations
from bouton import Bouton
import pygame
import sys
from stats import Stats
import os
import constants as const

from menu.extra_menu import extra_menu
from menu.choix_partie_menu import choix_partie_menu

stats = Stats()

def main_menu(screen):
    menu_button = pygame.image.load(const.MENU_BUTTON)
    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 105)
    text_font = pygame.font.SysFont("Helvetic", 50)

    taille_bordure = 2

    if os.path.exists("stats.json"):
        stats.importStats("stats.json")

    while True:

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

        play_button = Bouton(menu_button, (640, 250), "JOUER", text_font, "black", "White")
        extra_button = Bouton(menu_button, (640, 400), "EXTRA", text_font, "black", "White")
        quit_button = Bouton(menu_button, (640, 550), "QUITTER", text_font, "black", "White")

        for button in [play_button, extra_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    choix_partie_menu(screen, stats)

                if extra_button.checkForInput(mouse_pos):
                    extra_menu(screen, stats)

                if quit_button.checkForInput(mouse_pos):
                    stats.exportStats()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()