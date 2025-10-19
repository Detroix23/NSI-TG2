mots ='FLORES POULAIN CLAPET COFFRET FORGES ASTRILD CREPES NOIRCIR HANSES POIGNET'
a = 0
b = len(mots)
toto=''
for i in range(0, int(len(mots)/2)):
    if (mots[i]==' '):
        toto = toto + mots[abs(a-b)]
    a = a + 2
    b = b - 1
    
print(toto)