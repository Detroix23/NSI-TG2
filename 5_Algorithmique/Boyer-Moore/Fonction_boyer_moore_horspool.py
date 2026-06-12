# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:58:57 2026

@author: Noémie
"""

def boyer_moore_horspool(texte, motif):
    """In : texte et motif des chaines de caractères
    Out : une liste de la position des occurrences du motif dans le texte"""
    assert len(texte)>= len(motif)
    n = len(texte) # 
    m = len(motif)
    positions = []  #
    nb_tests=0
    tbSauts = table_sauts(motif) #
    i = 0
    while(i<=n-m): #
        trouve = True   # 
        j = m-1  #
        nb_bonnes_lettres = 0  # 
        while j >=0 and trouve:
            nb_tests+=1
            if(texte[i+j]!=motif[j]): #
                trouve = False    # 
                if(texte[i+j] in tbSauts and tbSauts[texte[i+j]]<=j): #
                    i+=tbSauts[texte[i+j]] #
                else:
                    if texte[i+j] in tbSauts:
                        i+=tbSauts[texte[i+j]]-nb_bonnes_lettres # 
                    else:
                        i+=j+1    # 
            
            nb_bonnes_lettres += 1 #
            j-=1
        if(trouve): #
            positions.append(i) #
            i=i+1 # 
        
    print("Avec la méthode Boyer Moore Horspool, on a fait :",nb_tests,"comparaison(s)")
    
    return positions