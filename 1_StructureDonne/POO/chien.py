class Chien:
    def __init__(self, nom, poids):
        self.nom = nom
        self.poids = poids

    def donne_nom(self):
        return self.nom

    def donne_poids(self):
        return self.poids

    def machouille(self, jouet):
        resultat = ""
        for i in range(len(jouet) - 1):
            resultat += jouet[i]
        return resultat

    def aboie(self, quantite):
        son: str = "Ouaf"    
        return son * quantite 

    def mange(self, ration):
        if 0 < ration <= (self.poids / 10):
            self.poids += ration
            return True
        else:
            return False

# Tests

medor = Chien('Médor', 12.0)
assert medor.donne_nom() == 'Médor'
assert medor.donne_poids() == 12.0
assert medor.machouille('bâton') == 'bâto'
assert medor.aboie(3) == 'OuafOuafOuaf'
assert medor.mange(2.0) is False
assert medor.mange(1.0) is True
assert medor.donne_poids() == 13.0
assert medor.mange(1.3) is True
