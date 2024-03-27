from __future__ import annotations
from menu.main_menu import main_menu
import constants as const
import pygame

if __name__ == "__main__":
    # Initialization of pygame
    pygame.init()

    # Creating the game screen
    screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
    pygame.display.set_caption("La cité academique")

    # Launching the game
    main_menu(screen)

    # Close pygame
    pygame.quit()

