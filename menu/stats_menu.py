from __future__ import annotations
from bouton import Bouton
import sys
import pygame
import constants as const

# Screen resolution
WIDTH, HEIGHT = 1280, 720


def transparent_surface(screen: pygame.Surface):
    # Carré transparent pour la visibilité des statistiques

    # Créez une nouvelle surface de la taille du carré
    square = pygame.Surface((WIDTH, HEIGHT))

    # Remplissez la surface avec la couleur grise
    square.fill((131, 131, 131))

    # Définissez le niveau d'opacité (alpha) de la surface
    # Notez que 0 est complètement transparent et 255 est complètement opaque
    square.set_alpha(128)

    # Dessinez la surface sur tout l'écran
    screen.blit(square, (0, 0))

    return square


# -------------Menu stats------------

def stats_menu(screen, stats) -> None:
    "Menu statistiques globales du jeu acessible depuis le menu principal"

    background = pygame.image.load(const.MENU_BG)
    title_font = pygame.font.SysFont("Helvetic", 75)
    text_font = pygame.font.SysFont("Helvetic", 50)

    run = True

    while run:
        # Positionnement de la souris
        stats_mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        # Remplir le fond
        screen.blit(background, (0, 0))

        transparent_surface(screen)

        # Titre menu
        game_title: pygame.Surface = title_font.render(
            "La Cité Academique", True, "black")
        game_title_rect: pygame.Rect = game_title.get_rect(
            center=(WIDTH//2, 100))
        screen.blit(game_title, game_title_rect)

        # -----------------------------------------------------------------------------------------
        stats_text: pygame.Surface = title_font.render(
            "Menu statistiques", True, "black")
        stats_rect: pygame.Rect = stats_text.get_rect(center=(640, 200))
        screen.blit(stats_text, stats_rect)

        # Boutons
        stats_back = Bouton(None, (640, 650), 'Retour',
                            text_font, 'black', 'white')
        stats_back.changeColor(stats_mouse_pos)
        stats_back.update(screen)
        
        stats_reset = Bouton(None, (1050, 650), 'Réinitialiser',
                            text_font, 'black', 'white')
        stats_reset.changeColor(stats_mouse_pos)
        stats_reset.update(screen)
        
        # -----------------------------------------------------------------------------------------

        # Gestion de l'affichage des statistiques

        score_text: pygame.Surface = text_font.render(
            ("Score :" + str(stats.getStats()['score'])), True, "black")
        score_rect: pygame.Rect = score_text.get_rect(center=(640, 320))
        screen.blit(score_text, score_rect)

        degats_moyens_text: pygame.Surface = text_font.render(
            ("Dégats moyens :" + str(stats.getStats()['degats_moyens'])), True, "black")
        degats_moyens_rect: pygame.Rect = degats_moyens_text.get_rect(
            center=(640, 380))
        screen.blit(degats_moyens_text, degats_moyens_rect)

        degats_totaux_text: pygame.Surface = text_font.render(
            ("Dégats totaux :" + str(stats.getStats()['degats_totaux'])), True, "black")
        degats_totaux_rect: pygame.Rect = degats_totaux_text.get_rect(
            center=(640, 440))
        screen.blit(degats_totaux_text, degats_totaux_rect)

        meilleur_personnage_text: pygame.Surface = text_font.render(
            ("Meilleur personnage :" + str(stats.getStats()['meilleur_personnage'])), True, "black")
        meilleur_personnage_rect: pygame.Rect = meilleur_personnage_text.get_rect(
            center=(640, 500))
        screen.blit(meilleur_personnage_text, meilleur_personnage_rect)

        pire_personnage_text: pygame.Surface = text_font.render(
            ("Pire personnage :" + str(stats.getStats()['pire_personnage'])), True, "black")
        pire_personnage_rect: pygame.Rect = pire_personnage_text.get_rect(
            center=(640, 560))
        screen.blit(pire_personnage_text, pire_personnage_rect)

        # -----------------------------------------------------------------------------------------
        
        
        
        
        
        # -----------------------------------------------------------------------------------------

        # gestion des evenements
        for event in pygame.event.get():
            # Si on quitte, on quitte
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si on clique sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stats_reset.checkForInput(stats_mouse_pos):
                    stats.resetStats()
                    run = False
                if stats_back.checkForInput(stats_mouse_pos):
                    run = False


        # Met a jour la fenetre
        pygame.display.update()
