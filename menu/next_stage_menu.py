from __future__ import annotations
from bouton import Bouton
import pygame

import constants as const

def next_stage_menu(screen):
    title_font = pygame.font.SysFont("Helvetic", 50)
    text_font = pygame.font.SysFont("Helvetic", 50)
    
    mouse_pos = pygame.mouse.get_pos()
    
    pause_surface = pygame.Surface((const.WIDTH, const.HEIGHT), pygame.SRCALPHA) ; pygame.draw.rect(pause_surface, (128, 128, 128, 150), [0, 0, const.WIDTH, const.HEIGHT])
    screen.blit(pause_surface, (0,0))

    title = title_font.render("Boss vaincu", True, (255, 255, 255)) ; title_rect = title.get_rect(center=(const.WIDTH//2, 250))
    screen.blit(title, title_rect)

    quit_button = Bouton(None, (const.WIDTH//2, 450), "QUITTER", text_font, "black", "White") ; quit_button.changeColor(mouse_pos)
    quit_button.update(screen)
    
    back_button = Bouton(None, (const.WIDTH//2, 350), "SUIVANT", text_font, "black", "White") ; back_button.changeColor(mouse_pos)
    back_button.update(screen)

    return quit_button, back_button