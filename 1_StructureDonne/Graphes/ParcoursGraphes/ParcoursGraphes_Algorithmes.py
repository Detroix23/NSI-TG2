"""
# NSI Structures: parcours de graphes.
NSI/1_StructureDonne/GraphesParcours de graphes/ParcoursGraphes_Algorithmes.py
"""

class Graph:
    """
    # `Graph` formé par dictionnaires. 
    """
    nodes: dict[str, list[str]]

    def __init__(self, nodes: dict[str, list[str]]) -> None:
        """
        Instancie un `Graph` avec un dictionnaire de sommets `nodes`.
        """
        self.nodes = nodes

    def neighbors(self, node: str) -> list[str]:
        """
        Renvoie la liste des voisins du sommet `node`.
        """
        return self.nodes[node]

def breadth_first_search(graph: Graph, node: str) -> set[str]:
    """
    Parcours un graphe `graph` pour trouver tous les sommets à partir de `node`. 

    Largeur d'abord: utilise une file FIFO pour découvrir les noeuds "par niveau".  
    """
    queue: list[str] = []
    queue.insert(0, node)
    discovered: set[str] = {node}
    while len(queue) != 0:
        node = queue.pop()
        print(f"(?) breadth_first_search: node={node}, queue={queue}, discovered={discovered}.")
        for neighbor in graph.neighbors(node):
            if neighbor not in discovered:
                discovered.add(neighbor)
                queue.insert(0, neighbor)
    
    return discovered


def depth_first_search(graph: Graph, node: str) -> set[str]:
    """
    Parcours un graphe `graph` pour trouver tous les sommets à partir de `node`. 

    Longueur d'abord, ou en profondeur: utilise une pile FIFO pour explorer loin 
    et revenir en arrière si bloqué.  
    """
    stack: list[str] = []
    stack.append(node)
    visited: set[str] = set()
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            print(f"(?) depth_first_search: {node=}, {stack=}, {visited=}.")
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited

def recursive_search(graph: Graph, node: str, visited: set[str]) -> set[str]:
    """
    Parcours un graphe `graph` pour trouver tous les sommets à partir de `node`. 

    Récursif: explorer loin et revenir en arrière si bloqué. Équivaut à un parcours en profondeur.
    """
    visited_new: set[str] = visited.union({node})
    print(f"(?) recursive_search: {node=}, {visited_new=}.")
    for neighbor in graph.neighbors(node):
        if neighbor not in visited_new:
            visited_new = visited_new.union(recursive_search(graph, neighbor, visited_new))

    return visited_new


def main() -> None:
    """
    Point d'entré principal pour tester les algorithmes de parcours de graphe.
    """
    g1 = Graph({
        "B": ["A", "C"],
        "C": ["A", "B", "D"],
        "D": ["C", "E"],
        "E": ["D"],
        "A": ["B", "C"],
    })

    print(breadth_first_search(g1, "A"))
    print(depth_first_search(g1, "A"))
    print(recursive_search(g1, "A", set()))

if __name__ == "__main__":
    main()
