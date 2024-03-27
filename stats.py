import json
import os

class Stats:
    def __init__(self):
        self.score = 0
        self.degats_totaux = 0 # C'est un attribut qui va servir à calculer les dégâts moyens
        self.degats_moyens = 0
        self.meilleur_personnage = None
        self.pire_personnage = None
        self.nb_attaques = 0 # Pour calculer les dégâts moyens, doit pas être retourner
        self.degats_personnages = {
            "Akane Kagari": 0,
            "Aurore Thercieux": 0,
            "Bob Bob": 0,
            "Dr. Eliza de Minerve": 0,
            "Erika Nishimura": 0,
            "Laura Occideum": 0,
            "William Occideum": 0
            } # Dictionnaire qui va contenir les dégâts de chaque personnage
        
    # Getters
        
    def getStats(self):
        # On retourne les stats sous forme de dictionnaire pour pouvoir les afficher
        return {
            "score": self.score,
            "degats_moyens": self.degats_moyens,
            "degats_totaux": self.degats_totaux,
            "meilleur_personnage": self.meilleur_personnage,
            "pire_personnage": self.pire_personnage,
            "nb_attaques": self.nb_attaques,
            "degats_personnages": self.degats_personnages
        }
        
    def exportStats(self):
        """Exporte en JSON les stats pour les sauvegarder dans un fichier
        """
        stats = self.getStats()
        with open("stats.json", "w") as stats_file:
            json.dump(stats, stats_file)
    

    def importStats(self, stats):
        """Importe les stats depuis un fichier JSON"""
        with open(stats, "r") as stats_file:
            stats_data = json.load(stats_file)  # Use json.load() instead of json.loads()
        self.score = stats_data["score"]
        self.degats_moyens = stats_data["degats_moyens"]
        self.degats_totaux = stats_data["degats_totaux"]
        self.meilleur_personnage = stats_data["meilleur_personnage"]
        self.pire_personnage = stats_data["pire_personnage"]
        self.degats_personnages = stats_data["degats_personnages"]
        self.nb_attaques = stats_data["nb_attaques"]
        
    def resetStats(self):
        if os.path.exists("stats.json"):
            os.remove("stats.json")
        self.score = 0
        self.degats_totaux = 0
        self.degats_moyens = 0
        self.meilleur_personnage = None
        self.pire_personnage = None
        self.nb_attaques = 0
        self.degats_personnages = {
            "Akane Kagari": 0,
            "Aurore Thercieux": 0,
            "Bob Bob": 0,
            "Dr. Eliza de Minerve": 0,
            "Erika Nishimura": 0,
            "Laura Occideum": 0,
            "William Occideum": 0
            }
        

        
        
        
    # Setters // Ça va être long et chiant
    
    def setScore(self, score):
        self.score = score
        
    def addScore(self, score):
        self.score += score
        
    def setDegatsMoyens(self, degats_moyens):
        self.degats_moyens = degats_moyens
        
    def calculDegatsMoyens(self):
        self.degats_moyens = self.degats_totaux / self.nb_attaques
        
    def addDegatsTotaux(self, degats):
        self.degats_totaux += degats
        self.nb_attaques += 1
        self.calculDegatsMoyens()
        self.addScore(degats) 
        
    def setMeilleurPersonnage(self, meilleur_personnage): # On va devoir faire un truc pour comparer les personnages
        self.meilleur_personnage = meilleur_personnage
        
    def setPirePersonnage(self, pire_personnage): # On va devoir faire un truc pour comparer les personnages
        self.pire_personnage = pire_personnage
    
    def BestWorstCharacter(self):
        """Fonction qui va permettre de déterminer le meilleur et le pire personnage en fonction des dégâts qu'ils ont infligés"""
        self.meilleur_personnage = max(self.degats_personnages, key=self.degats_personnages.get)
        self.pire_personnage = min(self.degats_personnages, key=self.degats_personnages.get)
        
    def addDegatsPersonnages(self, personnage, degats):
        self.degats_personnages[personnage] += degats
        self.BestWorstCharacter()
        
    
    

