def deplace2pions(depart,arrivee,intermediaire):
    bouge(depart,intermediaire)
    bouge(depart,arrivee)
    bouge(intermediaire,arrivee)

def deplaceNpions(n, depart, arrivee, intermediaire):
    if n == 2:
        deplace2pions(depart, arrivee, intermediaire)
    else:
        deplaceNpions(n-1, depart, intermediaire, arrivee)
        bouge(depart, arrivee)
        deplaceNpions(n-1, intermediaire, arrivee, depart)