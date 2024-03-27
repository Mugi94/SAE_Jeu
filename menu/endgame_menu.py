from __future__ import annotations
from bouton import Bouton
import pygame

import constants as const

def endgame_menu(screen, win):
    title_font = pygame.font.SysFont("Helvetic", 50)
    text_font = pygame.font.SysFont("Helvetic", 50)

    mouse_pos = pygame.mouse.get_pos()

    pause_surface = pygame.Surface((const.WIDTH, const.HEIGHT), pygame.SRCALPHA) ; pygame.draw.rect(pause_surface, (128, 128, 128, 150), [0, 0, const.WIDTH, const.HEIGHT])
    screen.blit(pause_surface, (0,0))
    
    if win:
        title = title_font.render("LES JOUEURS ONT GAGNES", True, (255, 255, 255)) ; title_rect = title.get_rect(center=(const.WIDTH//2, 250))
        screen.blit(title, title_rect)
    else:
        title = title_font.render("LES JOUEURS ONT PERDU", True, (255, 255, 255)) ; title_rect = title.get_rect(center=(const.WIDTH//2, 250))
        screen.blit(title, title_rect)
    
    quit_button = Bouton(None, (const.WIDTH//2, 450), "QUITTER", text_font, "black", "White") ; quit_button.changeColor(mouse_pos)
    quit_button.update(screen)
    
    retry_button = Bouton(None, (const.WIDTH//2, 350), "RECOMMENCER", text_font, "black", "White") ; retry_button.changeColor(mouse_pos)
    retry_button.update(screen)

    return quit_button, retry_button