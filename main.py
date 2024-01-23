# --------------------------------------------------------------
#              SAE C1 - Création d'un jeu de société
#                       BUT2 Informatique
# Minet Lorik
# TD2-TPC
# Année 2023-2024
# --------------------------------------------------------------

# -------------------------------------
# Importations
# -------------------------------------
from __future__ import annotations
from random import choice, randint
import pygame
import sys
import os

from bouton import Bouton
from plateau import Plateau
from personnage import *

# Chemin du répertoire courant
PATH = os.path.dirname(os.path.abspath(__file__))

# Initialisation de pygame
pygame.init()

# ------------Création de la fenêtre------------
WIDTH = 1280
HEIGHT = 720
screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("La cité academique")

# ------------Charger les images------------
MENU_BG = pygame.image.load(f"{PATH}/img/menu_principal.jpg")

# Cases du plateau
NEUTRE = pygame.image.load(f"{PATH}/img/cases/case_neutre.png")
BONUS = pygame.image.load(f"{PATH}/img/cases/case_bonus.png")
MALUS = pygame.image.load(f"{PATH}/img/cases/case_malus.png")
CASE_CLIQUABLE = pygame.image.load(f"{PATH}/img/cases/case_cliquable.png")
CASES = [NEUTRE, BONUS, MALUS]

# Fond des lieux
LISTE_LIEUX = {1: f"{PATH}/img/lieux/ruelles.jpg",
               2: f"{PATH}/img/lieux/ruines.jpg",
               3: f"{PATH}/img/lieux/aeroport.jpg",
               4: f"{PATH}/img/lieux/sous-terrain.jpg"}

# Affinite lieu
LIEU_CONTENT = pygame.image.load(f"{PATH}/img/lieux/lieucontent.png")
LIEU_NEUTRE = pygame.image.load(f"{PATH}/img/lieux/lieuneutre.png")
LIEU_PAS_CONTENT = pygame.image.load(f"{PATH}/img/lieux/lieupascontent.png")

# Boutons
MENU_BOUTON = pygame.image.load(f"{PATH}/img/test.png")
BOUTON = pygame.image.load(f"{PATH}/img/boutons/jeubouton.png")
BOUTON_CLIQUABLE = pygame.image.load(f"{PATH}/img/boutons/jeuboutoncliquable.png")
BOUTON_EN_ATTENTE = pygame.image.load(f"{PATH}/img/boutons/jeuboutonattente.png")


# Zone cliquable des cases
RECT_CASES = {
    # Horizontal haut
    1 : pygame.Rect((280, 0), (144,144)),
    2 : pygame.Rect((424, 0), (144,144)),
    3 : pygame.Rect((568, 0), (144,144)),
    4 : pygame.Rect((712, 0), (144,144)),
    
    # Vertical droite
    5 : pygame.Rect((856, 0), (144,144)),
    6 : pygame.Rect((856, 144), (144,144)),
    7 : pygame.Rect((856, 288), (144,144)),
    8 : pygame.Rect((856, 432), (144,144)),
    
    # Horizontal bas
    9 : pygame.Rect((856, 576), (144,144)),
    10 : pygame.Rect((712, 576), (144,144)),
    11 : pygame.Rect((568, 576), (144,144)),
    12 : pygame.Rect((424, 576), (144,144)),
    
    # Vertical gauche
    13 : pygame.Rect((280, 576), (144,144)),
    14 : pygame.Rect((280, 432), (144,144)),
    15 : pygame.Rect((280, 288), (144,144)),
    16 : pygame.Rect((280, 144), (144,144))
    }

# ------------Polices texte------------
BOUTON_FONT = pygame.font.SysFont("Helvetic", 30)
TITRE_FONT = pygame.font.SysFont("Helvetic", 50)
JEU_FONT = pygame.font.SysFont("Helvetic", 30)
MENU_TITRE_FONT = pygame.font.Font(f'{PATH}/fonts/Democratica Bold.ttf', 75)
MENU_BOUTON_FONT = pygame.font.SysFont("Helvetic", 50)

# --------------------------
# Fonctions de jeu
# --------------------------
def checkForInput(rect: pygame.Rect, position: tuple[int,int]) -> bool:
    """
    Renvoie vrai si le bouton est survolé.
    :param rect: (Rect)
    :param position: (tuple) coordonnées de la forme (x,y)
    :return: (bool)
    """
    return (position[0] in range(rect.left, rect.right)) and (position[1] in range(rect.top, rect.bottom))

def affichePlateau(plateau: Plateau) -> None:
    """
    Affiche le plateau a l'écran
    :param plateau: (Plateau)
    :return: (None)
    """  
    # i+1 car paramètre de getCase() = numéro case et non indice du tableau (numéro case = indice de la case + 1)
    # Horizontal haut [1,2,3,4] / ((i*144) + 280, 0) => *144 pour espace entre case et 280 pour la position sur l'écran
    for i in range(int(plateau.TAILLE/4)):
        if plateau.getCase(i+1).getType() == 'N':
            screen.blit(NEUTRE, ((i*144) + 280, 0))
        if plateau.getCase(i+1).getType() == 'B':
            screen.blit(BONUS, ((i*144) + 280, 0))
        if plateau.getCase(i+1).getType() == 'M':
            screen.blit(MALUS, ((i*144) + 280, 0))
        
        # Afficher le/les personages présent
        if plateau.getCase(i+1).getPersonnages() != []:
            # Pour chaque personnage présent sur le plateau
            for pers in plateau.getCase(i+1).getPersonnages():
                # Position propre a chaque personnage sur la case pour eviter la superposition
                if isinstance(pers, Aurore):
                    screen.blit(pygame.image.load(pers.getImg()), ((i*144) + 285, 5))
                
                if isinstance(pers, Akane):
                    screen.blit(pygame.image.load(pers.getImg()), ((i*144) + 355, 5))
                
                if isinstance(pers, Laura):
                    screen.blit(pygame.image.load(pers.getImg()), ((i*144) + 285, 75))
                
                if isinstance(pers, Bob):
                    screen.blit(pygame.image.load(pers.getImg()), ((i*144) + 355, 75))
                
    # Vertical droite [5,6,7,8]
    for j in range(int(plateau.TAILLE/4)):
        if plateau.getCase(j+5).getType() == 'N':
            screen.blit(NEUTRE, (856, (j*144)))
        if plateau.getCase(j+5).getType() == 'B':
            screen.blit(BONUS, (856, (j*144)))
        if plateau.getCase(j+5).getType() == 'M':
            screen.blit(MALUS, (856, (j*144)))
            
        # Afficher le/les personages présent
        if plateau.getCase(j+5).getPersonnages() != []:
            for pers in plateau.getCase(j+5).getPersonnages():
                if isinstance(pers, Aurore):
                    screen.blit(pygame.image.load(pers.getImg()), (861, (j*144) + 5))
                
                if isinstance(pers, Akane):
                    screen.blit(pygame.image.load(pers.getImg()), (931, (j*144) + 5))
                
                if isinstance(pers, Laura):
                    screen.blit(pygame.image.load(pers.getImg()), (861, (j*144) + 75))
                
                if isinstance(pers, Bob):
                    screen.blit(pygame.image.load(pers.getImg()), (931, (j*144) + 75))

    # Horizontal bas [12,11,10,9]  (inversé car plateau circulaire)
    for k in reversed(range(int(plateau.TAILLE/4))):
        if plateau.getCase(k+9).getType() == 'N':
            screen.blit(NEUTRE, (((plateau.TAILLE/4 - k-1)*144) + 424, 576))
        if plateau.getCase(k+9).getType() == 'B':
            screen.blit(BONUS, (((plateau.TAILLE/4 - k-1)*144) + 424, 576))
        if plateau.getCase(k+9).getType() == 'M':
            screen.blit(MALUS, (((plateau.TAILLE/4 - k-1)*144) + 424, 576))

        # Afficher le/les personages présent
        if plateau.getCase(k+9).getPersonnages() != []:
            for pers in plateau.getCase(k+9).getPersonnages():
                if isinstance(pers, Aurore):
                    screen.blit(pygame.image.load(pers.getImg()), (((plateau.TAILLE/4 - k-1)*144) + 429, 581))
                
                if isinstance(pers, Akane):
                    screen.blit(pygame.image.load(pers.getImg()), (((plateau.TAILLE/4 - k-1)*144) + 499, 581))
                
                if isinstance(pers, Laura):
                    screen.blit(pygame.image.load(pers.getImg()), (((plateau.TAILLE/4 - k-1)*144) + 429, 651))
                
                if isinstance(pers, Bob):
                    screen.blit(pygame.image.load(pers.getImg()), (((plateau.TAILLE/4 - k-1)*144) + 499, 651))

    # Vertical gauche [16,15,14,13] (inversé car plateau circulaire)
    for l in reversed(range(int(plateau.TAILLE/4))):
        if plateau.getCase(l+13).getType() == 'N':
            screen.blit(NEUTRE, (280, ((plateau.TAILLE/4 - l-1)*144) + 144))
        if plateau.getCase(l+13).getType() == 'B':
            screen.blit(BONUS, (280, ((plateau.TAILLE/4 - l-1)*144) + 144))
        if plateau.getCase(l+13).getType() == 'M':
            screen.blit(MALUS, (280, ((plateau.TAILLE/4 - l-1)*144) + 144))

        # Afficher le/les personages présent
        if plateau.getCase(l+13).getPersonnages() != []:
            for pers in plateau.getCase(l+13).getPersonnages():
                if isinstance(pers, Aurore):
                    screen.blit(pygame.image.load(pers.getImg()), (285, ((plateau.TAILLE/4 - l-1)*144) + 149))
                
                if isinstance(pers, Akane):
                    screen.blit(pygame.image.load(pers.getImg()), (355, ((plateau.TAILLE/4 - l-1)*144) + 149))
                
                if isinstance(pers, Laura):
                    screen.blit(pygame.image.load(pers.getImg()), (285, ((plateau.TAILLE/4 - l-1)*144) + 219))
                
                if isinstance(pers, Bob):
                    screen.blit(pygame.image.load(pers.getImg()), (355, ((plateau.TAILLE/4 - l-1)*144) + 219))

def afficheCartes(persos: list[Personnage], perso_actif: Personnage, etape: int) -> None:
    """
    Affiche les cartes des 4 personnages du jeu a l'écran.
    :param persos: (List) une liste des personnage en jeu
    :param perso_actif: (Personnage) le personnage qui joue actuellement
    :param etape: (int)
    :return: (None)
    """
    # Afficher la carte du premier personnage
    screen.blit(pygame.image.load(persos[0].getCarte()), (0, 0))
    
    # Statistique du premier personnage
    perso1_pv: pygame.Surface = JEU_FONT.render(f"PV = {persos[0].getPV()}", True, "black")
    perso1_atk: pygame.Surface = JEU_FONT.render(f"A = {persos[0].getATK()}", True, "black")
    perso1_def: pygame.Surface = JEU_FONT.render(f"D = {persos[0].getDEF()}", True, "black")
    
    # Vérification si premier personnage actif, afficher la zone des statistique en rouge
    if isinstance(perso_actif, Aurore):
        pygame.draw.rect(screen, "red", pygame.Rect((0,265),(165,75)))
    else: pygame.draw.rect(screen, "black", pygame.Rect((0,265),(165,75)))
    
    # Afficher les statistique du premier personnage a l'écran
    pygame.draw.rect(screen, (208,244,244), pygame.Rect((5,270),(155,65)))
    screen.blit(perso1_pv, perso1_pv.get_rect(center=(55, 290)))
    screen.blit(perso1_atk, perso1_atk.get_rect(center=(40, 320))) ; screen.blit(perso1_def, perso1_def.get_rect(center=(125, 320)))
    
    # Afficher l'affinité de lieu du premier personnage
    if persos[0].getType() == etape:
        screen.blit(LIEU_CONTENT, (115, 275))
    elif persos[0].getInverseType() == etape:
        screen.blit(LIEU_PAS_CONTENT, (115, 275))
    else:
        screen.blit(LIEU_NEUTRE, (115, 275))
    
    
    # Afficher la carte du second personnage
    screen.blit(pygame.image.load(persos[1].getCarte()), (WIDTH-165, 0))
    
    # Statistique du second personnage
    perso2_pv = JEU_FONT.render(f"PV = {persos[1].getPV()}", True, "black")
    perso2_atk = JEU_FONT.render(f"A = {persos[1].getATK()}", True, "black")
    perso2_def = JEU_FONT.render(f"D = {persos[1].getDEF()}", True, "black")
    
    # Vérification si second personnage actif, afficher la zone des statistique en rouge
    if isinstance(perso_actif, Akane):
        pygame.draw.rect(screen, "red", pygame.Rect((1115,265),(165,75)))
    else: pygame.draw.rect(screen, "black", pygame.Rect((1115,265),(165,75)))
    
    # Afficher les statistique du second personnage a l'écran
    pygame.draw.rect(screen, (208,244,244), pygame.Rect((1120,270),(155,65)))
    screen.blit(perso2_pv, perso2_pv.get_rect(center=(1170, 290)))
    screen.blit(perso2_atk, perso2_atk.get_rect(center=(1155, 320))) ; screen.blit(perso2_def, perso2_def.get_rect(center=(1240, 320)))
    
    # Afficher l'affinité de lieu du second personnage
    if persos[1].getType() == etape:
        screen.blit(LIEU_CONTENT, (1225, 275))
    elif persos[1].getInverseType() == etape:
        screen.blit(LIEU_PAS_CONTENT, (1225, 275))
    else:
        screen.blit(LIEU_NEUTRE, (1225, 275))
        
    
    # Afficher la carte du troisieme personnage
    screen.blit(pygame.image.load(persos[2].getCarte()), (WIDTH-165, HEIGHT-340))
    
    # Statistique du troisieme personnage
    perso3_pv = JEU_FONT.render(f"PV = {persos[2].getPV()}", True, "black")
    perso3_atk = JEU_FONT.render(f"A = {persos[2].getATK()}", True, "black")
    perso3_def = JEU_FONT.render(f"D = {persos[2].getDEF()}", True, "black")
    
    # Vérification si troisieme personnage actif, afficher la zone des statistique en rouge
    if isinstance(perso_actif, Bob):
        pygame.draw.rect(screen, "red", pygame.Rect((1115,645),(165,75)))
    else: pygame.draw.rect(screen, "black", pygame.Rect((1115,645),(165,75)))
    
    # Afficher les statistique du troisieme personnage a l'écran
    pygame.draw.rect(screen, (208,244,244), pygame.Rect((1120,650),(155,65)))
    screen.blit(perso3_pv, perso3_pv.get_rect(center=(1170, 670)))
    screen.blit(perso3_atk, perso3_atk.get_rect(center=(1155, 700))) ; screen.blit(perso3_def, perso3_def.get_rect(center=(1240, 700)))
    
    # Afficher l'affinité de lieu du troisieme personnage
    if persos[2].getType() == etape:
        screen.blit(LIEU_CONTENT, (1225, 655))
    elif persos[2].getInverseType() == etape:
        screen.blit(LIEU_PAS_CONTENT, (1225, 655))
    else:
        screen.blit(LIEU_NEUTRE, (1225, 655))
    
    
    # Afficher la carte du quatrieme personnage
    screen.blit(pygame.image.load(persos[3].getCarte()), (0, HEIGHT-340))
    
    # Statistique du quatrieme personnage
    perso4_pv = JEU_FONT.render(f"PV = {persos[3].getPV()}", True, "black")
    perso4_atk = JEU_FONT.render(f"A = {persos[3].getATK()}", True, "black")
    perso4_def = JEU_FONT.render(f"D = {persos[3].getDEF()}", True, "black")
    
    # Vérification si quatrieme personnage actif, afficher la zone des statistique en rouge
    if isinstance(perso_actif, Laura):
         pygame.draw.rect(screen, "red", pygame.Rect((0,645),(165,75)))
    else: pygame.draw.rect(screen, "black", pygame.Rect((0,645),(165,75)))
    
    # Afficher les statistique du quatrieme personnage a l'écran
    pygame.draw.rect(screen, (208,244,244), pygame.Rect((5,650),(155,65)))
    screen.blit(perso4_pv, perso4_pv.get_rect(center=(55, 670)))
    screen.blit(perso4_atk, perso4_atk.get_rect(center=(40, 700))) ; screen.blit(perso4_def, perso4_def.get_rect(center=(125, 700)))

    # Afficher l'affinité de lieu du quatrieme personnage
    if persos[3].getType() == etape:
        screen.blit(LIEU_CONTENT, (115, 655))
    elif persos[3].getInverseType() == etape:
        screen.blit(LIEU_PAS_CONTENT, (115, 655))
    else:
        screen.blit(LIEU_NEUTRE, (115, 655))

def afficheEnnemi(ennemi: Ennemi) -> None:
    """
    Affiche l'ennemi dans le plateau.
    :param ennemi: (Ennemi)
    :return: (None)
    """
    # Afficher l'image de l'ennemi
    screen.blit(pygame.image.load(ennemi.getImg()), (520, 150))
    
    # Afficher les points de vie de l'ennemi
    ennemi_pv: pygame.Surface = JEU_FONT.render(f"PV = {ennemi.getPV()}", True, (255, 255, 255))
    screen.blit(ennemi_pv, ennemi_pv.get_rect(center=(480, 170)))

def menuPause() -> tuple[Bouton, Bouton]:
    """
    Affiche le menu de pause a l'ecran.
    :return: (Tuple) les boutons du menu
    """
    # Positionnement de la souris
    pause_mouse_pos: tuple[int,int] = pygame.mouse.get_pos()
    
    # Fond du menu de pause
    pause_surface: pygame.Surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(pause_surface, (128, 128, 128, 150), [0, 0 ,WIDTH, HEIGHT]) ; screen.blit(pause_surface, (0,0))
    
    # Titre du menu de pause
    pause_title: pygame.Surface = TITRE_FONT.render("PAUSE", True, (255, 255, 255))
    pause_title_rect: pygame.Rect = pause_title.get_rect(center=(WIDTH//2, 250)) ; screen.blit(pause_title, pause_title_rect)
    
    # Boutons du menu pause
    pause_quitter: Bouton = Bouton(None, (WIDTH//2, 450), "QUITTER", MENU_BOUTON_FONT, "black", "White")
    pause_quitter.changeColor(pause_mouse_pos) ; pause_quitter.update(screen)
    
    pause_reprendre: Bouton = Bouton(None, (WIDTH//2, 350), "REPRENDRE", MENU_BOUTON_FONT, "black", "White")
    pause_reprendre.changeColor(pause_mouse_pos) ; pause_reprendre.update(screen)

    return pause_quitter, pause_reprendre

def menuBossSuivant() -> tuple[Bouton, Bouton]:
    """
    Affiche le menu d'entre deux boss a l'ecran.
    :return: (Tuple) les boutons du menu
    """
    # Positionnement de la souris
    pause_mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
    
    # Fond du menu de pause
    pause_surface: pygame.Surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(pause_surface, (128, 128, 128, 150), [0, 0 ,WIDTH, HEIGHT]) ; screen.blit(pause_surface, (0,0))
    
    # Titre du menu de pause
    pause_title: pygame.Surface = TITRE_FONT.render("Boss vaincu", True, (255, 255, 255))
    pause_title_rect: pygame.Rect = pause_title.get_rect(center=(WIDTH//2, 250)) ; screen.blit(pause_title, pause_title_rect)
    
    # Boutons du menu de pause
    pause_quitter: Bouton = Bouton(None, (WIDTH//2, 450), "QUITTER", MENU_BOUTON_FONT, "black", "White")
    pause_quitter.changeColor(pause_mouse_pos) ; pause_quitter.update(screen)
    
    pause_suivant: Bouton = Bouton(None, (WIDTH//2, 350), "SUIVANT", MENU_BOUTON_FONT, "black", "White")
    pause_suivant.changeColor(pause_mouse_pos) ; pause_suivant.update(screen)

    return pause_quitter, pause_suivant

def menuFinPartie(gagne: bool) -> tuple[Bouton, Bouton]:
    """
    Affiche le menu de fin de partie a l'ecran.
    :param gagne: (bool) victoire ou non
    :return: (Tuple) les boutons du menu
    """
    # Positionnement de la souris
    pause_mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
    
    # Fond du menu de pause
    pause_surface: pygame.Surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(pause_surface, (128, 128, 128, 150), [0, 0 ,WIDTH, HEIGHT]) ; screen.blit(pause_surface, (0,0))
    
    # Titre du menu selon victoire ou non
    if gagne:
        pause_title: pygame.Surface = TITRE_FONT.render("LES JOUEURS ONT GAGNES", True, (255, 255, 255))
        pause_title_rect: pygame.Rect = pause_title.get_rect(center=(WIDTH//2, 250)) ; screen.blit(pause_title, pause_title_rect)
    else:
        pause_title: pygame.Surface = TITRE_FONT.render("LES JOUEURS ONT PERDU", True, (255, 255, 255))
        pause_title_rect: pygame.Rect = pause_title.get_rect(center=(WIDTH//2, 250)) ; screen.blit(pause_title, pause_title_rect)
    
    # Boutons du menu de pause
    pause_quitter: Bouton = Bouton(None, (WIDTH//2, 450), "QUITTER", MENU_BOUTON_FONT, "black", "White")
    pause_quitter.changeColor(pause_mouse_pos) ; pause_quitter.update(screen)
    
    pause_recommencer: Bouton = Bouton(None, (WIDTH//2, 350), "RECOMMENCER", MENU_BOUTON_FONT, "black", "White")
    pause_recommencer.changeColor(pause_mouse_pos) ; pause_recommencer.update(screen)

    return pause_quitter, pause_recommencer

def lanceDe() -> int: return randint(1,6)

def auroreCapacite(plateau: Plateau, pers: Aurore, etape: int) -> int:
    """
    Renvoie les degats de la capacité du personnage Aurore
    :param plateau: (Plateau)
    :param pers: (Aurore)
    :param etape: (int)
    :return: (int)
    """
    degats: int = pers.lanceCapacite()

    # Vérification bonus de case
    if plateau.getCase(pers.getCaseNum()).getType() == 'B':
        degats += 3
    elif plateau.getCase(pers.getCaseNum()).getType() == 'M':
        degats -= 3
    
    # Verification bonus de lieu
    if pers.getType() == etape:
        degats += 2
    elif pers.getInverseType() == etape:
        degats -= 2

    # Verification degat minimal
    degats = degats if degats > 1 else 1 
    return degats

def akaneCapacite():
    pass

def lauraCapacite(plateau: Plateau, pers: Laura):
    mouse_pos = pygame.mouse.get_pos()

def attaqueCase(case: list[Personnage], ennemi: Ennemi, degat: int) -> None:
    """
    Attaque une case contenant un personnage.
    :param case: (list) Une liste de personnage
    :param ennemi: (Ennemi)
    :param degat: (int) les degats de l'ennemi
    :return: (None)
    :effet de bord: modifie les personnages de la case et l'ennemi optionnellement
    """
    # Pour tout les perso de la case
    for perso in case:
        # Verification que l'ennemi ne recoit pas de dégat renvoyé
        if isinstance(perso, Bob):
            ennemi.recevoirCoup(perso.recevoirCoup(degat))
        else: # Sinon attaquer le personnage
            perso.recevoirCoup(degat)

def boss1Attaque(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
    """
    Attaque une case contenant un personnage.
    :param plateau: (Plateau)
    :param ennemi: (Ennemi)
    :return: (tuple) le plateau et ennemi apres attaque
    :effet de bord: modifie les personnages plateau et l'ennemi optionnellement
    """
    # Degat envoyé sur un personnage
    degat: int = ennemi.lanceAttaque()
    perso_cible: Personnage = choice(plateau.getPersosPlateau())
    case_perso_cible: list[Personnage] = plateau.getPersosCase(perso_cible.getCaseNum())
    
    # Attaquer la case du personnage cible
    attaqueCase(case_perso_cible, ennemi, degat)
    
    return plateau, ennemi

def boss2Attaque(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
    """
    Attaque une case contenant un personnage et 5 cases au hasard.
    :param plateau: (Plateau)
    :param ennemi: (Ennemi)
    :return: (tuple) le plateau et ennemi apres attaque
    :effet de bord: modifie les personnages plateau et l'ennemi optionnellement
    """
    # Degat envoyé sur un personnage
    degat: int = ennemi.lanceAttaque()
    perso_cible: Personnage = choice(plateau.getPersosPlateau())
    case_perso_cible: list[Personnage] = plateau.getPersosCase(perso_cible.getCaseNum())
    
    # Attaquer la case du personnage cible
    attaqueCase(case_perso_cible, ennemi, degat)

    # Attaquer 5 cases au hasard
    for _ in range(4):
        # Récuperer une case au hasard
        num_case = randint(1, plateau.TAILLE)
        case = plateau.getCase(num_case)

        # Si la case contient des personnages et que le personnage cible n'est pas présent
        if case.getPersonnages() != []:
            if not perso_cible in case.getPersonnages():
                # Attaquer la case
                attaqueCase(case.getPersonnages(), ennemi, degat)

    return plateau, ennemi

def boss3Attaque(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
    """
    Attaque une case contenant un personnage et les cases a coté.
    :param plateau: (Plateau)
    :param ennemi: (Ennemi)
    :return: (tuple) le plateau et ennemi apres attaque
    :effet de bord: modifie les personnages plateau et l'ennemi optionnellement
    """
    # Degat envoyé sur un personnage
    degat: int = ennemi.lanceAttaque()
    perso_cible: Personnage = choice(plateau.getPersosPlateau())
    
    # Attaquer la case du personnage cible
    attaqueCase(plateau.getPersosCase(perso_cible.getCaseNum()), ennemi, degat)
    
    # Attaque la case de devant
    # Vérification case suivante dans le plateau
    if (perso_cible.getCaseNum() + 1) <= plateau.TAILLE:
        attaqueCase(plateau.getPersosCase(perso_cible.getCaseNum() + 1), ennemi, degat)
    else: # Sinon on reviens a la case 1
        attaqueCase(plateau.getPersosCase(1), ennemi, degat)
    
    # Attaque la case de derriere
    # Vérification case derriere dans le plateau
    if (perso_cible.getCaseNum() - 1) >= 1:
        attaqueCase(plateau.getPersosCase(perso_cible.getCaseNum() - 1), ennemi, degat)
    else: # Sinon on est a la case 16
        attaqueCase(plateau.getPersosCase(16), ennemi, degat)
    
    return plateau, ennemi

def boss4Attaque(plateau: Plateau, ennemi: Ennemi) -> tuple[Plateau, Ennemi]:
    """
    Attaque une case contenant un personnage cible et la case des autres personnages avec les dégats réduits.
    :param plateau: (Plateau)
    :param ennemi: (Ennemi)
    :return: (tuple) le plateau et ennemi apres attaque
    :effet de bord: modifie les personnages plateau et l'ennemi optionnellement
    """
    # Degat envoyé sur un personnage
    degat: int = ennemi.lanceAttaque()
    perso_cible: Personnage = choice(plateau.getPersosPlateau())
    case_perso_cible: list[Personnage] = plateau.getPersosCase(perso_cible.getCaseNum())
    
    # Liste des cases deja attaque
    num_cases_attaque: list[int] = [perso_cible.getCaseNum()]
    
    # Attaque la case du personnage cible
    attaqueCase(case_perso_cible, ennemi, degat)

    # Pour les autres personnages du plateau
    for perso in plateau.getPersosPlateau():
        if not isinstance(perso, type(perso_cible)):
            
            # Si la case n'a pas deja été attaqué
            if perso.getCaseNum() not in num_cases_attaque:
                num_cases_attaque.append(perso.getCaseNum())
                
                # Vérification que l'ennemi ne recoie pas des coup renvoyé
                if isinstance(perso, Bob):
                    ennemi.recevoirCoup(perso.recevoirCoup(round(degat*0.3)))
                else: perso.recevoirCoup(round(degat*0.3))

    return plateau, ennemi

def persoAJouer(pers: Personnage) -> None:
    """
    Remet tout les attributs de jeu d'un personnage a faux
    :param pers: (Personnage)
    :return: (None)
    """
    pers.deLancer = False
    pers.choixPossible = []
    pers.estDeplace = False
    pers.aJouer = False

def initPlateau(pers1: Personnage, pers2: Personnage, pers3: Personnage, pers4: Personnage) -> tuple[Plateau, list[Personnage]]:
    """
    Initialise le plateau en début de partie.
    :param pers1: (Personnage)
    :param pers2: (Personnage)
    :param pers3: (Personnage)
    :param pers4: (Personnage)
    :return: (tuple) le plateau et la liste des personnages
    """
    # Création du plateau avec bonus
    plateau: Plateau = Plateau() ; plateau.ajoutBonus()
    
    # Creation de la liste des personnage en jeu
    personnages: list[Personnage] = [pers1, pers2, pers3, pers4]
    
    # Place les personnages dans le plateau a leur position de depart
    plateau.placePerso(1, personnages[0])
    plateau.placePerso(5, personnages[1])
    plateau.placePerso(9, personnages[2])
    plateau.placePerso(13, personnages[3])
    
    return plateau, personnages


# ------------Partie lancé------------
def play() -> None:
    """Déroulement d'une partie."""
    # Condition de pause ou de fin de partie
    pause: bool = False
    pause_entre_boss: bool = False
    perdu: bool = False
    gagne: bool = False
    
    # Personnages en jeu
    aurore: Aurore = Aurore() ; akane: Akane = Akane() ; bob: Bob = Bob() ; laura: Laura = Laura()
    liste_perso: list[Personnage] = [aurore, akane, bob, laura]
    
    # Initialiser le plateau avec les personnages et les boss
    plateau, liste_perso_actif = initPlateau(aurore, akane, bob, laura)
    liste_ennemis: list[Ennemi] = [Boss1(), Boss2(), Boss3(), Boss4()]

    # Personnage actif
    perso_actif_indice: int = 0 ; perso_actif: Personnage = liste_perso_actif[perso_actif_indice]
    
    # Ennemis actuel
    ennemi_actuel: Ennemi = liste_ennemis[0]
    
    # Initialisation de la partie (num lieux/boss)
    etape: int = 1
    
    # Tant que la partie se joue
    while True:
        
        # Positionnement de la souris
        play_mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        
        # Fond de la fenêtre
        screen.blit(pygame.image.load(LISTE_LIEUX[etape]), (0, 0))
        
        # Afficher le plateau
        affichePlateau(plateau)
        
        # Affiche carte personnages
        afficheCartes(liste_perso, perso_actif, etape)
        
        # Affiche les ennemis
        afficheEnnemi(ennemi_actuel)
        
        # Boutons
        # Si le personnage n'est pas déplacé et n'a pas joué
        if (not perso_actif.estDeplace) and (not perso_actif.aJouer):
            lancer_de: Bouton = Bouton(BOUTON_CLIQUABLE, (496, 551), 'Lancer dé', BOUTON_FONT, 'black', 'black')
            lancer_attaque: Bouton = Bouton(BOUTON, (640, 551), 'Attaque', BOUTON_FONT, 'black', 'black')
            lancer_capacite: Bouton = Bouton(BOUTON, (784, 551), 'Capacité', BOUTON_FONT, 'black', 'black')

        # Sinon si déplacé et n'a pas joué
        elif perso_actif.estDeplace and (not perso_actif.aJouer):
            lancer_de: Bouton = Bouton(BOUTON, (496, 551), 'Lancer dé', BOUTON_FONT, 'black', 'black')
            lancer_attaque: Bouton = Bouton(BOUTON_CLIQUABLE, (640, 551), 'Attaque', BOUTON_FONT, 'black', 'black')
            
            # Si Bob, le bouton de capacité n'est pas jouable car capacité lancé automatiquement
            if isinstance(perso_actif, Bob):
                lancer_capacite: Bouton = Bouton(BOUTON, (784, 551), 'Capacité', BOUTON_FONT, 'black', 'black')
            
            # Si Akane et capacité lancé (en attente), bouton non cliquable
            elif isinstance(perso_actif, Akane) and perso_actif.capacite:
                lancer_capacite: Bouton = Bouton(BOUTON, (784, 551), 'Capacité', BOUTON_FONT, 'black', 'black')
            
            else: # Sinon bouton cliquable
                lancer_capacite: Bouton = Bouton(BOUTON_CLIQUABLE, (784, 551), 'Capacité', BOUTON_FONT, 'black', 'black')

        # Affiche les boutons a l'écran
        lancer_de.update(screen)
        lancer_attaque.update(screen)
        lancer_capacite.update(screen)

        # Condition spécial, personnage actif Laura et capacité en attente du choix du joueur        
        if isinstance(perso_actif, Laura):

            # Si le personnage n'a pas joué et que la capacité est lancé
            if not perso_actif.aJouer and perso_actif.capacite:
                # Bouton en attente que le joueur fasse un choix
                capacite_en_attente: Bouton = Bouton(BOUTON_EN_ATTENTE, (784, 551), 'Capacité', BOUTON_FONT, 'black', 'black') ; capacite_en_attente.update(screen)
                
                # Affichage des instructions
                instruction_capacite: pygame.Surface = JEU_FONT.render("Choisissez une case avec personnage(s)", True, "black") ; screen.blit(instruction_capacite, instruction_capacite.get_rect(center=(640, 510)))
                    
        # Afficher les choix possible si le dé est lancé
        if perso_actif.deLancer and not perso_actif.estDeplace:         
            perso_actif.choixPossible = [i+1 for i in range(val_de)]
            for cases_possible in perso_actif.choixPossible:
                indiceCase: int = (cases_possible + perso_actif.getCaseNum()) % 16
                if indiceCase == 0: indiceCase = 16
                screen.blit(CASE_CLIQUABLE, (RECT_CASES[indiceCase]))
        
        # Ennemi lance attaque si tout les joueurs ont joué
        if (perso_actif_indice == len(liste_perso_actif) - 1) and (perso_actif.aJouer) and not (ennemi_actuel.getPV() <= 0):
            if isinstance(ennemi_actuel, Boss1):
                plateau, ennemi_actuel = boss1Attaque(plateau, ennemi_actuel)
            
            if isinstance(ennemi_actuel, Boss2):
                plateau, ennemi_actuel = boss2Attaque(plateau, ennemi_actuel)
                
            if isinstance(ennemi_actuel, Boss3):
                plateau, ennemi_actuel = boss3Attaque(plateau, ennemi_actuel)
                
            if isinstance(ennemi_actuel, Boss4):
                plateau, ennemi_actuel = boss4Attaque(plateau, ennemi_actuel)

            
            # Apres attaque boss, verification si perso sans vie
            if plateau.getPersosPlateau() != []:
                for perso_plateau in plateau.getPersosPlateau():
                    if perso_plateau.getPV() == 0:
                        plateau.getCase(perso_plateau.getCaseNum()).enlevePersonnage(perso_plateau)
                        liste_perso_actif.remove(perso_plateau)
                        
                        if perso_plateau == perso_actif:
                            perso_actif_indice += 1

        if len(liste_perso_actif) == 0:
            perdu = True
            
        if len(liste_ennemis) == 0:
            gagne = True
        
        # Change d'ennemi si ennemi actuel vaincu
        if ennemi_actuel.getPV() <= 0 and (not pause_entre_boss):
            liste_ennemis.remove(ennemi_actuel)
            pause_entre_boss = True
        
        # remettre a 0 les valeurs de tour pour le prochain personnage
        if (perso_actif.aJouer) and (not perdu) and (not pause_entre_boss):
            perso_actif_indice = perso_actif_indice + 1
            if perso_actif_indice > len(liste_perso_actif) - 1:
                perso_actif_indice = 0
            
            # Si le personnage a plus de vie
            if liste_perso_actif[perso_actif_indice].getPV() == 0:
                perso_actif_indice += 1
            
            persoAJouer(perso_actif)
            perso_actif = liste_perso_actif[perso_actif_indice]
        
        # gestion des evenements
        for event in pygame.event.get():
            # Si on quitte la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Si on clique sur la souris (et non jeu en pause)
            if (event.type == pygame.MOUSEBUTTONDOWN) and not (pause or pause_entre_boss):
                
                # Vérification bouton lancé dé cliqué
                if checkForInput(lancer_de.rect, play_mouse_pos):
                    # Si personnage actif n'a pas lancé le dé, le faire
                    if not perso_actif.estDeplace:
                        val_de: int = lanceDe()
                        perso_actif.deLancer = True
                        
                # Verification bouton lancer attaque cliqué
                if checkForInput(lancer_attaque.rect, play_mouse_pos):
                    # Si le personnage actif n'a pas joué mais a lancé le dé
                    if not perso_actif.aJouer and perso_actif.estDeplace:
                        degats_attaque: int = perso_actif.lanceAttaque()
                        
                        # Vérification bonus de case
                        # Verification case bonus, on ajoute des degats
                        if plateau.getCase(perso_actif.getCaseNum()).getType() == 'B':
                            degats_attaque += 3
                        
                        # Sinon si case malus, retirer degats
                        elif plateau.getCase(perso_actif.getCaseNum()).getType() == 'M':
                            degats_attaque -= 3
                        
                        # Verification bonus de lieu
                        # Si lieu correspond au type du personnage, ajouter des degats
                        if perso_actif.getType() == etape:
                            degats_attaque += 2
                        
                        # Sinon si personnage a pas une bonne affinité au lieu, retirer degats
                        elif perso_actif.getInverseType() == etape:
                            degats_attaque -= 2
                        
                        # Vérifier degat minimal et lancer attaque
                        degats_attaque = degats_attaque if degats_attaque > 1 else 1
                        ennemi_actuel.recevoirCoup(degats_attaque) ; perso_actif.aJouer = True
                
                # Si bouton lancé capacité cliqué
                if checkForInput(lancer_capacite.rect, play_mouse_pos):
                    # Si le personnage n'a pas joué mais est déplacé
                    if not perso_actif.aJouer and perso_actif.estDeplace:

                        # Aurore (Attaque plus puissante)
                        if isinstance(perso_actif, Aurore):                            
                            degats_aurore = auroreCapacite(plateau, perso_actif, etape)
                            ennemi_actuel.recevoirCoup(degats_aurore) ; perso_actif.aJouer = True
                            
                        # Akane (Reduction degat)
                        if isinstance(perso_actif, Akane):
                            if not perso_actif.capacite:         
                                perso_actif.lanceCapacite()
                                perso_actif.aJouer = True
                            
                        # Laura (Soin)
                        if isinstance(perso_actif, Laura):
                            perso_actif.capacite = True
    
                # Si personnage Laura a lancé sa capacité
                if isinstance(perso_actif, Laura):
                    # Si pas joué mais capacité lancé
                    if not perso_actif.aJouer and perso_actif.capacite:
                        
                        # Verification pour toute les cases
                        for case in RECT_CASES:
                            # Si on clique sur une case
                            if checkForInput(RECT_CASES[case], play_mouse_pos):
                                case_avec_perso = False
                                
                                # Si la case ne contient pas de personnage
                                if not case_avec_perso:
                                    case_choisi = plateau.getPersosCase(case)
                                    # Si la case n'est pas vide (contient personnages), lancer la capacité sur les personnages de la case
                                    if case_choisi != []:
                                        for perso in case_choisi:
                                            perso_actif.lanceCapacite(perso)
                                            perso_actif.aJouer = True ; perso_actif.capacite = False
                
                # Si personnage a lancé le dé mais pas déplacé
                if perso_actif.deLancer and not perso_actif.estDeplace:
                    # Recuperer les cases de déplacement possible
                    for choix_de in perso_actif.choixPossible:
                        pers_case = choix_de + perso_actif.getCaseNum() % 16
                        if pers_case > 16: pers_case -= 16
                        
                        # Vérification qu'une case possible a été cliqué, si oui, déplacer le personnage a cette case
                        if checkForInput(RECT_CASES[pers_case], play_mouse_pos):
                            numDeplacement = choix_de ; perso_actif.estDeplace = True
                            plateau.deplacePerso(perso_actif, numDeplacement)

            # Si on appuie sur une touche du clavier
            if event.type == pygame.KEYDOWN:
                # Mettre a pause si on appuie sur echap
                if event.key == pygame.K_ESCAPE:
                    # Si on est deja en pause, retirer la pause
                    if pause:
                        pause = False
                    else: # Sinon mettre en pause
                        pause = True

        # Si on est en pause, mais pas en pause entre les etapes
        if pause and not pause_entre_boss:
            # Boutons du menu
            quitter, reprendre = menuPause()
            
            # Si on appuie sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si on appuie sur quitter, retour au menu principal
                if checkForInput(quitter.rect, play_mouse_pos):
                    main_menu()

                # Sinon si on appuie sur reprendre, ne plus mettre en pause
                if checkForInput(reprendre.rect, play_mouse_pos):
                    pause = False

        # Si pause entre les boss et qu'on est pas a la derniere etape
        if pause_entre_boss and not (etape == 4):
            # Boutons du menu
            quitter, suivant = menuBossSuivant()
            
            # Si on appuie sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si on appuie sur quitter, retour au menu principal
                if checkForInput(quitter.rect, play_mouse_pos):
                    main_menu()

                # Si on appuie sur suivant, on enleve la pause et on passe a la manche suivante
                if checkForInput(suivant.rect, play_mouse_pos):
                    pause_entre_boss = False
                    ennemi_actuel = liste_ennemis[0]
                    etape += 1
        
        # Si on a gagné ou perdu
        if perdu or gagne:
            # Boutons du menu
            quitter, recommencer = menuFinPartie(gagne)
            
            # Si on appuie sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si on appuie sur quitter, retour au menu principal
                if checkForInput(quitter.rect, play_mouse_pos):
                    main_menu()
                
                # Si on appuie sur recommencer, on relance une nouvelle partie
                if checkForInput(recommencer.rect, play_mouse_pos):
                    play()

        # Met a jour la fenetre
        pygame.display.update()


# ------------Menu sauvegarde------------
def sauvegarde() -> None:
    """Menu de sauvegarde"""
    # Tant qu'on est sur le menu sauvegarde
    while True:
        # Positionnement de la souris
        sauv_mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        # Remplir le fond
        screen.blit(MENU_BG, (0, 0))

        # Définition du titre
        game_title: pygame.Surface = MENU_TITRE_FONT.render("La Cité Academique", True, (255, 255, 255))
        game_title_rect: pygame.Rect = game_title.get_rect(center=(WIDTH//2, 100)) ; screen.blit(game_title, game_title_rect)
        
        # -----------------------------------------------------------------------------------------
        sauv_text = TITRE_FONT.render("Menu sauvegarde", True, "black")
        sauv_rect = sauv_text.get_rect(center=(640, 260)) ; screen.blit(sauv_text, sauv_rect)
        
        # Boutons
        sauv_back: Bouton = Bouton(None, (640, 460), 'Retour', MENU_BOUTON_FONT, 'black', 'white')
        sauv_back.changeColor(sauv_mouse_pos) ; sauv_back.update(screen)
        # -----------------------------------------------------------------------------------------
        
        # gestion des evenements
        for event in pygame.event.get():
            # Si on quitte, on quitte
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Si on clique sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if checkForInput(sauv_back.rect, sauv_mouse_pos):
                    main_menu()
        
        # Met a jour la fenetre
        pygame.display.update()


# ------------Menu extra------------
def extra() -> None:    
    # Tant qu'on est sur le menu sauvegarde
    while True:
        # Positionnement de la souris
        EXTRA_MOUSE_POS = pygame.mouse.get_pos()
        
        # Remplir le fond
        screen.blit(MENU_BG, (0, 0))
        
        # Titre menu
        GAME_TITLE = MENU_TITRE_FONT.render("La Cité Academique", True, (255, 255, 255))
        GAME_TITLE_RECT = GAME_TITLE.get_rect(center=(WIDTH//2, 100))
        screen.blit(GAME_TITLE, GAME_TITLE_RECT)
        
        # -----------------------------------------------------------------------------------------
        EXTRA_TEXT = TITRE_FONT.render("Menu extra", True, "black")
        EXTRA_RECT = EXTRA_TEXT.get_rect(center=(640, 260))
        screen.blit(EXTRA_TEXT, EXTRA_RECT)

        # Boutons
        EXTRA_BACK = Bouton(None, (640, 460), 'Retour', MENU_BOUTON_FONT, 'black', 'white')
        
        EXTRA_BACK.changeColor(EXTRA_MOUSE_POS)
        EXTRA_BACK.update(screen)
        # -----------------------------------------------------------------------------------------
        
        # gestion des evenements
        for event in pygame.event.get():
            # Si on quitte, on quitte
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Si on clique sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if checkForInput(EXTRA_BACK.rect, EXTRA_MOUSE_POS):
                    main_menu()
        
        # Met a jour la fenetre
        pygame.display.update()


# ------------Menu principal------------
def main_menu() -> None:
    """Menu principal du jeu."""
    # Tant que l'on est dans l'écran d'accueil
    while True:
        # Positionnement de la souris
        menu_mouse_pos: tuple[int,int] = pygame.mouse.get_pos()
        
        # Fond du menu
        screen.blit(MENU_BG, (0, 0))
        
        # Titre menu
        game_titre: pygame.Surface = MENU_TITRE_FONT.render("La Cité Academique", True, (255,255,255)) #(103, 214, 225)
        game_titre_rect: pygame.Rect = game_titre.get_rect(center=(WIDTH//2, 100)) ; screen.blit(game_titre, game_titre_rect)
        
        # Boutons
        play_bouton: Bouton = Bouton(MENU_BOUTON, (640, 250), "JOUER", MENU_BOUTON_FONT, "black", "White")
        saves_bouton: Bouton = Bouton(MENU_BOUTON, (640, 400), "SAUVEGARDE", MENU_BOUTON_FONT, "black", "White")
        quit_bouton: Bouton = Bouton(MENU_BOUTON, (640, 550), "QUITTER", MENU_BOUTON_FONT, "black", "White")
        extra_bouton: Bouton = Bouton(None, (1050, 600), "EXTRA", MENU_BOUTON_FONT, "black", "White")
        
        # Effet survol boutons
        for button in [play_bouton, saves_bouton, quit_bouton, extra_bouton]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
            
        # Gestion des evenements
        for event in pygame.event.get():
            # Si on quitte, on quitte
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Si on a cliqué quelque part avec la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if checkForInput(play_bouton.rect, menu_mouse_pos):
                    play()
                if checkForInput(saves_bouton.rect, menu_mouse_pos):
                    sauvegarde()
                if checkForInput(extra_bouton.rect, menu_mouse_pos):
                    extra()
                if checkForInput(quit_bouton.rect, menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Met à jour la page
        pygame.display.update()


# --------------------------------------------------------------
# Fonction principale, lancement du jeu
# --------------------------------------------------------------
if __name__ == "__main__":
    main_menu()