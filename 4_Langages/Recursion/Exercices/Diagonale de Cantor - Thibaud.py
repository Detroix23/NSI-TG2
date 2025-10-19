def numero(x, y):
    if x == 0 and y == 0:
        return 0
    elif y == 0:
        return 1 + numero(0, x-1)
    else:
        return 1 + numero(x+1, y-1)
    
print(numero(0, 0))  #retourne 0
print(numero(0, 4))  #retourne 14
print(numero(3, 0))  #retourne 6