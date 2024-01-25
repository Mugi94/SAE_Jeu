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
import os

PATH = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------
# Classe Personnage pour les joueurs
# ----------------------------------
class Personnage:
    """Super classe Personnage qui sera hérité, elle déclare les attributs et méthodes communes"""
    
    # Constructeur
    def __init__(self: Personnage):
        """
        Constructeur de la classe Personnage, déclare les attributs d'un personnage.
        :param self: (Personnage)
        :return: (None)
        """
        self._nom: str
        self._PV: int = 100
        self._attaque: int
        self._defense: int
        self._typePers: int
        self._typeInversePers: int
        self._carte: str
        self._carteTour: str
        self._img: str
        self._numCase: int | None = None
        
        # Attributs public pour savoir l'etat du personnage dans le jeu
        self.deLancer: bool = False
        self.choixPossible: list[int] = []
        self.estDeplace: bool = False
        self.aJouer: bool = False

    # -------------Méthodes-------------
    def getNom(self: Personnage) -> str:
        """
        Retourne le nom d'un personnage.
        :param self: (Personnage)
        :return: (String)
        """
        return self._nom

    def getPV(self: Personnage) -> int:
        """
        Retourne les points de vie d'un personnage.
        :param self: (Personnage)
        :return: (Int)
        """
        return self._PV
    
    def getATK(self: Personnage) -> int:
        """
        Retourne l'attaque d'un personnage.
        :param self: (Personnage)
        :return: (int)
        """
        return self._attaque
    
    def getDEF(self: Personnage) -> int:
        """
        Retourne la défense d'un personnage.
        :param self: (Personnage)
        :return: (int)
        """
        return self._defense
    
    def getType(self: Personnage) -> int:
        """
        Retourne le type d'un personnage.
        :param self: (Personnage)
        :return: (int)
        """
        return self._typePers
    
    def getInverseType(self: Personnage) -> int:
        """
        Retourne le type inverse d'un personnage.
        :param self: (Personnage)
        :return: (int)
        """
        return self._typeInversePers

    def getCarte(self: Personnage) -> str:
        """
        Renvoie le chemin de la carte du personnage.
        :param self: (Personnage)
        :return: (None)
        """
        return self._carte
    
    def getImg(self: Personnage) -> str:
        """
        Renvoie le chemin de l'image en jeu du personnage.
        :param self: (Personnage)
        :return: (String)
        """
        return self._img
    
    def getCaseNum(self: Personnage) -> int | None:
        """
        Renvoie le numéro de la case actuelle du personnage
        :param self: (Personnage)
        :return: (Int)
        """
        return self._numCase
    
    def setNumCase(self: Personnage, numCase: int) -> None:
        """
        Change le numéro de case du personnage
        :param self: (Personnage)
        :param numCase: (int)
        :return: (None)
        :effet de bord: Modifie _numCase
        """
        self._numCase = numCase
    
    def recevoirCoup(self: Personnage, dgts: int):
        """
        Retire les points de vie d'un personnage selon les dégâts subits et sa défense.
        :param self: (Personnage)
        :param dgts: (Int)
        :return: (None)
        :effet de bord: Modifie l'attribut _PV
        """
        degat = round(dgts - (self._defense / 2))
        degat = degat if degat >= 3 else 3
        self._PV -= degat
        if self._PV < 0: self._PV = 0
            
    
    def lanceAttaque(self: Personnage) -> int:
        """
        Renvoie les dégâts envoyé par un personnage.
        :param self: (Personnage)
        :return: (Int)
        """
        return self._attaque
    
    def __repr__(self: Personnage) -> str:
        """
        Renvoie une chaine de caractère qui représente un personnage.
        :param self: (Personnage)
        :return: (String)
        """
        return str(self._nom)


# -----------------------Création personnages/ennemis-------------------------------




# ------------------
# Main de test
# ------------------
# if __name__ == "__main__":
    
#     print('---------Test Aurore---------')
#     aurore : Aurore = Aurore()
#     print(aurore)
#     print(aurore.getNom())
#     print(f'PV = {aurore.getPV()}')
#     print(f'typePers = {aurore.getType()}')
#     print(aurore.getCarte())
#     print(f'case num : {aurore.getCaseNum()}\n')
    
#     print('---------Test Akane---------')
#     akane : Akane = Akane()
#     print(akane)
#     print(akane.getNom())
#     print(f'PV = {akane.getPV()}')
#     print(f'typePers = {akane.getType()}')
#     print(akane.getCarte())
#     print(f'case num : {akane.getCaseNum()}\n')
    
#     print('---------Test Laura---------')
#     laura : Laura = Laura()
#     print(laura)
#     print(laura.getNom())
#     print(f'PV = {laura.getPV()}')
#     print(f'typePers = {laura.getType()}')
#     print(laura.getCarte())
#     print(f'case num : {laura.getCaseNum()}\n')
    
#     print('---------Test Bob---------')
#     bob : Bob = Bob()
#     print(bob)
#     print(bob.getNom())
#     print(f'PV = {bob.getPV()}')
#     print(f'typePers = {bob.getType()}')
#     print(bob.getCarte())
#     print(f'case num : {bob.getCaseNum()}\n')
    
#     print('---------Test attaque/compétences---------')

#     print(f'Aurore lance une attaque de : {str(aurore.lanceAttaque())}')
#     print(f'Aurore lance une capacite : dgts={str(aurore.lanceCapacite())}')
#     aurore.recevoirCoup(9)
#     print(f'Aurore recoie une attaque de 9 : PV={aurore.getPV()}')
#     laura.lanceCapacite(aurore)
#     print(f'Laura a soigné aurore, elle a désormait {aurore.getPV()}PV')
    
#     print(f'Bob recoie un coup de 10 et renvoie la moitié des dégâts : dgtsRenvoie={bob.recevoirCoup(10)} / PV={bob.getPV()}')
    
#     akane.recevoirCoup(10)
#     print(f'Akane recoie un coup de 10 sans capacite : PV={akane.getPV()}')
    
#     akane._PV = 100
#     akane.lanceCapacite()
#     akane.recevoirCoup(10)
#     print(f'Akane recoie un coup de 10 avec capacite : PV={akane.getPV()}')