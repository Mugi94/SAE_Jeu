class Stats:
    def __init__(self):
        self.score = 0
        self.degats_totaux = 0 # C'est un attribut qui va servir à calculer les dégâts moyens
        self.degats_moyens = 0
        self.meilleur_personnage = None
        self.pire_personnage = None
        self.nb_attaques = 0 # Pour calculer les dégâts moyens, doit pas être retourner
        
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
    
    

