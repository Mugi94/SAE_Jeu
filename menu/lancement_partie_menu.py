from __future__ import annotations
from bouton import Bouton
from joueur import Joueur, Aleatoire, Basique
from personnage import *
from jeu import lancer_jeu
from random import choice
import pygame
import sys

import constants as const

def personnage_aleatoire(liste_personnages, personnages_pris):
    personnage = choice(liste_personnages)
    
    while personnage in personnages_pris:
        personnage = choice(liste_personnages)
    return personnage

def lancement_partie_menu(screen, joueurs, personnages, stats):
    width = screen.get_width()
    height = screen.get_height()

    title_font = pygame.font.Font(const.DEMOCRATICA_BOLD, 75)
    text_font = pygame.font.SysFont("Helvetic", 40)
    background = pygame.image.load(const.MENU_LANCEMENT)
    
    # Combler le manque de joueur
    personnage_joueurs = []
    for joueur in joueurs:
        personnage_joueurs.append(joueur.personnage)

    while len(joueurs) < 4:
        personnage = personnage_aleatoire(personnages, personnage_joueurs)
        personnage_joueurs.append(personnage)
        joueurs.append(Basique(personnage))
    

    joueur1_pret = False
    
    if joueurs[1].__class__ is not Joueur:
        joueur2_pret = True
    else:
        joueur2_pret = False

    if joueurs[2].__class__ is not Joueur:
        joueur3_pret = True
    else:
        joueur3_pret = False        

    if joueurs[3].__class__ is not Joueur:
        joueur4_pret = True
    else:
        joueur4_pret = False


    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))

        title = title_font.render("Votre équipe", True, (255,255,255)) ; title_rect = title.get_rect(center=(width*0.5, height*0.14))
        screen.blit(title, title_rect)

        # - Afficher le contour des joueurs
        positions = [(0.13, 0.33), (0.33, 0.33), (0.53, 0.33), (0.73, 0.33)]
        for index, joueur_pret in enumerate([joueur1_pret, joueur2_pret, joueur3_pret, joueur4_pret]):
            x, y = positions[index]
            if joueur_pret:
                pygame.draw.rect(screen, "green", pygame.Rect((width*x - 2.5, height*y - 2.5), (170, 270)))
            else:
                pygame.draw.rect(screen, "red", pygame.Rect((width*x - 2.5, height*y - 2.5), (170, 270)))

        # - Affichage infos des joueurs
        for index, joueur in enumerate(joueurs):
            x, y = positions[index]
            
            nom_joueur = text_font.render(joueur.nom, True, (255,255,255)) ; nom_joueur_rect = nom_joueur.get_rect(center=(width*x + 83, height*0.29))
            screen.blit(nom_joueur, nom_joueur_rect)
        
            personnage_joueur = pygame.image.load(joueur.personnage.images['carte'])
            screen.blit(personnage_joueur, (width*x, height*y))


        # - Boutons des joueurs
        bouton_joueur1 = Bouton(None, (width*0.2, height*0.73), "Prêt", text_font, "white", "black")
        
        if joueurs[1].__class__ is not Joueur:
            bouton_joueur2 = Bouton(None, (width*0.4, height*0.73), "Changer", text_font, "white", "black")
        else:
            bouton_joueur2 = Bouton(None, (width*0.4, height*0.73), "Prêt", text_font, "white", "black")
        
        if joueurs[2].__class__ is not Joueur:
            bouton_joueur3 = Bouton(None, (width*0.6, height*0.73), "Changer", text_font, "white", "black")
        else:
            bouton_joueur3 = Bouton(None, (width*0.6, height*0.73), "Prêt", text_font, "white", "black")

        if joueurs[3].__class__ is not Joueur:
            bouton_joueur4 = Bouton(None, (width*0.8, height*0.73), "Changer", text_font, "white", "black")
        else:
            bouton_joueur4 = Bouton(None, (width*0.8, height*0.73), "Prêt", text_font, "white", "black")

        bouton_lancement = Bouton(None, (width*0.5, height*0.9), "Lancer partie", text_font, "white", "black")

        for bouton in [bouton_joueur1, bouton_joueur2, bouton_joueur3, bouton_joueur4, bouton_lancement]:
            bouton.changeColor(mouse_pos)
            bouton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_joueur1.checkForInput(mouse_pos):
                    if not joueur1_pret:
                        joueur1_pret = True
                    else:
                        joueur1_pret = False

                if bouton_joueur2.checkForInput(mouse_pos):
                    if joueurs[1].__class__ is not Joueur:
                        personnage_joueurs.remove(joueurs[1].personnage)
                        joueurs[1].personnage = personnage_aleatoire(personnages, personnage_joueurs)
                        personnage_joueurs.append(joueurs[1].personnage)
                    else:
                        if not joueur2_pret:
                            joueur2_pret = True
                        else:
                            joueur2_pret = False

                if bouton_joueur3.checkForInput(mouse_pos):
                    if joueurs[2].__class__ is not Joueur:
                        personnage_joueurs.remove(joueurs[2].personnage)
                        joueurs[2].personnage = personnage_aleatoire(personnages, personnage_joueurs)
                        personnage_joueurs.append(joueurs[2].personnage)
                    else:
                        if not joueur3_pret:
                            joueur3_pret = True
                        else:
                            joueur3_pret = False

                if bouton_joueur4.checkForInput(mouse_pos):
                    if joueurs[3].__class__ is not Joueur:
                        personnage_joueurs.remove(joueurs[3].personnage)
                        joueurs[3].personnage = personnage_aleatoire(personnages, personnage_joueurs)
                        personnage_joueurs.append(joueurs[3].personnage)
                    else:
                        if not joueur4_pret:
                            joueur4_pret = True
                        else:
                            joueur4_pret = False

                if bouton_lancement.checkForInput(mouse_pos):
                    if all([joueur1_pret, joueur2_pret, joueur3_pret, joueur4_pret]):
                        lancer_jeu(screen, joueurs, stats)
                        run = False

        pygame.display.update()