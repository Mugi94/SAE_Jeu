from __future__ import annotations
import pygame
import constants as const

def affinite(personnage, etape):
    affinite = const.LIEU_NEUTRE
    
    if personnage.affinite['haute'] == etape:
        affinite = const.LIEU_CONTENT
    
    if personnage.affinite['basse'] == etape:
        affinite = const.LIEU_PAS_CONTENT

    return pygame.image.load(affinite)


def afficher_cartes(screen, characters):
    width = screen.get_width()
    height = screen.get_height()
    
    zones_cliquable = {}
    
    game_font = pygame.font.SysFont("Helvetic", 30)

    if len(characters) > 0:
        personnage = characters[0]
        carte = pygame.image.load(personnage.images['carte'])
        carte_width = carte.get_width()
        carte_height = carte.get_height()
        screen.blit(carte, (0, 0))
        zones_cliquable[personnage] = pygame.Rect((0, 0), (carte_width, carte_height))

        pourcentage_pv = min((personnage.PV / personnage.PV_max), 1.0)
        taille_barre_vie = int(pourcentage_pv * carte_width)
        pygame.draw.rect(screen, "red", (0, 265, (personnage.PV_max * carte_width) / 100, 25))
        pygame.draw.rect(screen, "green", (0, 265, taille_barre_vie, 25))
        infos_pv = game_font.render(f'{personnage.PV}/{personnage.PV_max}', True, (0, 0, 0))
        screen.blit(infos_pv, infos_pv.get_rect(center=(50, 280)))

        if len(characters) > 1:
            personnage = characters[1]
            carte = pygame.image.load(personnage.images['carte'])
            carte_width = carte.get_width()
            carte_height = carte.get_height()
            screen.blit(carte, (width-carte_width, 0))
            zones_cliquable[personnage] = pygame.Rect((width-carte_width, 0), (carte_width, carte_height))
            
            pourcentage_pv = min((personnage.PV / personnage.PV_max), 1.0)
            taille_barre_vie = int(pourcentage_pv * carte_width)
            pygame.draw.rect(screen, "red", (width-carte_width, 265, (personnage.PV_max * carte_width) / 100, 25))
            pygame.draw.rect(screen, "green", (width-carte_width, 265, taille_barre_vie, 25))
            infos_pv = game_font.render(f'{personnage.PV}/{personnage.PV_max}', True, (0, 0, 0))
            screen.blit(infos_pv, infos_pv.get_rect(center=(width*0.91, 280)))

            if len(characters) > 2:
                personnage = characters[2]
                carte = pygame.image.load(personnage.images['carte'])
                carte_width = carte.get_width()
                carte_height = carte.get_height()
                screen.blit(carte, (width-carte_width, height-(carte_height+25)))
                zones_cliquable[personnage] = pygame.Rect((width-carte_width, height-(carte_height+25)), (carte_width, carte_height))
                
                pourcentage_pv = min((personnage.PV / personnage.PV_max), 1.0)
                taille_barre_vie = int(pourcentage_pv * carte_width)
                pygame.draw.rect(screen, "red", (width-carte_width, height*0.966, (personnage.PV_max * carte_width) / 100, 25))
                pygame.draw.rect(screen, "green", (width-carte_width, height*0.966, taille_barre_vie, 25))
                infos_pv = game_font.render(f'{personnage.PV}/{personnage.PV_max}', True, (0, 0, 0))
                screen.blit(infos_pv, infos_pv.get_rect(center=(width*0.91, height*0.985)))

                if len(characters) > 3:
                    personnage = characters[3]
                    carte = pygame.image.load(personnage.images['carte'])
                    carte_width = carte.get_width()
                    carte_height = carte.get_height()
                    screen.blit(carte, (0, height- (carte_height+25)))
                    zones_cliquable[personnage] = pygame.Rect((0, height-(carte_height+25)), (carte_width, carte_height))

                    pourcentage_pv = min((personnage.PV / personnage.PV_max), 1.0)
                    taille_barre_vie = int(pourcentage_pv * carte_width)
                    pygame.draw.rect(screen, "red", (0, height*0.966, (personnage.PV_max * carte_width) / 100, 25))
                    pygame.draw.rect(screen, "green", (0, height*0.966, taille_barre_vie, 25))
                    infos_pv = game_font.render(f'{personnage.PV}/{personnage.PV_max}', True, (0, 0, 0))
                    screen.blit(infos_pv, infos_pv.get_rect(center=(50, height*0.985)))
    
    return zones_cliquable