#Exercice 1

def compte_a(chaine):
    if len(chaine) == 1 :
        if chaine[0] == "a" :
            return 1
        else:
            return 0
    else:
        if chaine[0] == "a":
            return (1 + compte_a(chaine[1:]))
        else:
            return compte_a(chaine[1:])


print(compte_a("blabla"))	# affiche 2
print(compte_a("dur")) 		# affiche 0


#Exercice 2

def numero(x,y):
    if (x == 0) and (y == 0):
       return 0 
    elif y==0:
        return x + numero(x-1,0)
    else:
        return numero(x+1,y-1)+1


def numerov2(x,y):
    if x==0 and y==0:
        return 0
    elif y==0:
        return numero(0,x-1)+1
    else:
        return numero(x+1,y-1)+1


#Exercice 3
    
def NbChiffres(n):
    if n < 10:
        return 1
    else:
        return 1 + NbChiffres(n // 10)




