# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:23:14 2024

@author: Noémie Exartier
"""

def aligne(s1, s2):
    """ Paramètres
    ---------
    s1 : (str)
    une chaîne de caractères correspondant à la première séquence.
    
    s2 : (str)
    une chaîne de caractères correspondant à la deuxième séquence.
    
    Résultat
    --------
    (int)
    Cette fonction renvoie le score du meilleur alignement de s1 et s2.
"""

    n1, n2 = len(s1), len(s2)
    sc = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    # Remplissage de la première colonne
    for i in range(1, n1 + 1):
        sc[...][...] = -i
    
    # Remplissage de la première ligne
    for j in range(..., ...):
        sc[...][...] = ...
    
    # Autres coefficients
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            # Score qui serait obtenu dans la case (i, j) par l'alignement du dernier caractère de seq1 avec -
            a = ...
            
            # Score qui serait obtenu dans la case (i, j) par l'alignement du dernier caractère de seq2 avec -
            b = ...
            
            # Score qui serait obtenu dans la case (i, j) par alignement du dernier caractère de seq1
            # avec le caractère de seq2
            if s1[i - 1] == s2[j - 1]: 
                c = ...
            else:
                c = ...
            trois_valeurs = [a, b, c]
            sc[...][...] = max(trois_valeurs)
    return ...

seq1_1 = "ENORME"
seq1_2 = "GENOME"

seq2_1 = "ATATACAGGTCA"
seq2_2 = "GACTACACGACT"

seq3_1 = "ASTUCIEUX"
seq3_2 = "STUDIEUX"

assert aligne(seq1_1, seq1_2) == 3
assert aligne(seq2_1, seq2_2) == 1
assert aligne(seq3_1, seq3_2) == 5

# Autres tests à prévoir...
    

            

