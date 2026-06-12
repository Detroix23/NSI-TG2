from time import time

def recherche_naive(motif, texte):
    # A compléter
    
    pass

def table_sauts(motif):
    # A compléter
    
    pass


def boyer_moore_horspool(texte, motif):
    # A compléter
    
    pass

#texte=input("Donner le texte à tester:")
#motif=input("Donner le motif a retrouver dans le texte:")

texte = 'Allons enfin ! Le nom du chien de Tintin est Milou et pas Rintintinati !'
motif = 'tin'

#print("Table de sauts pour le motif PAPI : ",table_sauts("PAPI"))
#print("Table de sauts pour le motif CTGCGA:", table_sauts("CTGCGA"))
#print("Table de sauts pour le motif ACTGCGA:", table_sauts("ACTGCGA"))


#fichier_texte = open("Texte_comparaison.txt", "r", encoding="UTF-8")
#texte = fichier_texte.read()

#motif = "Cet homme de tant d'esprit avait l'air inquiet"

#print("En tout, il y a : ",recherche_naive(motif, texte)," occurence(s)(méthode naive) du motif :", motif)
# print(boyer_moore_horspool(texte, motif))
#print("En tout, il y a : ", len(boyer_moore_horspool(texte, motif))," occurence(s)(Boyer Moore Horspool) du motif", motif)

"""debut = time()
recherche_naive(motif,texte)
temps = time() - debut
print("Temps d'exécution de la recherche naïve :", temps)

debut = time()
recherche_naive(motif,texte)
temps = time() - debut
print("Temps d'exécution de la recherche avec Boyer-Moore :", temps)"""



