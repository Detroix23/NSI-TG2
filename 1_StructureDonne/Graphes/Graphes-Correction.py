# Créé par Gisèle Bareux, le 19/08/2020 avec EduPython
# Dernière modification : Noémie Exartier, le 27/01/2026

def CREER_GRAPHE_VIDE():
    return {}

def AJOUTER_SOMMET(G,s):
    if s in G:
        print("Ce sommet existe déjà, impossible de le rajouter")
    else:
        G[s] = []
    return G

def AJOUTER_ARC(G, sd, sf):
    if (sd in G) and (sf in G):    # on teste si sd et sf sont des sommets qui existent
        if sf not in G[sd]:        # on teste si l'arc de sd vers sf n'existe pas encore
            G[sd].append(sf)
        return G
    else:
        print("Impossible de rajouter cet arc")
        
def AJOUTER_ARETE(G, sd, sf):
    if (sd in G) and (sf in G):        # on teste si sd et sf sont des sommets qui existent
        if sf not in G[sd]:            # et si l'arête de sd vers sf n'existe pas encore
            G[sd].append(sf)
            if sd != sf:
                G[sf].append(sd)
        return G
    else:
        print("Impossible de rajouter cette arete")

def SUPPRIMER_SOMMET(G,s):
    if s in G:        # Le sommet existe
        del G[s]      # supprime le sommet
        for cle in G: # pour chaque sommet, on va tester s'il y a un arc vers le sommet à supprimer
            if s in G[cle]:
                index_de_s = G[cle].index(s) # on cherche l'index dans la liste du sommet supprimé
                del G[cle][index_de_s] # on supprime l'arc qui va à ce sommet
        return G
    else:
        print("Impossible de supprimer ce sommet")

def SUPPRIMER_ARC(G, sd, sf):
    if (sd in G) and (sf in G[sd]):          # le sommet sd existe et il y a un arc vers sf
        index_sf = G[sd].index(sf)           # on recherche l'index de sf dans la liste G[sd]
        del G[sd][index_sf]                  # on supprime l'arc allant de sd à sf
        return G
    else:
        print("Impossible de supprimer cet arc")

def SUPPRIMER_ARETE(G, sd, sf):
    if (sd in G) and (sf in G[sd]):        # le sommet sd existe et il y a une arête vers sf
        index_sf = G[sd].index(sf)
        del G[sd][index_sf]                 # on supprime l'arete de sd vers sf
        if sd != sf:                        # il faut aussi supprimer sdl'arête de sf vers sd
            index_sd = G[sf].index(sd)
            del G[sf][index_sd] 
        return G
    else:
        print("Impossible de supprimer cette arete")

def nb_sommets(G):
    return len(G)

def deg_non_oriente(G, s):
    nb_boucles = 0
    if G[s] != []:
        for cle in G:
            if cle in G[cle]:
                nb_boucles += 1        # détection des boucles qui comptent double 
    return len(G[s]) + nb_boucles

def deg_oriente(G, s):
    deg = 0
    if G[s] != []:       # si des arcs sortent du sommet s     
        deg = len(G[s])  # on calcule les degrés sortant du sommet s : d+
    for cle in G:        # on ajoute les degrés entrant du sommet s : d-
        if (s in G[cle]): 
            deg += 1
    return deg

def conversion_g_en_mat_adj(G):
    n = nb_sommets(G)
    liste_sommets = []
    mat = [n*[0] for i in range(n)]
    for cle in sorted(G.keys()): #on trie par ordre alphabétique la liste des clés du dictionnaire et on les stocke dans sommets
        liste_sommets.append(cle)
    for cle in G:
        valeurs = G[cle]
        valeurs.sort()
        # print(valeurs)
        index_ligne = liste_sommets.index(cle)          # numero de la ligne dans la matrice
        for sommet in valeurs:
            index_colonne = liste_sommets.index(sommet) # numero de la colonne dans la matrice
            mat[index_ligne][index_colonne]=1
    return mat

def conversion_mat_adj_en_g(mat):
    graphe = CREER_GRAPHE_VIDE()
    for i in range(len(mat)):
        AJOUTER_SOMMET(graphe, chr(65 + i))
    for k in range(len(mat)):
        for j in range(len(mat)):
            if mat[k][j] == 1:
                AJOUTER_ARC(graphe, chr(65 + k), chr(65 + j)) #la lettre A vaut 65 en decimal dans le codage ASCII.
    return graphe


G1 = CREER_GRAPHE_VIDE()
AJOUTER_SOMMET(G1,'A')
AJOUTER_SOMMET(G1,'B')
AJOUTER_SOMMET(G1,'C')
AJOUTER_SOMMET(G1,'D')
AJOUTER_SOMMET(G1,'E')
AJOUTER_SOMMET(G1,'F')
AJOUTER_ARC(G1,'A','B')
AJOUTER_ARC(G1,'B','C')
AJOUTER_ARC(G1,'C','F')
AJOUTER_ARC(G1,'F','E')
AJOUTER_ARC(G1,'E','D')
print(G1)
SUPPRIMER_ARC(G1,'A','B')
SUPPRIMER_ARC(G1,'E','A')
print(G1)

G2 = CREER_GRAPHE_VIDE()
AJOUTER_SOMMET(G2,'A')
AJOUTER_SOMMET(G2,'B')
AJOUTER_SOMMET(G2,'C')
AJOUTER_SOMMET(G2,'D')
AJOUTER_ARETE(G2,'A','B')
AJOUTER_ARETE(G2,'A','C')
AJOUTER_ARETE(G2,'A','D')
AJOUTER_ARETE(G2,'B','C')
AJOUTER_ARETE(G2,'B','D')
AJOUTER_ARETE(G2,'C','D')
SUPPRIMER_SOMMET(G2,'D')
SUPPRIMER_SOMMET(G2,'E')
SUPPRIMER_ARETE(G2,'A','B')
SUPPRIMER_ARETE(G2,'E','A')
print(G2)

print("Le nombre de sommets de G1 est : " + str(nb_sommets(G1)))
print("Le nombre de sommets de G2 est : " + str (nb_sommets(G2)))
print("Le degré du sommet A de G2 est : " + str (deg_non_oriente(G2,'A')))
print("Le degré du sommet C de G2 est : " + str (deg_non_oriente(G2,'C')))
print("Le degré du sommet A de G1 est : " + str(deg_oriente(G1,'A')))
print("Le degré du sommet B de G1 est : " + str(deg_oriente(G1,'B')))

G3 = {'A':['B','D'],
      'B':['A','C'],
      'C':['B'],
      'D':['A','B']
      }
      
print(conversion_g_en_mat_adj(G3))

G4 = {'A':['B'],
      'B':['C','E'],
      'C':['B','E'],
      'D':['A','B','F'],
      'E':['D','F'],
      'F':['D']
      }
      
print(conversion_g_en_mat_adj(G4))

matrice5 = [[0,1,0,1,1],
            [1,0,1,0,0],
            [0,1,0,1,1],
            [1,0,1,0,0],
            [1,0,1,0,1]
            ]
G5 = conversion_mat_adj_en_g(matrice5)
print(G5)

G6 = {'A':['B','C'],
      'B':['A','D','E'],
      'C':['A','D','H'],
      'D':['B','C','E'],
      'E':['B','D','F'],
      'F':['E','G'],
      'G':['F','H'],
      'H':['G','C']
      }
      
G7 = {'A' :['E','F'],
      'B' :['C','D'],
      'C' :['D','B'],
      'D' :['B','C'],
      'E' :['A'],
      'F':['A']
      }

