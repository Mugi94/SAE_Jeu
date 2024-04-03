from __future__ import annotations
from bouton import Bouton
import pygame
import sys

from menu.stats_menu import stats_menu

import constants as const

def reglement(screen):
    width = screen.get_width()
    height = screen.get_height()

    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.SysFont("Helvetic", 75)
    text_font = pygame.font.SysFont("Helvetic", 50)

    title = title_font.render("Règlement", True, (0,0,0)) ; title_rect = title.get_rect(center=(const.WIDTH//2, 100))
    ligne1_texte = text_font.render("Jeu en tour par tour:", None, (0,0,0)) ; ligne1_rect = ligne1_texte.get_rect(topleft=(width*0.08, height*0.25))
    ligne2_texte = text_font.render("- Chaque joueur lance un dé et effectue une action", None, (0,0,0)) ; ligne2_rect = ligne2_texte.get_rect(topleft=(width*0.08, height*0.35))
    ligne3_texte = text_font.render("- Après que chaque joueur ait joué, l'ennemi attaque", None, (0,0,0)) ; ligne3_rect = ligne3_texte.get_rect(topleft=(width*0.08, height*0.45))
    ligne4_texte = text_font.render("- Des bonus sont appliqué au personnages selon la case où", None, (0,0,0)) ; ligne4_rect = ligne4_texte.get_rect(topleft=(width*0.08, height*0.55))
    ligne5_texte = text_font.render("ils se situent et à leurs affinité au lieu actuel", None, (0,0,0)) ; ligne5_rect = ligne5_texte.get_rect(topleft=(width*0.08, height*0.6))
    ligne6_texte = text_font.render("- Le but est de faire régner la paix dans la cité en éliminant", None, (0,0,0)) ; ligne6_rect = ligne6_texte.get_rect(topleft=(width*0.08, height*0.7))
    ligne7_texte = text_font.render("tous les ennemis sans vous faire battre", None, (0,0,0)) ; ligne7_rect = ligne7_texte.get_rect(topleft=(width*0.08, height*0.75))
    
    run = True
    while run:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, "black", pygame.Rect((width*0.05, height*0.05), (width*0.90, height*0.90)))
        pygame.draw.rect(screen, "lightgray", pygame.Rect((width*0.05 + 7.5, height*0.05 + 7.5), (width*0.90 - 15, height*0.90 - 15)))

        screen.blit(title, title_rect)
        screen.blit(ligne1_texte, ligne1_rect)
        screen.blit(ligne2_texte, ligne2_rect)
        screen.blit(ligne3_texte, ligne3_rect)
        screen.blit(ligne4_texte, ligne4_rect)
        screen.blit(ligne5_texte, ligne5_rect)
        screen.blit(ligne6_texte, ligne6_rect)
        screen.blit(ligne7_texte, ligne7_rect)

        bouton_retour = Bouton(None, (640, 620), "Retour", text_font, "black", "White")
        bouton_retour.changeColor(mouse_pos) ; bouton_retour.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_retour.checkForInput(mouse_pos):
                    run = False

        pygame.display.update()

def extra_menu(screen, stats):
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

        bouton_regles = Bouton(menu_button, (640, 250), "REGLES", text_font, "black", "White")
        bouton_stats = Bouton(menu_button, (640, 400), "STATISTIQUES", text_font, "black", "White")
        bouton_retour = Bouton(menu_button, (640, 550), "RETOUR", text_font, "black", "White")
        for button in [bouton_regles, bouton_stats, bouton_retour]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_regles.checkForInput(mouse_pos):
                    reglement(screen)
                
                if bouton_stats.checkForInput(mouse_pos):
                    stats_menu(screen, stats)
                
                if bouton_retour.checkForInput(mouse_pos):
                    run = False

        pygame.display.update()