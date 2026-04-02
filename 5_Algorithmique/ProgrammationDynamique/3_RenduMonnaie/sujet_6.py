"""
# Programmation dynamique.
Rendu de monnaie: Sujet 6.

La stratégie gloutonne est utilisée : on essaie de rendre la monnaie en maximisant le nombre de pièces de
grande valeur.
Exemple : s'il faut rendre 46 centimes, on prend autant de pièces de 20cts que possible sans dépasser la
somme à rendre, puis autant de pièces de 10cts que possible sans dépasser le reste de la somme à rendre, etc.
La fonction rendre_monnaie prend en paramètres somme_a_rendre, un nombre entier correspondant à la
somme à rendre (exprimée en centimes), et de `pieces_disponibles`, un dictionnaire associant la valeur faciale des
pièces (ou billets) et renvoie la liste des pièces (ou billets) à rendre 
"""

STOCK1: dict[int, int] = {
    500_00: 0,
    200_00: 0,
    100_00: 0,
    50_00: 0,
    20_00: 1,
    10_00: 2,
    5_00: 1,
    2_00: 3,
    1_00: 1,
    50: 1,
    20: 3,
    10: 0,
    5: 1,
    2: 0,
    1: 2
}

STOCK2: dict[int, int] = {
    500_00: 10000000,
    200_00: 10000000,
    100_00: 10000000,
    50_00: 10000000,
    20_00: 10000000,
    10_00: 10000000,
    5_00: 10000000,
    2_00: 10000000,
    1_00: 10000000,
    50: 10000000,
    20: 10000000,
    10: 10000000,
    5: 10000000,
    2: 10000000,
    1: 10000000
}

def rendre_monnaie(somme: int, pieces: dict[int, int]) -> list[int]:
    """
    Retourne une liste des valeurs des pièces à rendre.  
    Usage d'une stratégie gloutonne. 

    Exemple:
    ```python
    >>> rendre_monnaie(46, pieces_disponibles)
    [20, 20, 5, 1]
    ```
    """
    # liste des pièces à rendre
    pieces_rendues: list[int] = []
    # boucle de construction de la liste des pièces
    for valeur in pieces :
        while pieces[valeur] > 0 and somme - valeur >= 0 and True:
            somme -= valeur
            pieces[valeur] -= 1
            pieces_rendues.append(valeur)

    return pieces_rendues

def main() -> None:
    print("# Programmation dynamique")
    print("Rendu de monnaie: sujet 6.")
    
    print("Stock: 1.")
    for somme in (1, 3, 46, 123, 255, 5000):
        rendu: list[int] = rendre_monnaie(somme, STOCK1.copy())
        verification: int = sum(rendu)
        print(f"somme={somme}, rendu={rendu}, v={verification} ({'V' if somme == verification else 'X'});")

    print("Stock: 2.")
    for somme in (1, 3, 46, 123, 255, 5000):
        rendu: list[int] = rendre_monnaie(somme, STOCK2.copy())
        verification: int = sum(rendu)
        print(f"somme={somme}, rendu={rendu}, v={verification} ({'V' if somme == verification else 'X'});")


if __name__ == "__main__":
    main()
