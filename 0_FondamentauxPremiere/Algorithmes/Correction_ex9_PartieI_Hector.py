"""
    Fonction: Renvoie vrai si la liste est trié dans l'ordre décroissant.
    Condition: Liste de tuples, où la valeur a trier est d'index 1.
"""
def ordre_decroissant(liste_personnes: list[tuple[str, int]]) -> bool:
    decroissant: bool = True
    i: int = 0
    while decroissant and i < len(liste_personnes) - 1:
        if liste_personnes[i][1] < liste_personnes[i+1][1]:
            decroissant = False
    
    return decroissant 

    
assert ordre_decroissant([('Leo', 12), ('Lea', 19), ('Zoe', 17)]) == False
assert ordre_decroissant([('Lea', 19), ('Zoe', 17),('Leo', 12)]) == True
