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
    """Classe permettant de créer un bouton sur un écran"""

    def __init__(self: Bouton,
                 img: Surface,
                 pos: tuple[int,int],
                 text_input: str,
                 font: Font,
                 color: str,
                 hover_color: str):
        """Constructeur de la classe Bouton"""
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


    # --------- Getters / Setters ---------
    @property
    def rect(self: Bouton) -> Rect: return self._rect
    # ------------------------------------

    def update(self: Bouton, screen: Surface) -> None:
        """Met a jour le bouton"""
        if self._image is not None:
            screen.blit(self._image, self._rect)
            screen.blit(self._text, self._text_rect)

    def checkForInput(self: Bouton, position: tuple[int, int]) -> bool:
        """Vérifie si la souris est sur le bouton"""
        return (position[0] in range(self._rect.left, self._rect.right)) and (position[1] in range(self._rect.top, self._rect.bottom))
    
    def changeColor(self: Bouton, position: tuple[int,int]) -> None:
        """Change la couleur du texte au survol"""
        if self.checkForInput(position):
            self._text = self._font.render(self._text_input, True, self._hover_color)
        else:
            self._text = self._font.render(self._text_input, True, self._color)