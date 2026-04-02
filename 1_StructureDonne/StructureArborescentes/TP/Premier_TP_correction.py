# -*- coding: utf-8 -*-

class Noeud:
    
    def __init__(self, value:str):
        self.valeur = value
        self.sag = None
        self.sad = None
        
    def insert_gauche(self, value:str):
    """Créer le noeud de valeur valeue et l'insère un noeud dans le sous-arbre gauche"""
        if self.sag == None:
            self.sag = Noeud(value)
        else:
            new_node = Noeud(value)
            new_node.sag = self.sag
            self.sag = new_node
            
    def insert_droit(self, value:str):
    """Créer le noeud de valeur valeue et l'insère un noeud dans le sous-arbre gauche"""
        if self.sad == None:
            self.sad = Noeud(value)
        else:
            new_node = Noeud(value)
            new_node.sad = self.sad
            self.sad = new_node
            
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
arbre1 = Noeud(8)

# Construction du sous-arbre gauche
arbre1.insert_gauche(4)

arbre1.get_ssa_gauche().insert_gauche(3)
arbre1.get_ssa_gauche().insert_droit(6)

# Construction du sous-arbre droit

arbre1.insert_droit(12)

arbre1.get_ssa_droit().insert_gauche(9)
arbre1.get_ssa_droit().insert_droit(14)

print("Arbre 1 :", affiche(arbre1))

#-------------------------- Arbre 2 -----------------------------------#    

arbre2 = Noeud(8)
arbre2.insert_gauche(3)
arbre2.get_ssa_gauche().insert_droit("1")

print("Arbre 2 :", affiche(arbre2))


#-------------------------- Arbre 3 -----------------------------------#    

arbre3 = Noeud(8)# Construction du sous-arbre gauche
arbre3.insert_gauche(4)

arbre3.get_ssa_gauche().insert_gauche(3)
arbre3.get_ssa_gauche().insert_droit(6)
arbre3.get_ssa_gauche().get_ssa_gauche().insert_gauche(1)

# Construction du sous-arbre droit

arbre3.insert_droit(12)

arbre3.get_ssa_droit().insert_gauche(9)
arbre3.get_ssa_droit().insert_droit(14)
arbre3.get_ssa_droit().get_ssa_gauche().insert_droit(11)

print("Arbre 3 :", affiche(arbre3))
