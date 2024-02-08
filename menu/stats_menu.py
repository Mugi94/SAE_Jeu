from __future__ import annotations
from bouton import Bouton
import sys
import pygame

#Screen resolution
WIDTH, HEIGHT = 1280, 720



# -------------Menu stats------------

def stats_menu(screen, stats) -> None:
    "Menu statistiques globales du jeu acessible depuis le menu principal"
    
    background = pygame.image.load("img/menu_principal.jpg")
    title_font = pygame.font.Font("fonts/Democratica Bold.ttf", 75)
    text_font = pygame.font.SysFont("Helvetic", 50)
    
    run = True
    
    while run:
        # Positionnement de la souris
        stats_mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        # Remplir le fond
        screen.blit(background, (0, 0))

        # Titre menu
        game_title: pygame.Surface = title_font.render(
            "La Cité Academique", True, (255, 255, 255))
        game_title_rect: pygame.Rect = game_title.get_rect(
            center=(WIDTH//2, 100))
        screen.blit(game_title, game_title_rect)

        # -----------------------------------------------------------------------------------------
        stats_text: pygame.Surface = title_font.render("Menu statistiques", True, "black")
        stats_rect: pygame.Rect = stats_text.get_rect(center=(640, 260))
        screen.blit(stats_text, stats_rect)

        # Boutons
        stats_back = Bouton(None, (), 'Retour', text_font, 'black', 'white')
        stats_back.changeColor(stats_mouse_pos)
        stats_back.update(screen)
        # -----------------------------------------------------------------------------------------

        # Gestion de l'affichage des statistiques

        stats1_text: pygame.Surface = text_font.render(
            "Statistiques globales", True, "black")
        stats1_rect: pygame.Rect = stats1_text.get_rect(center=(640, 320))
        screen.blit(stats1_text, stats1_rect)

        score_text: pygame.Surface = text_font.render(
            f"Score: {stats['score']}", True, "black")
        score_rect: pygame.Rect = score_text.get_rect(center=(640, 380))
        screen.blit(score_text, score_rect)
        
        degats_moyens_text: pygame.Surface = text_font.render(
            f"Dégats moyens: {stats['degats_moyens']}", True, "black")
        degats_moyens_rect: pygame.Rect = degats_moyens_text.get_rect(center=(640, 440))
        screen.blit(degats_moyens_text, degats_moyens_rect)
        
        degats_totaux_text: pygame.Surface = text_font.render(
            f"Dégats totaux: {stats['degats_totaux']}", True, "black")
        degats_totaux_rect: pygame.Rect = degats_totaux_text.get_rect(center=(640, 500))
        screen.blit(degats_totaux_text, degats_totaux_rect)
        
        meilleur_personnage_text: pygame.Surface = text_font.render(
            f"Meilleur personnage: {stats['meilleur_personnage']}", True, "black")
        meilleur_personnage_rect: pygame.Rect = meilleur_personnage_text.get_rect(center=(640, 560))
        screen.blit(meilleur_personnage_text, meilleur_personnage_rect)
        
        pire_personnage_text: pygame.Surface = text_font.render(
            f"Pire personnage: {stats['pire_personnage']}", True, "black")
        pire_personnage_rect: pygame.Rect = pire_personnage_text.get_rect(center=(640, 620))
        screen.blit(pire_personnage_text, pire_personnage_rect)
        
        # -----------------------------------------------------------------------------------------
        

        # gestion des evenements
        for event in pygame.event.get():
            # Si on quitte, on quitte
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si on clique sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stats_back.checkForInput(stats_mouse_pos):
                    run = False

        # Met a jour la fenetre
        pygame.display.update()
