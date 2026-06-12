def recherche_naive(motif,texte):
    n=len(texte)
    m=len(motif)
    compteur_occurences=0
    nb_tests=0
    assert n>=m,'Le texte n\'est pas assez long pour y trouver le motif'
    for s in range(n-m+1):
        nb_tests=nb_tests+1
        if motif[0:m]==texte[s:s+m]:
            compteur_occurences+=1
            # print("L'ocurrence ",compteur_occurences, " à été trouvée au ",s,"ième caractère")
    print("Avec la méthode naïve, on a fait :",nb_tests,"comparaison(s)")
    return compteur_occurences

def table_sauts(motif):
    table={}
    i=0
    for lettre in motif[:-1]:#on enlève le dernier caractère
        table[lettre]=len(motif)-i-1
        i+=1
    return table

def boyer_moore_horspool(texte, motif):
    """In : texte et motif des chaines de caractères
    Out : une liste de la position des occurrences du motif dans le texte"""
    assert len(texte)>= len(motif)
    n = len(texte)# On récupère la taille de chaque chaine,
    m = len(motif)
    positions = []  #Création d'une liste pour récupérer les positions des motifs trouvés
    nb_tests=0
    tbSauts = table_sauts(motif)#Remplissage de la liste: création de la table des sauts
    i = 0
    while(i<=n-m):#tant que l'indice i est inférieur à la taille du texte moins celle du motif
        trouve = True   # On suppose avoir trouvé une correspondance
        j = m-1  # position dans le motif
        nb_bonnes_lettres = 0  # compte le nombre de lettres qui coïncident
        while j >=0 and trouve:
        #for j in range (m-1,-1,-1):#On teste en partant de la droite la correspondance des caractères du motif avec ceux du texte
            #trouve=True
            nb_tests+=1
            if(texte[i+j]!=motif[j]):#si la lettre du texte juste au-dessus est différente de celle du motif
                trouve = False    # il n'y a pas de correspondance
                if(texte[i+j] in tbSauts and tbSauts[texte[i+j]]<=j): #si la lettre du texte est dans le motif et le saut de cette lettre<=j
                    i+=tbSauts[texte[i+j]]#on ajoute à i le saut correspondant à la lettre du texte que l'on compare
                else:
                    if texte[i+j] in tbSauts:
                        i+=tbSauts[texte[i+j]]-nb_bonnes_lettres # Décalage en tenant compte des lettres qui coïncident
                    else:
                        i+=j+1    # Décalage du reste du motif
            
            nb_bonnes_lettres += 1 # On incrémente de 1 lorsque deux lettres coïncident
            j-=1
        if(trouve):#Si tous les caractères correspondent
            positions.append(i) #On ajoute la position de la portion du texte
            i=i+1 # On décale le motif de 1 
        
    print("Avec la méthode Boyer Moore Horspool, on a fait :",nb_tests,"comparaison(s)")
    
    return positions

#texte=input("Donner le texte à tester:")
#motif=input("Donner le motif a retrouver dans le texte:")
#print("En tout, il y a : ",recherche_naive(motif,texte)," occurence(s)")
#print("Table de sauts pour le motif exo:",table_sauts("PAPI"))
#print("Table de sauts pour le motif CTGCGA:", table_sauts("CTGCGA"))
#print("Table de sauts pour le motif ACTGCGA:", table_sauts("ACTGCGA"))
#recherche_naive(motif,texte)


fichier_texte = open("Texte_comparaison.txt", "r", encoding = "UTF-8")
texte = fichier_texte.read()

motif = "Cet homme de tant d'esprit avait l'air inquiet"
#boyer_moore_horspool(texte,motif)
print("En tout, il y a : ",recherche_naive(motif, texte)," occurence(s)(méthode naive) du motif :", motif)
# print(boyer_moore_horspool(texte, motif))

print("En tout, il y a : ", len(boyer_moore_horspool(texte, motif))," occurence(s)(Boyer Moore Horspool) du motif", motif)

"""fichier_texte=open("Texte_comparaison.txt","r")
texte=fichier_texte.read()
print("En tout, il y a : ",recherche_naive(motif,texte)," occurence(s)(méthode naive) du motif :",motif)
print(boyer_moore_horspool(texte,motif))
print("En tout, il y a : ", len(boyer_moore_horspool(texte,motif))," occurence(s)(Boyer Moore Horspool) du motif",motif)"""
