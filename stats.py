import json

class Stats:
    def __init__(self):
        self.score = 0
        self.degats_totaux = 0 # C'est un attribut qui va servir à calculer les dégâts moyens
        self.degats_moyens = 0
        self.meilleur_personnage = None
        self.pire_personnage = None
        self.nb_attaques = 0 # Pour calculer les dégâts moyens, doit pas être retourner
        self.degats_personnages = {
            Akane: 0,
            Aurore: 0,
            Bob: 0,
            Laura: 0
            } # Dictionnaire qui va contenir les dégâts de chaque personnage
        
    # Getters
        
    def getStats(self):
        # On retourne les stats sous forme de dictionnaire pour pouvoir les afficher
        return {
            "score": self.score,
            "degats_moyens": self.degats_moyens,
            "degats_totaux": self.degats_totaux,
            "meilleur_personnage": self.meilleur_personnage,
            "pire_personnage": self.pire_personnage
        }
        
    def exportStats(self):
        """Exporte en JSON les stats pour les sauvegarder dans un fichier
        """
        stats = self.getStats()
        return json.dumps(stats)
    
    def importStats(self, stats):
        """Importe les stats depuis un fichier JSON
        """
        stats = json.loads(stats)
        self.score = stats["score"]
        self.degats_moyens = stats["degats_moyens"]
        self.degats_totaux = stats["degats_totaux"]
        self.meilleur_personnage = stats["meilleur_personnage"]
        self.pire_personnage = stats["pire_personnage"]
        
        
        
    # Setters // Ça va être long et chiant
    
    def setScore(self, score):
        self.score = score
        
    def setDegatsMoyens(self, degats_moyens):
        self.degats_moyens = degats_moyens
        
    def addDegatsTotaux(self, degats):
        self.degats_totaux += degats
        self.nb_attaques += 1
        
    def calculDegatsMoyens(self, degats):
        self.degats_moyens = self.degats_total / self.nb_attaques
        
    def setMeilleurPersonnage(self, meilleur_personnage): # On va devoir faire un truc pour comparer les personnages
        self.meilleur_personnage = meilleur_personnage
        
    def setPirePersonnage(self, pire_personnage): # On va devoir faire un truc pour comparer les personnages
        self.pire_personnage = pire_personnage
        
    def addDegatsPersonnages(self, personnage, degats):
        self.degats_personnages[personnage] += degats
        
    def BestWorstCharacter(self):
        """Fonction qui va permettre de déterminer le meilleur et le pire personnage en fonction des dégâts qu'ils ont infligés"""
        self.meilleur_personnage = max(self.degats_personnages, key=self.degats_personnages.get)
        self.pire_personnage = min(self.degats_personnages, key=self.degats_personnages.get)
        
    
    

