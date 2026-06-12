"""
# NSI Algorithmique: tri fusion.
NSI/5_Algorithmique/DiviserRegner/1_TriFusion/1_TriFusion_algorithms.py

Algorithmes critiques pour réaliser le tri fusion.
"""

def fusion_recursive(list1: list[int], list2: list[int]) -> list[int]:
    """
    Fusionne les deux `liste1` et `liste2` dans l'ordre croissant.

    @param list1: `list[int]`, liste triée d'entiers.
    @param list2: `list[int]`, liste triée d'entiers.
    """

    def body(list1: list[int], list2: list[int]) -> list[int]:
        if len(list1) == 0:
            return list2
        elif len(list2) == 0:
            return list1
        else:
            return ([list1[0]] + body(list1[1:], list2)
                if list1[0] < list2[0]
                else [list2[0]] + body(list1, list2[1:])
            )
        
    return body(list1, list2)


def main() -> None:
    """
    Point d'entré principal pour tester les algorithmes.
    """
    print(fusion_recursive([1, 3, 65, 192], [1, 1, 4, 4, 100]))        

if __name__ == "__main__":
    main()
    