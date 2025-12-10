"""
# Subject 2024
src/__main__.py  
Application.  
"""

INFTY: int = 10**32
k: int = 10

def lacher(i: int) -> bool:
    """
    Renvoie si l'oeuf casse si lâché depuis l'étage `i`.
    """
    if k < 1:
        raise ValueError(f"(X) - Plus d'oeufs `k` ({k}).")

    return i > 10

def verif_etage_critique(c: int) -> bool:
    """
    _Question 1.1.1_
    Verifier si l'oeuf casse, laché depuis l'étage `c`.
    """
    return lacher(c)

def critique_un_seul_oeuf(n: int) -> int:
    """
    _Question 1.1.2_
    Renvoie l'étage critique en utilisant qu'un seul oeuf, k = 1.
    n: int, nombre d'étage de l'immeuble.
    S'il n'existe pas, renvoie `n + 1`.
    """
    etage: int = 0
    while not verif_etage_critique(etage) and etage < n:
        etage += 1

    if etage == n and not verif_etage_critique(etage):
        etage += 1

    return etage

def critique_dichotomique(n: int) -> int:
    """
    _Question 1.1.3_
    Renvoie l'étage critique en utilisant de la dichotomie et en disposant de k = n oeufs.
    n: int, nombre d'étage de l'immeuble.
    S'il n'existe pas, renvoie `n + 1`.
    """
    borne_inferieure: int = 0
    borne_superieure: int = n
    milieu: int = (borne_inferieure + borne_superieure) // 2

    while borne_inferieure <= borne_superieure:
        if verif_etage_critique(milieu):
            borne_superieure = milieu - 1
        else:
            borne_inferieure = milieu + 1
        
        milieu: int = (borne_inferieure + borne_superieure) // 2

    if not verif_etage_critique(milieu):
        milieu += 1

    return milieu

def L(e: int, r: int, depth: int = 0) -> int:
    print(f"{e=}, {r=}, {depth=}")

    if r == 0 and e > 0:
        return INFTY
    if e == 0:
        return 0
    
    minimum: int = 0
    for i in range(1, e + 1):
        l1: int = L(i - 1, r - 1, depth=depth+1)
        l2: int = L(e - i, r, depth=depth+1)
        if l1 > l2 and l1 < minimum:
            minimum = l1
        elif l2 > l1 and l2 < minimum:
            minimum = l2
    
    return 1 + minimum


def main() -> None:
    """
    Porte d'entrée principale pour tout test.
    """

    print(L(20, 5))

if __name__ == "__main__":
    main()
