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
from random import choice, randrange
from pygame import Surface, image
from personnage import *
import os

# ----------------
# Constantes
# ----------------
CASE_NEUTRE = 'N'
CASE_BONUS = 'B'
CASE_MALUS = 'M'
CASES_BONUS = [CASE_BONUS, CASE_MALUS]

PATH = os.path.dirname(os.path.abspath(__file__))

# -------------------
# Classe Case
# -------------------
class Case:
    """Classe Case représentant une case du Plateau."""
    
    # Constructeur
    def __init__(self: Case, type_case: str = "N"):
        """
        Constructeur de la classe Case.
        :param self: (Case)
        :param type_case: (String)
        :return: (None)
        """
        # attributs
        self._type: str = type_case
        self._listePersonnages: list[Personnage] = []
        
        # définition de l'image de la case
        if type_case == "B": # Case bonus
            self._img: str = f"{PATH}/img/cases/case_bonus.png"
        if type_case == "M": # Case malus
            self._img: str = f"{PATH}/img/cases/case_malus.png"
        else: # Case neutre
            self._img: str = f"{PATH}/img/cases/case_neutre.png"
    
    # Getters et setters
    def getType(self: Case) -> str:
        """
        Retourne le type de la Case.
        :param self: (Case)
        :return: (String)
        """
        return self._type

    def getPersonnages(self: Case) -> list[Personnage]:
        """
        Retourne la liste des personnages présent sur la case.
        :param self: (Case)
        :return: (List) Une liste de personnage
        """
        return self._listePersonnages
    
    def getImg(self: Case) -> str:
        """
        Retourne le chemin de l'image de la case.
        :param self: (Case)
        :return: (str) Chemin menant à l'image
        """
        return self._img
    
    def placePersonnage(self: Case, pers: Personnage) -> None:
        """
        Place un personnage sur la case.
        :param self: (Case)
        :param pers: (Personnage)
        :return: (None)
        :effet de bord: Modifie l'attribut _listePersonnages
        """
        self._listePersonnages.append(pers)
    
    def enlevePersonnage(self: Case, pers: Personnage) -> None:
        """
        Retire un personnage sur la case.
        :param self: (Case)
        :param pers: (Personnage)
        :return: (None)
        :effet de bord: Modifie l'attribut _listePersonnages
        """
        self._listePersonnages.remove(pers)
    
    def __repr__(self: Case) -> str:
        """
        Renvoie une chaine de caractère représentant une case.
        :param self: (Case)
        :return: (String)
        """
        return f'{self._type} = {self._listePersonnages}'

# ---------------
# Classe Plateau
# ----------------
class Plateau:
    """Classe Plateau contenant des objets Case."""

    # Attributs statiques
    TAILLE = 16

    # Constructeur
    def __init__(self: Plateau):
        """
        Constructeur de la classe plateau, génère un plateau avec des cases neutres selon la taille donnée en attribut statique.
        :param self: (Plateau)
        :return: (None)
        """
        self._cases: list[Case] = [Case() for _ in range (Plateau.TAILLE)]

    # -------------Méthodes-------------
    def getCase(self: Plateau, numCase: int) -> Case:
        """
        Renvoie la case du plateau selon son numéro.
        :param self: (Plateau)
        :param numCase: (Int)
        :CU: numCase doit être de 1 à 20
        :return: (Case)
        """
        assert 0 < numCase <= 20, "numCase doit être de 1 à 20"
        return self._cases[numCase-1]
    
    def getPersosPlateau(self: Plateau) -> list[Personnage]:
        """
        Retourne une liste de tout les personnages présent sur le plateau
        :param self: (Plateau)
        :return: (List) Une liste de personnage
        """
        listePers: list[Personnage] = []
        for case in self._cases:
            if case.getPersonnages() != []:
                listePers += case.getPersonnages()
        return listePers
    
    def getPersosCase(self: Plateau, numCase: int) -> list[Personnage]:
        """
        Renvoie la liste des personnages présent sur une case du plateau.
        :param self: (Plateau)
        :param numCase: (Int) Le numéro de la case et pas l'indice: indice = 4 -> numCase = 5 
        :return: (List) Une liste de personnage
        """
        return self._cases[numCase-1].getPersonnages()

    def placePerso(self: Plateau, numCase: int, personnage: Personnage) -> None:
        """
        Place un personnage sur le plateau à la case donnée.
        :param self: (Plateau)
        :param numCase: (Int)
        :param personnage: (Personnage)
        :return: (None)
        :effet de bord: Modifie l'attribut _listePersonnages de la case dans _cases et _numCase de personnage
        """
        # Placer le personnage sur la case
        self.getCase(numCase).placePersonnage(personnage)
        # Mettre à jour le numéro de la case du personnage
        personnage.setNumCase(numCase)

    def deplacePerso(self: Plateau, pers: Personnage, nbCases: int) -> None:
        """
        Déplace un personnage dans le plateau selon un nombre de case donnée
        :param self: (Plateau)
        :param pers: (Personnage)
        :param nbCases: (Int)
        :return: (None)
        """ 
        # retirer le personnage de sa case actuelle
        self.getCase(pers.getCaseNum()).getPersonnages().remove(pers)

        # Si personnage dépace la derniere case du plateau (numCase + nmDeplace % 16 == 0)
        if (pers.getCaseNum() + nbCases) % Plateau.TAILLE == 0:
            self.placePerso(Plateau.TAILLE, pers)
        
        else:
            # le placer sur la nouvelle case
            self.placePerso((pers.getCaseNum() + nbCases) % Plateau.TAILLE, pers)

    def ajoutBonus(self: Plateau, bonus: int = 3, malus: int = 3) -> None:
        """
        Rempli les cases du plateau aléatoirement.
        :param self: (Plateau)
        :param bonus: (int) le nombre de bonus sur le plateau
        :param malus: (int) le nombre de malus sur le plateau
        :return: (None)
        :effet de bord: Modifie l'attribut _cases
        """
        maxBonus : int = bonus
        maxMalus : int = malus
        
        # Tant qu'on a pas placé tout les bonus
        while (maxBonus + maxMalus) > 0:
            # Générer un indice et une case aléatoire
            indice: int = randrange(Plateau.TAILLE)

            # Si la case est neutre
            if self._cases[indice].getType() == 'N':
                caseAlea: Case = Case(choice(CASES_BONUS))

                # Si caseAlea bonus
                if caseAlea.getType() == CASE_BONUS and (maxBonus > 0):
                    self._cases[indice] = caseAlea
                    maxBonus = maxBonus - 1

                # Sinon si caseAlea malus
                elif (maxMalus > 0) and caseAlea.getType() == CASE_MALUS:
                    self._cases[indice] = caseAlea
                    maxMalus = maxMalus - 1

    def reinitialiser(self: Plateau) -> None:
        """
        Réinitialise le plateau.
        :param self: (Plateau)
        :return: (None)
        :effet de bord: Modifie l'attribut _cases
        """
        self._cases = [Case() for _ in range(Plateau.TAILLE)]

    def __repr__(self: Plateau) -> str:
        """
        Renvoie une chaine de caractère représentant un plateau
        :param self: (Plateau)
        :return: (String)
        """
        rep: str = ""
        for i in range(Plateau.TAILLE):
            rep += str(self.getCase(i+1).getType()) + " - " + str(self.getCase(i+1).getPersonnages()) + " | "
        return rep

# ------------------
# Main de test
# ------------------
if __name__ == "__main__":
    aurore = Aurore()
    akane = Akane()
    
    print("-------Test classe Case-------")
    testCase1 : Case = Case(CASE_NEUTRE)
    testCase2 : Case = Case(CASE_BONUS)
    testCase3 : Case = Case(CASE_MALUS)

    print(f'Type case 1 : {testCase1.getType()}')
    print(f'Type case 2 : {testCase2.getType()}')
    print(f'Type case 3 : {testCase3.getType()}\n')

    print(f'Case 1 : {testCase1}')
    print(f'Case 2 : {testCase2}')
    print(f'Case 3 : {testCase3}\n')

    print(f'Chemin image testCase2 : {testCase2.getImg()}\n')

    testCase1.placePersonnage(aurore)
    testCase1.placePersonnage(akane)
    print('Ajout de Aurore et Akane dans testCase1')
    print(f'Dans testCase1, il y a : {testCase1.getPersonnages()}\n')
    print(f'Case 1 : {testCase1}\n')

    testCase1.enlevePersonnage(akane)

    print('Enlever Akane dans testCase1')
    print(f'Dans testCase1, il y a : {testCase1.getPersonnages()}')
    print(f'Case 1 : {testCase1}\n')

    print("-------Test classe Plateau-------")

    plateau : Plateau = Plateau()
    print(f'Le plateau est : {str(plateau)}')
    print(f'La case 5 est : {plateau.getCase(5)}\n')

    plateau.ajoutBonus()
    print('Ajout des bonus sur le plateau')
    print(f'Le plateau est : {str(plateau)}\n')
    
    print("Ajout de Aurore au plateau à la case 5 et akane case 7")
    plateau.placePerso(5, aurore)
    plateau.placePerso(7, akane)
    print(f'Le plateau est : {str(plateau)}')
    print(f'Case 5 : {plateau.getCase(5)}\n')
    
    print(f'Tout les personnages sur le plateau : {plateau.getPersosPlateau()}\n')
    print(f'Aurore se trouve case : {aurore.getCaseNum()}')
    print(f'Akane se trouve case : {akane.getCaseNum()}')
    
    plateau.deplacePerso(aurore, 2)
    print("Aurore s'est deplacé de 2 cases")
    print(f'Aurore se trouve case : {aurore.getCaseNum()}')
    print(f'Le plateau est : {str(plateau)}\n')
    
    plateau.reinitialiser()
    print(f'Plateau mit a 0 : {plateau}')