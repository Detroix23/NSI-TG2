
def sommetsDegreMax(G_mat):
    '''
    Permet d'obtenir les numeros des sommets de plus haut degré d'un graphe défini par sa matrice d'adjacence
    Par Hector.
    @param G_mat : matrice d'adjacence d'un graphe G (matrice obligatoirement carrée)
    @return numSommetDegreMax : liste des numéros de sommets de degre max
    '''
    score: int = 0
    podium: int = []
    index: int = 0
    while index < nbSommets(G_mat):
        count: int = degre(G_mat, index) 
        
        if count > score:
            score = count
            podium = [index]
            
        elif count == score:
            podium.append(index)
        
        index += 1
    
    return podium
    