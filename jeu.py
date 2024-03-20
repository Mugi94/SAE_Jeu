from __future__ import annotations
import pygame
import sys

from bouton import Bouton
from plateau import Plateau
from personnage import *
from ennemi import *

from menu.pause_menu import pause_menu
from menu.endgame_menu import endgame_menu
from menu.next_stage_menu import next_stage_menu
from afficher_cartes import afficher_cartes

import constants as const

def lancer_jeu(screen, joueurs, stats, stage = 1):
    width = screen.get_width()
    height = screen.get_height()

    bouton = pygame.image.load(const.BOUTON)
    bouton_cliquable = pygame.image.load(const.BOUTON_CLIQUABLE)
    bouton_font = pygame.font.SysFont("Helvetic", 30)
    game_font = pygame.font.SysFont("Helvetic", 30)
    
    case_cliquable = pygame.image.load(const.CASE_CLIQUABLE)

    run = True
    pause = False
    pause_entre_etape = False

    characters = [joueur.personnage for joueur in joueurs]
    plateau = Plateau(characters)

    ennemis = [
        Ringo(),
        Doppelganger(),
        Lucifer(),
        Medato()
    ]

    ennemi_index = stage - 1
    joueur_actuel_index = 0

    while run:
        mouse_pos = pygame.mouse.get_pos()
        
        # Afficher ennemi
        ennemi = ennemis[ennemi_index]
        if ennemi.PV <= 0 and (not pause_entre_etape):
            pause_entre_etape = True

        # Afficher le jeu
        background = pygame.image.load(const.STAGES[stage])
        screen.blit(background, (0, 0))
        plateau.draw(screen)
        ennemi.draw(screen)
        afficher_cartes(screen, characters)

        joueur_actuel = joueurs[joueur_actuel_index]

        # Boutons en jeu
        # Personnage pas déplacé
        if not joueur_actuel.personnage_deplacer and not joueur_actuel.action_effectuer:
            lancer_de = Bouton(bouton_cliquable, (width*0.389, height*0.765), 'Lancer dé', bouton_font, 'black', 'white')
            lancer_attaque = Bouton(bouton, (width*0.5, height*0.765), 'Attaque', bouton_font, 'black', 'black')
            lancer_capacite = Bouton(bouton, (width*0.612, height*0.765), 'Capacité', bouton_font, 'black', 'black')

        # Personnage déplacé mais pas joué
        elif joueur_actuel.personnage_deplacer and not joueur_actuel.action_effectuer:
            lancer_de = Bouton(bouton, (width*0.389, height*0.765), 'Lancer dé', bouton_font, 'black', 'black')
            lancer_attaque = Bouton(bouton_cliquable, (width*0.5, height*0.765), 'Attaque', bouton_font, 'black', 'white')
            lancer_capacite = Bouton(bouton_cliquable, (width*0.612, height*0.765), 'Capacité', bouton_font, 'black', 'white')
            # gerer capaciter selon personnage
            # ...

        # Afficher les boutons
        for bouton_jeu in [lancer_de, lancer_attaque, lancer_capacite]:
            bouton_jeu.update(screen)

        # Evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not pause_entre_etape:
                        if pause:
                            pause = False
                        else:
                            pause = True

        if pause:
            quitter, reprendre = pause_menu(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitter.checkForInput(mouse_pos):
                    run = False

                if reprendre.checkForInput(mouse_pos):
                    pause = False

        if pause_entre_etape and not (ennemi_index == len(ennemis)):
            quitter, suivant = next_stage_menu(screen)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitter.checkForInput(mouse_pos):
                    run = False

                if suivant.checkForInput(mouse_pos):
                    pause_entre_etape = False
                    ennemi_index += 1
                    stage += 1

        # Jouer tour
        texte_joueur = game_font.render(f"C'est à {joueur_actuel.nom} de jouer", True, (0, 0, 0))
        screen.blit(texte_joueur, texte_joueur.get_rect(center=(width*0.45, height*0.65)))
        
        
        if not (pause or pause_entre_etape):
            # Déplacement du personnage
            # Lancement du dé
            if not joueur_actuel.de_lancer:
                resultat_de = joueur_actuel.lancer_de(lancer_de)

            # Choix du déplacement
            elif joueur_actuel.de_lancer and not joueur_actuel.personnage_deplacer:
                choix_possible = [i+1 for i in range(resultat_de)]

                # Afficher les choix possible
                for choix in choix_possible:
                    indice = (choix + joueur_actuel.personnage.position) % 16
                    if indice == 0:
                        indice = 16
                    screen.blit(case_cliquable, (plateau.zone_cliquable[indice]))

                # Déplacer si choix effectué
                deplacement_choisi = joueur_actuel.choix_deplacement(choix_possible, plateau, joueur_actuel.personnage.position)
                if deplacement_choisi is not None:
                    plateau.deplacer_personnage(joueur_actuel.personnage, deplacement_choisi)
                    deplacement_choisi = None

            # Choisir l'action voulu (attaque ou capacite)
            elif joueur_actuel.personnage_deplacer and not joueur_actuel.action_effectuer:
                action = 0
                action = joueur_actuel.choix_action(lancer_attaque, lancer_capacite)
                if action == 1:
                    degats_joueur = joueur_actuel.personnage.lancerAttaque(ennemi, plateau, stage)
                    stats.addDegatsPersonnages(joueur_actuel.personnage.nom, degats_joueur)
                    stats.addDegatsTotaux(degats_joueur)
                    
                elif action == 2:
                    print("Capacité")
                    # joueur_actuel.personnage.lancerCapacite(...)

            
            # Changer de joueur
            # Si le joueur actuel a joué son tour, on passe au suivant
            if joueur_actuel.action_effectuer:
                joueur_actuel_index = (joueur_actuel_index + 1) % len(joueurs)
                
                # Vérifier que le joueur suivant peut jouer (Personnage en vie), sinon il passe son tour
                while joueurs[joueur_actuel_index].personnage.PV == 0:
                    joueurs[joueur_actuel_index].action_effectuer = True
                    joueur_actuel_index = (joueur_actuel_index + 1) % len(joueurs)

            # Attaque de l'ennemi si tout les joueurs ont joué, puis tour suivant
            if all(joueur.action_effectuer for joueur in joueurs):
                ennemi.lancerAttaque(plateau)
                for joueur in joueurs:
                    joueur.de_lancer = False
                    joueur.personnage_deplacer = False
                    joueur.action_effectuer = False
                print("Tour suivant !")

        pygame.display.update()