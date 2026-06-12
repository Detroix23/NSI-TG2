from hanoi_vision import Visualisation_hanoi

def bouge(x,y):
    if len(x) == 0:
        return "Vous ne pouvez pas déplacer depuis une tour vide"
    deplace = x[-1]
    if len(y) == 0:
        x.pop()
        y.append(deplace)
    else:
        if y[-1] < deplace:
            return "Vous ne pouvez pas déplacer sur un socle plus petit"
        else : 
            x.pop()
            y.append(deplace)


tour0 = [5,4,3,2,1]
tour1 = []
tour2 = []
hanoi = [tour0, tour1, tour2]


def deplace_2_pions(depart,intermediare,arrivee):
    if len(depart) == 1:  #On part du principe que les pions commencent tous au départ
        bouge(depart,arrivee)
    else:
        bouge(depart,intermediare)
        bouge(depart,arrivee)
        bouge(intermediare,arrivee)

def deplace_n_pions(n,depart,intermediare,arrivee):
    if n == 1:
        bouge(depart,arrivee)
    if n == 2:
        deplace_2_pions(depart,intermediare,arrivee)
    else :
        deplace_n_pions(n-1,depart,arrivee,intermediare)
        bouge(depart,arrivee)
        deplace_n_pions(n-1,intermediare,depart,arrivee)




def main():
    v = Visualisation_hanoi(hanoi)
    deplace_n_pions(5,tour0,tour1,tour2)
    v.mise_a_jour(hanoi)
    v.fin()

main()
