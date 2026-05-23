"""
# NSI.
Épreuve pratique.

analyse.py

Correction: Hector, 32 minutes.
"""
from math import sqrt

import donnees
import donnees_completes

EMPLOYES = list[dict[str, int | str]]

def salaire_moyen_condition(employes: EMPLOYES, champ: str, valeur: str | int) -> None | float:
    '''
    Renvoie le salaire moyen des employes ayant val comme valeur associée
    au champ donné en argument.
    Si le nombre d'employés considéré est nul, cette fonction renvoie None
    '''
    summation: int = 0
    count: int = 0
    for employee in employes:
        if employee[champ] == valeur and isinstance(employee["salaire"], int):
            summation += employee["salaire"]
            count += 1

    if count == 0:
        return None
    
    return summation / count


def test_salaire_moyen_condition():
    e: EMPLOYES = donnees.employes
    assert salaire_moyen_condition([], 'sexe', 'F') == None
    assert salaire_moyen_condition(e, 'sexe', 'F') == 2400.0
    assert salaire_moyen_condition(e, 'etudes', 3) == 2550.0
    assert salaire_moyen_condition(e, 'etudes', 12) == None


def effectif_par_sexe(employes: EMPLOYES) -> dict[str, int]:
    '''Renvoie un dictionnaire ayant deux clés 'F' et 'M'
    associée respectivement au nombre d'employées femmes et au
    nombre d'employés hommes dans les données en arguments.'''
    effectifs: dict[str, int] = {"F": 0, "M": 0}
    for employee in employes:
        if employee["sexe"] == "F":
            effectifs["F"] += 1
        else:
            effectifs["M"] += 1
    
    return effectifs

def test_effectif_par_sexe():
    e: EMPLOYES = donnees.employes
    assert effectif_par_sexe(e) == {'F': 3, 'M': 3}


def calcul_ecart_sexe(employes) -> None | float:
    '''Renvoie l'écart de salaire en pourcentage pour les femmes 
    par rapport aux hommes'''
    moy_h: None | float = salaire_moyen_condition(employes, 'sexe', 'M')
    # La variable `employes` était écrite sous un string.
    moy_f: None | float = salaire_moyen_condition(employes, 'sexe', 'F')
    
    # Arithmétique impossible quand `None` peut être présent.
    if moy_f is None or moy_h is None:
        return None
    
    # Mauvaise formule.
    return (moy_h - moy_f) / moy_h * 100

def test_calcul_ecart_sexe() -> None:
    employes_0: EMPLOYES = []
    assert calcul_ecart_sexe(employes_0) is None
    
    
    employes_1sexe: EMPLOYES = [
        {'experience': 5, 'etudes': 3, 'sexe': 'F', 'salaire': 2400},
        {'experience': 5, 'etudes': 5, 'sexe': 'F', 'salaire': 2500},
        {'experience': 2, 'etudes': 5, 'sexe': 'F', 'salaire': 2300},
    ]
    assert calcul_ecart_sexe(employes_1sexe) is None

    assert 0 <= calcul_ecart_sexe(donnees.employes) <= 100
    assert 0 <= calcul_ecart_sexe(donnees_completes.employes) <= 100

# Attribution d'un premier salaire après embauche par les k plus proches voisins

def sexe_vers_entier(e):
    if e['sexe'] == 'F':
        return 1
    else:
        return -1


def distance(e1, e2):
    '''Renvoie la mesure de distance entre deux personnes.'''
    s = (
        # Cela implique que l'écart de salaire est normal.
        # (sexe_vers_entier(e1) - sexe_vers_entier(e2))**2
        + (e1['experience'] - e2['experience'])**2
        + (e1['etudes'] - e2['etudes'])**2
    )
    return sqrt(s)


def k_plus_proches(k, employes, e):
    '''Renvoie les k employes les plus proches de e par la 
    distance définie au dessus.'''
    e_d = [
        (distance(e, employes[i]), i) 
        for i in range(len(employes))
    ]
    e_d.sort()  # va trier en premier sur la distance
    voisins = []
    for i in range(k):
        voisins.append(employes[e_d[i][1]])
    return voisins


def salaire_moyen(employes):
    '''Renvoie le salaire moyen pour une liste d'employes'''
    if len(employes) == 0:
        return None
    s = sum(e['salaire'] for e in employes)
    return s/len(employes)


def salaire_par_proximite(employes, e):
    '''Prend en entrée une liste d'employés et un dictionnaire comportant
    les champs experience, etudes et sexe et renvoie le salaire le plus
    proche en moyennant les 3 plus proches voisins'''
    voisins = k_plus_proches(3, employes, e)
    return salaire_moyen(voisins)

def test_salaire_par_proximite() -> None:
    futur_femme= {'experience': 3, 'etudes': 3, 'sexe': 'F'}
    futur_homme = {'experience': 3, 'etudes': 3, 'sexe': 'M'}

    print(f"Salaire par proximité Femme: {salaire_par_proximite(donnees_completes.employes, futur_femme)}")
    print(f"Salaire par proximité Homme: {salaire_par_proximite(donnees_completes.employes, futur_homme)}")

def main() -> None:
    print("\n\n# Analyse de salaire.")

    print("\n## Question 1.")
    test_salaire_moyen_condition()
    print(f"Salaire moyen Hommes: {salaire_moyen_condition(donnees_completes.employes, "sexe", "M")}")
    print(f"Salaire moyen Femmes: {salaire_moyen_condition(donnees_completes.employes, "sexe", "F")}")

    print("\n## Question 2.")
    test_effectif_par_sexe()

    print("\n## Question 3.")
    test_calcul_ecart_sexe()

    print("\n## Question 4.")
    test_salaire_par_proximite()

if __name__ == "__main__":
    main()
