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

# --------------
# Classe Ennemis
# --------------
class Ennemi:
    """Classe Ennemi"""
    def __init__(self: Ennemi):
        """
        Constructeur de la classe Ennemi, déclare les attributs.
        :param self: (Ennemi)
        :return: (None)
        """
        self._PV: int
        self._attaque: int = 10
        self._defense: int = 10
        self._img: str

    def getPV(self: Ennemi) -> int:
        """
        Renvoie les points de vie d'un ennemi.
        :param self: (Ennemi)
        :return: (int)
        """
        return self._PV

    def getATK(self: Ennemi) -> int:
        """
        Renvoie l'attaque d'un ennemi.
        :param self: (Ennemi)
        :return: (int)
        """
        return self._attaque
    
    def getImg(self: Ennemi) -> str:
        """
        Renvoie le chemin de l'image d'un ennemi.
        :param self: (Ennemi)
        :return: (String)
        """
        return self._img
    
    def recevoirCoup(self: Ennemi, dgts: int) -> None:
        """
        Recoie un coup selon les degats subits.
        :param self: (Ennemi)
        :param dgts: (int)
        :return: (None)
        :effet de bord: modifie _PV et lance une autre methode
        """
        degat = round(dgts - (self._defense / 2))
        degat = degat if degat >= 1 else 1
        self._PV -= degat
        if self._PV < 0: self._PV = 0

# -----------------------Création personnages/ennemis-------------------------------

# ------------------
# Personnage Aurore
# ------------------
class Aurore(Personnage):
    """Classe Aurore, sous classe de Personnage"""
    
    # Constructeur
    def __init__(self: Aurore):
        """
        Constructeur de la classe Aurore, initialise les attributs.
        :param self: (Aurore)
        :return: (None)
        """
        super().__init__()
        self._nom = "Aurore Thercieux"
        self._attaque = 10
        self._defense = 6
        self._typePers = 2
        self._typeInversePers = 3
        self._carte = f"{PATH}/img/personnages/aurore/aurorecarte.png"
        self._img = f"{PATH}/img/personnages/aurore/auroreimg.png"

    # -------------Méthodes-------------
    def lanceCapacite(self: Aurore) -> int:
        """
        Renvoie les dégâts envoyé de la compétence du personnage.
        :param self: (Aurore)
        :return: (int)
        """
        return round(self._attaque + (self._attaque/2))

# -----------------
# Personnage Akane
# -----------------
class Akane(Personnage):
    """Classe Akane, sous classe de Personnage"""
    
    # Constructeur
    def __init__(self: Akane):
        """
        Constructeur de la classe Akane, initialise les attributs.
        :param self: (Akane)
        :return: (None)
        """
        super().__init__()
        self._nom = "Akane Kagari"
        self._attaque = 8
        self._defense = 4
        self._typePers = 1
        self._typeInversePers = 4
        self._carte = f"{PATH}/img/personnages/akane/akanecarte.png"
        self._img = f"{PATH}/img/personnages/akane/akaneimg.png"
        self.capacite: bool = False

    # -------------Méthodes-------------
    def recevoirCoup(self: Akane, dgts: int) -> None:
        """
        Recoie un coup et lance la capacité automatiquement
        :param self: (Bob)
        :param dgts: (int)
        :return: (None)
        :effet de bord: modifie _PV et lance une autre methode
        """
        degat = round(dgts - (self._defense / 2))
        degat = degat if degat >= 3 else 3
        if self.capacite:
            self._PV -= degat
            self.capacite = False
        else:
            self._PV -= degat
        if self._PV < 0: self._PV = 0
    
    def lanceCapacite(self: Akane) -> None:
        """
        Réduit les dégats du prochain coup reçu.
        :param self: (Akane)
        :return: (None)
        """
        self.capacite = True

# -----------------
# Personnage Laura
# -----------------
class Laura(Personnage):
    """Classe Laura, sous classe de Personnage"""
    
    # Constructeur
    def __init__(self: Laura):
        """
        Constructeur de la classe Laura, initialise les attributs.
        :param self: (Laura)
        :return: (None)
        """
        super().__init__()
        self._nom = "Laura Occideum"
        self._attaque = 4
        self._defense = 7
        self._typePers = 3
        self._typeInversePers = 1
        self._carte = f"{PATH}/img/personnages/laura/lauracarte.png"
        self._img = f"{PATH}/img/personnages/laura/lauraimg.png"
        self.capacite: bool = False
    
    # -------------Méthodes-------------
    def lanceCapacite(self: Laura, pers: Personnage) -> None:
        pers._PV += 20
        if pers.getPV() > 100:
            pers._PV = 100

# ---------------
# Personnage Bob
# ---------------
class Bob(Personnage):
    """Classe Bob, sous classe de Personnage"""
    
    # Constructeur
    def __init__(self: Bob):
        """
        Constructeur de la classe Bob, initialise les attributs.
        :param self: (Bob)
        :return: (None)
        """
        super().__init__()
        self._nom = "Bob bob"
        self._attaque = 3   
        self._defense = 9
        self._typePers = 4
        self._typeInversePers = 2
        self._carte = f"{PATH}/img/personnages/bob/bobcarte.png"
        self._img = f"{PATH}/img/personnages/bob/bobimg.png"
    
    # -------------Méthodes-------------
    def recevoirCoup(self: Bob, dgts: int) -> int:
        """
        Recoie un coup et lance la capacité automatiquement
        :param self: (Bob)
        :param dgts: (int)
        :return: (int)
        :effet de bord: modifie _PV et lance une autre methode
        """
        degat = round(dgts - (self._defense / 2))
        degat = degat if degat >= 3 else 3
        self._PV = self._PV - degat
        if self._PV < 0: self._PV = 0
        return self.lanceCapacite(dgts)

    def lanceCapacite(self: Bob, dgts: int) -> int:
        """
        Renvoie les dégâts subit.
        :param self: (Bob)
        :param dgts: (int) les dégâts subit
        :return: (int)
        """
        return dgts


class Boss1(Ennemi):
    """Class Boss1, le premier Ennemi"""
    
    # Constructeur
    def __init__(self: Boss1):
        """
        Constructeur de la classe Boss1, déclare les attributs.
        :param self: (Boss1)
        :return: (None)
        """
        super().__init__()
        self._PV = 300
        self._img = f"{PATH}/img/ennemi/boss1.png"
        
    def lanceAttaque(self: Boss1) -> int:
        """
        Lance une attaque propre au Boss1
        :param self: (Boss1)
        :return: (int)
        """
        return self._attaque

class Boss2(Ennemi):
    """Class Boss2, le premier Ennemi"""
    
    # Constructeur
    def __init__(self: Boss2):
        """
        Constructeur de la classe Boss2, déclare les attributs.
        :param self: (Boss2)
        :return: (None)
        """
        super().__init__()
        self._PV = 325
        self._img = f"{PATH}/img/ennemi/boss2.png"
        
    def lanceAttaque(self: Boss2) -> int:
        """
        Lance une attaque propre au Boss2
        :param self: (Boss2)
        :return: (int)
        """
        return self._attaque

class Boss3(Ennemi):
    """Class Boss3, le premier Ennemi"""
    
    # Constructeur
    def __init__(self: Boss3):
        """
        Constructeur de la classe Boss3, déclare les attributs.
        :param self: (Boss3)
        :return: (None)
        """
        super().__init__()
        self._PV = 350
        self._img = f"{PATH}/img/ennemi/boss3.png"
        
    def lanceAttaque(self: Boss3) -> int:
        """
        Lance une attaque propre au Boss3
        :param self: (Boss3)
        :return: (int)
        """
        return self._attaque

class Boss4(Ennemi):
    """Class Boss1, le premier Ennemi"""
    
    # Constructeur
    def __init__(self: Boss4):
        """
        Constructeur de la classe Boss4, déclare les attributs.
        :param self: (Boss4)
        :return: (None)
        """
        super().__init__()
        self._PV = 400
        self._img = f"{PATH}/img/ennemi/boss4.png"
        
    def lanceAttaque(self: Boss4) -> int:
        """
        Lance une attaque propre au Boss4
        :param self: (Boss4)
        :return: (int)
        """
        return self._attaque

# ------------------
# Main de test
# ------------------
if __name__ == "__main__":
    
    print('---------Test Aurore---------')
    aurore : Aurore = Aurore()
    print(aurore)
    print(aurore.getNom())
    print(f'PV = {aurore.getPV()}')
    print(f'typePers = {aurore.getType()}')
    print(aurore.getCarte())
    print(f'case num : {aurore.getCaseNum()}\n')
    
    print('---------Test Akane---------')
    akane : Akane = Akane()
    print(akane)
    print(akane.getNom())
    print(f'PV = {akane.getPV()}')
    print(f'typePers = {akane.getType()}')
    print(akane.getCarte())
    print(f'case num : {akane.getCaseNum()}\n')
    
    print('---------Test Laura---------')
    laura : Laura = Laura()
    print(laura)
    print(laura.getNom())
    print(f'PV = {laura.getPV()}')
    print(f'typePers = {laura.getType()}')
    print(laura.getCarte())
    print(f'case num : {laura.getCaseNum()}\n')
    
    print('---------Test Bob---------')
    bob : Bob = Bob()
    print(bob)
    print(bob.getNom())
    print(f'PV = {bob.getPV()}')
    print(f'typePers = {bob.getType()}')
    print(bob.getCarte())
    print(f'case num : {bob.getCaseNum()}\n')
    
    print('---------Test attaque/compétences---------')

    print(f'Aurore lance une attaque de : {str(aurore.lanceAttaque())}')
    print(f'Aurore lance une capacite : dgts={str(aurore.lanceCapacite())}')
    aurore.recevoirCoup(9)
    print(f'Aurore recoie une attaque de 9 : PV={aurore.getPV()}')
    laura.lanceCapacite(aurore)
    print(f'Laura a soigné aurore, elle a désormait {aurore.getPV()}PV')
    
    print(f'Bob recoie un coup de 10 et renvoie la moitié des dégâts : dgtsRenvoie={bob.recevoirCoup(10)} / PV={bob.getPV()}')
    
    akane.recevoirCoup(10)
    print(f'Akane recoie un coup de 10 sans capacite : PV={akane.getPV()}')
    
    akane._PV = 100
    akane.lanceCapacite()
    akane.recevoirCoup(10)
    print(f'Akane recoie un coup de 10 avec capacite : PV={akane.getPV()}')