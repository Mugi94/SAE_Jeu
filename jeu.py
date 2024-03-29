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
    bouton_attente = pygame.image.load(const.BOUTON_EN_ATTENTE)
    bouton_font = pygame.font.SysFont("Helvetic", 30)
    game_font = pygame.font.SysFont("Helvetic", 30)
    
    case_cliquable = pygame.image.load(const.CASE_CLIQUABLE)

    run = True
    pause = False
    pause_entre_etape = False
    
    gagne = False
    perdu = False

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
        if ennemi.PV <= 0 and not pause_entre_etape and not (gagne or perdu):
            pause_entre_etape = True
            stats.addScore(ennemi.PV_max)

        # Afficher le jeu
        background = pygame.image.load(const.STAGES[stage])
        screen.blit(background, (0, 0))
        ennemi.draw(screen)
        plateau.draw(screen)
        cartes_personnage = afficher_cartes(screen, characters)

        joueur_actuel = joueurs[joueur_actuel_index]

        # Afficher joueur actuel
        texte_joueur = game_font.render(f"Au tour de {joueur_actuel.nom}", True, (0, 0, 0))
        personnage_image = pygame.image.load(joueur_actuel.personnage.images['icone'])
        screen.blit(texte_joueur, texte_joueur.get_rect(center=(width*0.42, height*0.26)))
        screen.blit(personnage_image, (width*0.34, height*0.28))

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
            
            if joueur_actuel.personnage.capacite['active'] and joueur_actuel.personnage.capacite['choix_necessaire']:
                lancer_capacite = Bouton(bouton_attente, (width*0.612, height*0.765), 'Capacité', bouton_font, 'black', 'white')
            
            elif (joueur_actuel.personnage.capacite['active'] or (joueur_actuel.personnage.capacite['passive']) and not joueur_actuel.personnage.capacite['choix_necessaire']) or joueur_actuel.cooldown != joueur_actuel.personnage.capacite['temps_rechargement']:
                lancer_capacite = Bouton(bouton, (width*0.612, height*0.765), 'Capacité', bouton_font, 'black', 'white')

            else:
                lancer_capacite = Bouton(bouton_cliquable, (width*0.612, height*0.765), 'Capacité', bouton_font, 'black', 'white')


        # Afficher les boutons
        for bouton_jeu in [lancer_de, lancer_attaque, lancer_capacite]:
            bouton_jeu.update(screen)


        # Afficher cooldown capacite
        if joueur_actuel.personnage.capacite['passive']:
                pygame.draw.circle(screen, (0, 0, 255), (width*0.65, height*0.71), 10)
                pygame.draw.circle(screen, (0, 0, 0), (width*0.65, height*0.71), 10, 3)
        
        elif joueur_actuel.personnage.capacite['temps_rechargement'] is None:
            if joueur_actuel.cooldown is None:
                pygame.draw.circle(screen, (0, 255, 0), (width*0.65, height*0.71), 10)
                pygame.draw.circle(screen, (0, 0, 0), (width*0.65, height*0.71), 10, 3)
            else:
                pygame.draw.circle(screen, (255, 0, 0), (width*0.65, height*0.71), 10)
                pygame.draw.circle(screen, (0, 0, 0), (width*0.65, height*0.71), 10, 3)

        else:
            nb_cooldown = min(joueur_actuel.cooldown, joueur_actuel.personnage.capacite['temps_rechargement'])
            for i in range(joueur_actuel.personnage.capacite['temps_rechargement']):
                if i < nb_cooldown:
                    pygame.draw.circle(screen, (0, 255, 0), (width*0.65 - 30*i, height*0.71), 10)
                    pygame.draw.circle(screen, (0, 0, 0), (width*0.65 - 30*i, height*0.71), 10, 3)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (width*0.65 - 30*i, height*0.71), 10)
                    pygame.draw.circle(screen, (0, 0, 0), (width*0.65 - 30*i, height*0.71), 10, 3)


        # Evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not pause_entre_etape and not (gagne or perdu):
                        if pause:
                            pause = False
                        else:
                            pause = True

        if pause:
            quitter, reprendre = pause_menu(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitter.checkForInput(mouse_pos):
                    stats.exportStats()
                    run = False

                if reprendre.checkForInput(mouse_pos):
                    pause = False

        if pause_entre_etape and not (gagne or perdu):
            quitter, suivant = next_stage_menu(screen)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitter.checkForInput(mouse_pos):
                    stats.exportStats()
                    run = False

                if suivant.checkForInput(mouse_pos):
                    pause_entre_etape = False
                    ennemi_index += 1
                    stage += 1

        # Vérification des personnages en vie
        for joueur in joueurs:
            if joueur.personnage.PV <= 0 and joueur.personnage in plateau.personnages:
                plateau.case(joueur.personnage.position).enlevePersonnage(joueur.personnage)
                if joueur_actuel == joueur:
                    joueur_actuel.action_effectuer = True

            if joueur.personnage.PV > 0 and joueur.personnage not in plateau.personnages:
                plateau.ajouter_personnage(joueur.personnage, joueur.personnage.position)

        # Jouer tour
        if not (pause or pause_entre_etape or gagne or perdu) or joueur_actuel.action_effectuer:
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
                joueur_actuel.action = joueur_actuel.choix_action(lancer_attaque, lancer_capacite)

                if joueur_actuel.action == 1 and not (joueur_actuel.personnage.capacite['choix_necessaire'] and joueur_actuel.personnage.capacite['active']):
                    degats_joueur = joueur_actuel.personnage.lancerAttaque(ennemi, plateau, stage)
                    joueur_actuel.action_effectuer = True
                    print(f"{joueur_actuel.personnage} inflige {degats_joueur} de degats à {ennemi}")
                    
                    stats.addDegatsPersonnages(joueur_actuel.personnage.nom, degats_joueur)
                    stats.addDegatsTotaux(degats_joueur)

                elif joueur_actuel.action == 2 and joueur_actuel.cooldown == joueur_actuel.personnage.capacite['temps_rechargement']:
                    if not joueur_actuel.personnage.capacite['choix_necessaire'] or not joueur_actuel.personnage.capacite['passive']:
                        degats_joueur = joueur_actuel.personnage.lancerCapacite(ennemi, plateau, stage, cartes_personnage, ennemi)
                        joueur_actuel.action_effectuer = True
                        joueur_actuel.cooldown = -1
                        print(f"{joueur_actuel.personnage} utilise {joueur_actuel.personnage.capacite['nom']}")
                        
                        stats.addDegatsPersonnages(joueur_actuel.personnage.nom, degats_joueur)
                        stats.addDegatsTotaux(degats_joueur)

                    # Capacité a choix
                    else:
                        joueur_actuel.personnage.capacite['active'] = True

                # Choix pour la capacité
                if joueur_actuel.personnage.capacite['choix_necessaire'] and joueur_actuel.personnage.capacite['active']:
                    texte_action = game_font.render(f"Choissisez un personnage", True, (0, 0, 0))
                    screen.blit(texte_action, texte_joueur.get_rect(center=(width*0.41, height*0.71)))
                    
                    choix_joueur = joueur_actuel.choix_capacite(plateau, cartes_personnage)
                    if choix_joueur is not None and not (joueur_actuel.personnage.capacite['nom'] == "Heaven Canceller" and choix_joueur.PV != 0):
                        
                        # A ne pas faire de base mais evite au jeu de se fermer
                        if joueur_actuel.personnage.capacite['nom'] == "Heaven Canceller" and choix_joueur.PV != 0:
                            choix_joueur = None
                            continue
                        
                        degats_joueur = joueur_actuel.personnage.lancerCapacite(choix_joueur, plateau, stage, cartes_personnage, ennemi)
                        joueur_actuel.action_effectuer = True
                        joueur_actuel.personnage.capacite['active'] = False
                        joueur_actuel.cooldown = -1
                        print(f"{joueur_actuel.personnage} utilise {joueur_actuel.personnage.capacite['nom']} sur {choix_joueur}")
                    


            # Changer de joueur
            # Si le joueur actuel a joué son tour, on passe au suivant
            if joueur_actuel.action_effectuer:
                if joueur_actuel.personnage.capacite['temps_rechargement'] is not None:
                    if not (joueur_actuel.personnage.PV <= 0) and (joueur_actuel.cooldown < joueur_actuel.personnage.capacite['temps_rechargement']):
                        joueur_actuel.cooldown += 1

                joueur_actuel_index = (joueur_actuel_index + 1) % len(joueurs)
                
                # Vérifier que le joueur suivant peut jouer
                if joueurs[joueur_actuel_index].personnage not in plateau.personnages or joueurs[joueur_actuel_index].personnage.PV <= 0:
                    joueurs[joueur_actuel_index].action_effectuer = True
                    joueur_actuel_index = (joueur_actuel_index + 1) % len(joueurs)

            # Attaque de l'ennemi si tout les joueurs ont joué, puis tour suivant
            if all(joueur.action_effectuer for joueur in joueurs):
                ennemi.lancerAttaque(plateau, stage)
                for joueur in joueurs:
                    joueur.de_lancer = False
                    joueur.personnage_deplacer = False
                    joueur.action = 0
                    joueur.action_effectuer = False
                print("Tour suivant !")


        if len(plateau.personnages) == 0:
            perdu = True

        if stage == len(ennemis) and ennemi.PV <= 0:
            gagne = True

        if perdu or gagne:
            quitter, recommencer = endgame_menu(screen, gagne)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitter.checkForInput(mouse_pos):
                    run = False

                if recommencer.checkForInput(mouse_pos):
                    lancer_jeu()

        pygame.display.update()