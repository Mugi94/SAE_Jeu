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
from pygame import Surface, Rect
from pygame.font import Font

# -------------------
# Classe Bouton
# -------------------
class Bouton:
    """Classe permettant de créer un bouton sur un ecran"""

    # Constructeur
    def __init__(self: Bouton, img: Surface, pos: tuple[int,int], text_input: str, font: Font, color: str, hover_color: str):
        """
        Constructeur de la classe Bouton.
        :param self: (Bouton)
        :param img: (Surface)
        :param pos: (tuple) coordonnées de la forme (x,y)
        :param text_input: (String)
        :param font: (Font)
        :param color: (String)
        :param hover_color: (String)
        :return: (None)
        """
        
        # Attributs
        self._image: str | None = img
        self._x: int = pos[0]
        self._y: int = pos[1]
        self._text_input: str = text_input
        self._font: Font = font
        self._color: str = color
        self._text: Surface = self._font.render(self._text_input, True, self._color)
        self._hover_color: str = hover_color
        
        # Si on a pas d'image, le texte le deviens
        if self._image is None:
            self._image = self._text
        
        self._rect: Rect = self._image.get_rect(center=(self._x, self._y))
        self._text_rect: Rect = self._text.get_rect(center=(self._x, self._y))

    # Getter
    @property
    def rect(self: Bouton) -> Rect:
        """
        Getter de _rect, renvoie l'attribut rect.
        :param self: (Bouton)
        :return: (Rect)
        """
        return self._rect

    # Methodes
    # Mise a jour du bouton
    def update(self: Bouton, screen: Surface) -> None:
        """
        Met a jour le bouton sur l'ecran.
        :param self: (Bouton)
        :param screen: (Surface) l'ecran du jeu
        :return: (None)
        """
        if self._image is not None:
            screen.blit(self._image, self._rect)
            screen.blit(self._text, self._text_rect)


    # Changement de couleur au survol
    def changeColor(self: Bouton, position: tuple[int,int]) -> None:
        """
        Change la couleur du texte au survol du bouton.
        :param self: (Bouton)
        :param position: (tuple) coordonnées de la forme (x,y)
        :return: (String)
        """
        # Si le texte est survolé, le mettre a la couleur du survol
        if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
            self._text = self._font.render(self._text_input, True, self._hover_color)
        
        # Sinon le texte est de la couleur d'origine
        else:
            self._text = self._font.render(self._text_input, True, self._color)