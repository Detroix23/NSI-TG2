"""
# NSI Structures: arbres et ABR.
NSI/1_StructureDonne/StructureArborescentes/Arbres_Algorithmes.py

Arbre: graphe connexe & sans cycles.
"""
from typing import Optional

class BinaryNode:
    """
    # `BinaryNode`: noeud d'un arbre binaire.
    """
    value: int
    left: Optional['BinaryNode']
    right: Optional['BinaryNode'] 
    count: int

    def __init__(
        self, 
        value: int, 
        left: Optional['BinaryNode'] = None, 
        right: Optional['BinaryNode'] = None, 
        count: int = 1
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.count = count
    
    def neighbors(self) -> list['BinaryNode']:
        neighbors: list['BinaryNode'] = []
        if self.left is not None:
            neighbors.append(self.left)
        if self.right is not None:
            neighbors.append(self.right)
        return neighbors
    
    def get_from_binary(self, binary: str) -> BinaryNode:
        """
        Renvoie la valeur dans l'arbre trouvé à partir de la racine `self`.

        Dans une chaîne binaire:
        - `0`: sous-arbre gauche;
        - `1`: sous-arbre droit.

        `binary`: `str` chaîne de bits. Ne pas mettre le `1` initial.        
        """ 
        selected: BinaryNode = self
        for bit in binary:
            if bit == "0" and selected.left is not None:
                selected = selected.left
            if bit == "1" and selected.right is not None:
                selected = selected.right
            else:
                return selected
            
        return selected

def height(root: BinaryNode, current: int = 0) -> int:
    """
    Cherche la hauteur, profondeur maximum, de l'arbre de racine `root`.
    """
    return (max(height(neighbor, current + 1) for neighbor in root.neighbors())
        if root.neighbors()
        else current   
    )

def main() -> None:
    """
    Point d'entré principal pour tester les algorithmes sur arbres.
    """
    a1 = BinaryNode(3,
        left=BinaryNode(1),
        right=BinaryNode(5,
            left=BinaryNode(4),
            right=BinaryNode(7,
                right=BinaryNode(10)
            ),    
        ),
    )

    print(f"{height(a1)=}")
    print(f"{a1.get_from_binary("10").value=}")

if __name__ == "__main__":
    main()
