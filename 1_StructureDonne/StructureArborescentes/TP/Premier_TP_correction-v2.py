# -*- coding: utf-8 -*-

class Noeud:
    
    def __init__(self, value:str):
        self.valeur = value
        self.sag = None
        self.sad = None
        
    def insert_gauche(self, noeud):
    """Insère un noeud dans le sous-arbre gauche"""
        if self.sag == None:
            self.sag = noeud
        else:
            noeud.sag = self.sag
            self.sag = noeud
            
    def insert_droit(self, noeud):
    """Insère un noeud dans le sous-arbre droit"""
        if self.sad == None:
            self.sad = noeud
        else:
            noeud.sad = self.sad
            self.sad = noeud
            
    def get_valeur(self):
        return self.valeur
    
    def get_ssa_gauche(self):
        return self.sag
    
    def get_ssa_droit(self):
        return self.sad
    
    
    
def affiche(arbre):
    if arbre != None:
        return (arbre.get_valeur(), affiche(arbre.get_ssa_gauche()), affiche(arbre.get_ssa_droit()))
    
#-------------------------- Arbre 1 -----------------------------------#    
n0 = Noeud(8)
n1 = Noeud(4)
n2 = Noeud(12)
n3 = Noeud(3)
n4 = Noeud(6)
n5 = Noeud(9)
n6 = Noeud(14)

# Construction de la racine
arbre1 = n0

# Construction du sous-arbre gauche
arbre1.insert_gauche(n1)
arbre1.get_ssa_gauche().insert_gauche(n3)
arbre1.get_ssa_gauche().insert_droit(n4)

# Construction du sous-arbre droit
arbre1.insert_droit(n2)
arbre1.get_ssa_droit().insert_gauche(n5)
arbre1.get_ssa_droit().insert_droit(n6)


print("Arbre 1 :", affiche(arbre1))