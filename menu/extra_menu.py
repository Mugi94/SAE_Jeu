from __future__ import annotations
from bouton import Bouton
import pygame
import sys

import constants as const


def extra_menu(screen):
    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 75)
    text_font = pygame.font.SysFont("Helvetic", 50)
    
    run = True
    while run:
        
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        
        title = title_font.render("La Cité Academique", True, (255,255,255)) ; title_rect = title.get_rect(center=(const.WIDTH//2, 100))
        screen.blit(title, title_rect)

        text = text_font.render("Menu extra", True, "black") ; text_rect = text.get_rect(center=(640, 260))
        screen.blit(text, text_rect)

        button_back = Bouton(None, (640, 460), 'Retour', text_font, 'black', 'white') ; button_back.changeColor(mouse_pos)
        button_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.checkForInput(mouse_pos):
                    run = False

        pygame.display.update()