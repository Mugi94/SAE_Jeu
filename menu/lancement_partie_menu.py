from __future__ import annotations
from bouton import Bouton
from joueur import Joueur, Aleatoire
from personnage import *
from jeu import lancer_jeu
import pygame
import sys

import constants as const

def previous(indice, personnages):
    indice -= 1
    if indice < 0:
        indice = len(personnages) - 1
    return indice

def next(indice, personnages):
    indice += 1
    if indice >= len(personnages):
        indice = 0
    return indice


def lancement_partie_menu(screen, personnage, personnages, stats):
    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 75)
    text_font = pygame.font.SysFont("Helvetic", 50)
    confirm_text_font = pygame.font.SysFont("Helvetic", 30)
    next_img = pygame.transform.scale(pygame.image.load(const.BOUTON_SUIVANT), (30, 30))
    previous_img = pygame.transform.scale(pygame.image.load(const.BOUTON_PRECEDENT), (30, 30))
    background = pygame.image.load(const.MENU_LANCEMENT)
    
    indices = [i for i in range(len(personnages))]
    indices.remove(personnages.index(personnage))
    indice_choix_2 = indices[0] ; indice_choix_3 = indices[1] ; indice_choix_4 = indices[2]

    joueur1 = Joueur(personnage, "Joueur1")
    joueur2 = Joueur(personnages[indice_choix_2], "Joueur2") ; joueur_2_pret = False
    joueur3 = Joueur(personnages[indice_choix_3], "Joueur3") ; joueur_3_pret = False
    joueur4 = Joueur(personnages[indice_choix_4], "Joueur4") ; joueur_4_pret = False

    personnages_pris = [personnage]

    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        
        personnage_2 = personnages[indice_choix_2]
        personnage_3 = personnages[indice_choix_3]
        personnage_4 = personnages[indice_choix_4]

        title = title_font.render("Votre équipe", True, (255,255,255)) ; title_rect = title.get_rect(center=(const.WIDTH*0.5, const.HEIGHT*0.14))
        screen.blit(title, title_rect)

        carte_personnage = pygame.image.load(personnage.images['carte'])
        pygame.draw.rect(screen, "green", pygame.Rect((const.WIDTH*0.13-2.5, const.HEIGHT/3-2.5),(carte_personnage.get_width()+5, carte_personnage.get_height()+5)))
        screen.blit(carte_personnage, (const.WIDTH*0.13, const.HEIGHT/3))
        changer_personnage = Bouton(None, (const.WIDTH*0.2, const.HEIGHT*0.73), "Changer", confirm_text_font, "white", "black")


        if personnage_2 in personnages_pris and not joueur_2_pret:
            carte_personnage_2 = pygame.image.load(personnage_2.images['carte_grise'])
        else:
            carte_personnage_2 = pygame.image.load(personnage_2.images['carte'])

        if joueur_2_pret:
            pygame.draw.rect(screen, "green", pygame.Rect((const.WIDTH*0.33-2.5, const.HEIGHT/3-2.5),(carte_personnage_2.get_width()+5, carte_personnage_2.get_height()+5)))
        else:
            pygame.draw.rect(screen, "red", pygame.Rect((const.WIDTH*0.33-2.5, const.HEIGHT/3-2.5),(carte_personnage_2.get_width()+5, carte_personnage_2.get_height()+5)))
        screen.blit(carte_personnage_2, (const.WIDTH*0.33, const.HEIGHT/3))
        confirm_button_2 = Bouton(None, (const.WIDTH*0.4, const.HEIGHT*0.73), "Confirmer", confirm_text_font, "white", "black")
        previous_button_2 = Bouton(previous_img, (const.WIDTH*0.34, const.HEIGHT*0.73), "", text_font, "white", "white")
        next_button_2 = Bouton(next_img, (const.WIDTH*0.45, const.HEIGHT*0.73), "", text_font, "white", "white")


        if personnage_3 in personnages_pris and not joueur_3_pret:
            carte_personnage_3 = pygame.image.load(personnage_3.images['carte_grise'])
        else:
            carte_personnage_3 = pygame.image.load(personnage_3.images['carte'])

        if joueur_3_pret:
            pygame.draw.rect(screen, "green", pygame.Rect((const.WIDTH*0.53-2.5, const.HEIGHT/3-2.5),(carte_personnage_2.get_width()+5, carte_personnage_2.get_height()+5)))
        else:
            pygame.draw.rect(screen, "red", pygame.Rect((const.WIDTH*0.53-2.5, const.HEIGHT/3-2.5),(carte_personnage_2.get_width()+5, carte_personnage_2.get_height()+5)))
        screen.blit(carte_personnage_3, (const.WIDTH*0.53, const.HEIGHT/3))
        confirm_button_3 = Bouton(None, (const.WIDTH*0.6, const.HEIGHT*0.73), "Confirmer", confirm_text_font, "white", "black")
        previous_button_3 = Bouton(previous_img, (const.WIDTH*0.54, const.HEIGHT*0.73), "", text_font, "white", "white")
        next_button_3 = Bouton(next_img, (const.WIDTH*0.65, const.HEIGHT*0.73), "", text_font, "white", "white")

        if personnage_4 in personnages_pris and not joueur_4_pret:
            carte_personnage_4 = pygame.image.load(personnage_4.images['carte_grise'])
        else:
            carte_personnage_4 = pygame.image.load(personnage_4.images['carte'])

        if joueur_4_pret:
            pygame.draw.rect(screen, "green", pygame.Rect((const.WIDTH*0.73-2.5, const.HEIGHT/3-2.5),(carte_personnage_2.get_width()+5, carte_personnage_2.get_height()+5)))
        else:
            pygame.draw.rect(screen, "red", pygame.Rect((const.WIDTH*0.73-2.5, const.HEIGHT/3-2.5),(carte_personnage_2.get_width()+5, carte_personnage_2.get_height()+5)))
        screen.blit(carte_personnage_4, (const.WIDTH*0.73, const.HEIGHT/3))
        confirm_button_4 = Bouton(None, (const.WIDTH*0.8, const.HEIGHT*0.73), "Confirmer", confirm_text_font, "white", "black")
        previous_button_4 = Bouton(previous_img, (const.WIDTH*0.74, const.HEIGHT*0.73), "", text_font, "white", "white")
        next_button_4 = Bouton(next_img, (const.WIDTH*0.85, const.HEIGHT*0.73), "", text_font, "white", "white")

        launch_button = Bouton(None, (const.WIDTH*0.5, const.HEIGHT*0.9), "Lancer partie", text_font, "white", "black")

        for button in [launch_button, changer_personnage,
                       confirm_button_2, confirm_button_3, confirm_button_4,
                       previous_button_2, previous_button_3, previous_button_4,
                       next_button_2, next_button_3, next_button_4]:

            button.changeColor(mouse_pos)
            button.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if changer_personnage.checkForInput(mouse_pos):
                    run = False
                
                if previous_button_2.checkForInput(mouse_pos) and not joueur_2_pret:
                    indice_choix_2 = previous(indice_choix_2, personnages)
                    joueur2.personnage = personnages[indice_choix_2]

                if next_button_2.checkForInput(mouse_pos) and not joueur_2_pret:
                    indice_choix_2 = next(indice_choix_2, personnages)
                    joueur2.personnage = personnages[indice_choix_2]

                if confirm_button_2.checkForInput(mouse_pos):
                    if not joueur_2_pret and joueur2.personnage not in personnages_pris:
                        personnages_pris.append(personnage_2)
                        joueur_2_pret = True


                if previous_button_3.checkForInput(mouse_pos) and not joueur_3_pret:
                    indice_choix_3 = previous(indice_choix_3, personnages)
                    joueur3.personnage = personnages[indice_choix_3]

                if next_button_3.checkForInput(mouse_pos) and not joueur_3_pret:
                    indice_choix_3 = next(indice_choix_3, personnages)
                    joueur3.personnage = personnages[indice_choix_3]

                if confirm_button_3.checkForInput(mouse_pos):
                    if not joueur_3_pret and joueur3.personnage not in personnages_pris:
                        personnages_pris.append(personnage_3)
                        joueur_3_pret = True


                if previous_button_4.checkForInput(mouse_pos) and not joueur_4_pret:
                    indice_choix_4 = previous(indice_choix_4, personnages)
                    joueur4.personnage = personnages[indice_choix_4]

                if next_button_4.checkForInput(mouse_pos) and not joueur_4_pret:
                    indice_choix_4 = next(indice_choix_4, personnages)
                    joueur4.personnage = personnages[indice_choix_4]

                if confirm_button_4.checkForInput(mouse_pos):
                    if not joueur_4_pret and joueur4.personnage not in personnages_pris:
                        personnages_pris.append(personnage_4)
                        joueur_4_pret = True

                if launch_button.checkForInput(mouse_pos):
                    if joueur_2_pret == True and joueur_3_pret == True and joueur_4_pret == True:
                        lancer_jeu(screen, [joueur1, joueur2, joueur3, joueur4], stats)
                        run = False

        pygame.display.update()