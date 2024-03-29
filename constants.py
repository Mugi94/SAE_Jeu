import os

# Current directory
PATH = os.path.dirname(os.path.abspath(__file__))


# Screen resolution
WIDTH, HEIGHT = 1280, 720


# Path to the game's backgrounds
MENU_BG = f"{PATH}/img/menu/menu_principal.jpg"
MENU_PERSONNAGE = f"{PATH}/img/menu/menu_personnage.jpg"
MENU_LANCEMENT = f"{PATH}/img/menu/menu_lancement.jpg"

STAGES = {
    1: f"{PATH}/img/lieux/ruelles.jpg",
    2: f"{PATH}/img/lieux/ruines.jpg",
    3: f"{PATH}/img/lieux/aeroport.jpg",
    4: f"{PATH}/img/lieux/sous-terrain.jpg"
}


# Path to the squares on the board
NEUTRE = f"{PATH}/img/cases/case_neutre.png"
BONUS = f"{PATH}/img/cases/case_bonus.png"
MALUS = f"{PATH}/img/cases/case_malus.png"
CASE_CLIQUABLE = f"{PATH}/img/cases/case_cliquable.png"


# Path to the affinities' logos 
LIEU_CONTENT = f"{PATH}/img/lieux/lieucontent.png"
LIEU_NEUTRE = f"{PATH}/img/lieux/lieuneutre.png"
LIEU_PAS_CONTENT = f"{PATH}/img/lieux/lieupascontent.png"


# Path to the buttons' images
MENU_BUTTON = f"{PATH}/img/boutons/bouton_menu.png"
BOUTON = f"{PATH}/img/boutons/jeubouton.png"
BOUTON_CLIQUABLE = f"{PATH}/img/boutons/jeuboutoncliquable.png"
BOUTON_EN_ATTENTE = f"{PATH}/img/boutons/jeuboutonattente.png"

BOUTON_SUIVANT = f"{PATH}/img/boutons/choix_suivant.png"
BOUTON_PRECEDENT = f"{PATH}/img/boutons/choix_precedent.png"

# Path to the imported fonts
DEMOCRATICA_BOLD = f'{PATH}/fonts/Democratica Bold.ttf'