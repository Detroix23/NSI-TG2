from hanoi_vision import Visualisation_hanoi

def bouge(x, y):
    # vérification déplacement licite
    if len(hanoi[x]) == 0: # La tour de départ est vide
        print("pas de pion à déplacer")
    elif len(hanoi[y]) == 0: # la tour de départ est pleine et la tour de destination est vide
        pion = hanoi[x].pop()
        hanoi[y].append(pion)
    elif hanoi[x][-1] < hanoi[y][-1]: # Le pion sur la tour de départ est inferieur au pion sur la tour d'arrivée, on peut le déplacer
        pion = hanoi[x].pop()
        hanoi[y].append(pion)
    else: # pion de départ est superieur à pion arrivée
        print("Déplacement illicite")
    print(hanoi)
    v.mise_a_jour(hanoi)

tour0 = [3, 2, 1]
tour1 = []
tour2 = []
hanoi = [tour0, tour1, tour2]
print(hanoi)
v = Visualisation_hanoi(hanoi)

bouge(0, 2)
bouge(0, 1)
bouge(2, 1)
bouge(0, 2)
bouge(1, 0)
bouge(1, 2)
bouge(0, 2)
v.fin()



