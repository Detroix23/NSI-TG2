"""
TREE
tree.py
"""
import numpy
from typing import Optional

# Special header to take the actual branch value, and not the next branch.
CURRENT: str = ""


class Tree:
    """
    Define a Tree using numpy.
    Arguments:
        - arrays: numpy.NDarray(dtype=int); Used to store data in numpy arrays.
        - headers: list[Optional[str]]; Give named keys for the index-only numpy arrays.
        `CURRENT` in the list allow to get value of branch that are not in the extremites.
        Don't forget to create value for all branch, and not only the last ones.
    
    Exemple: Current = Crt
        
            Crt A   B
    Crt     1   2   3 
      A     4   5   6
      B     7   8   9
    """
    dtype: numpy.dtype
    arrays: numpy.ndarray
    headers: tuple[str]
    
    def __init__(self, arrays: numpy.ndarray, headers: tuple[str]) -> None:
        """
        Construct the tree.
        """
        self.arrays = arrays
        self.dtype = self.arrays.dtype
        headers = (CURRENT,) + headers
        self.headers = headers
    
    def __str__(self) -> str:
        return f"""Tree(
    arrays=(
        size={self.arrays.size}
        ndim={self.arrays.ndim}
        shape={self.arrays.shape}
    ) 
    headers={self.headers}
) """ 
    
    def __repr__(self) -> str:
        return f"Tree(arrays=(size={self.arrays.size} ndim={self.arrays.ndim} \
shape={self.arrays.shape}) headers={self.headers})"
        
    def get(self, *headers: str) -> int:
        """
        Return the value of the three following the given headers.
        """
        indexes: list[int] = list()
        
        if len(headers) > self.arrays.ndim:
            raise IndexError(f"(X) - Too many headers: {len(headers)} {headers}. \n{self}")
        
        for header in headers:
            if header not in self.headers:
                raise KeyError(f"(X) - Header {header} not in the tree's headers ({self.headers})")
            
            indexes.append(self.headers.index(header))
            
        return self.arrays[*indexes]
    
    def update(self, value: int, *headers: str) -> None:
        """
        Update to the `value` the position at `headers`.
        """
        indexes: list[int] = list()
        
        if len(headers) > self.arrays.ndim:
            raise IndexError(f"(X) - Too many headers: {len(headers)} {headers}. \n{self}")
        
        for header in headers:
            if header not in self.headers:
                raise KeyError(f"(X) - Header {header} not in the tree's headers ({self.headers})")
            
            indexes.append(self.headers.index(header))
        
        # print(f"dtype {self.dtype} {repr(self.dtype)} {type(self.dtype)} {self.dtype.__class__}")
               
        try:
            if not hasattr(self.arrays[*indexes], 'dtype'):
                raise ValueError(f"(X) - Somehow not a numpy array element. \
{self.arrays[*indexes]} {type(self.arrays[*indexes])}")

            if self.arrays[*indexes].dtype != self.dtype:
                raise IndexError(f"(X) - Can't update a whole array; update an unique value. \
headers={headers}, result={self.arrays[*indexes]} type={type(self.arrays[*indexes])}")
         
            self.arrays[*indexes] = value

        except Exception as exception:
            print(f"(X) - tree.update: headers={headers}, indexes={indexes}.")
            raise exception
    
    
    def string_tree(self, level_in: Optional[int] = None) -> str:
        """
        Display the tree branch to a certain `level`.
        0 (default) means all.
        """
        level: int
        if level_in is None:
            level = self.arrays.ndim
        else:
            level = level_in
        
        ranks: list[list[str]] = list()
        
        ranks.append([
            f"{header}: {self.get(header, CURRENT)}" for header in self.headers 
            if header != CURRENT 
        ])

        def headers_combinations(level: int) -> list[tuple[str, ...]]:
            if level <= 1:
                return [(header, ) for header in self.headers]
            
            headers: list[tuple[str, tuple]] = list()
            
            

        print("HC:", headers_combinations(3))

        return ranks
    
def main() -> None:
    print("# Tree")
    print("## TREE")
    
    a1 = numpy.array([[
            [1, 2, 3, 4],
            [4, 5, 6, 7],
            [7, 8, 9, 10],
            [10, 11, 12, 13],
        ], [
            [5, 2, 3, 4],
            [4, 5, 6, 7],
            [7, 8, 9, 10],
            [10, 11, 12, 13],
        ], [
            [7, 2, 3, 4],
            [4, 5, 6, 7],
            [7, 8, 9, 10],
            [10, 11, 12, 13],
        ], [
            [7, 2, 3, 4],
            [4, 5, 6, 7],
            [7, 8, 9, 10],
            [10, 11, 12, 13],
        ],
    ])
            
    h1 = ("A", "B", "C")
    t1 = Tree(a1, h1)
    
    print(t1)
    g = ("A", "C")
    print("-", g, t1.get(*g))
    g = ("A")
    print("-", g, t1.get(*g))
    g = ("A", CURRENT)
    print("-", g, t1.get(*g))
    g = (CURRENT)
    print("-", g, t1.get(*g))
    g = ("C", "A")
    a1 = t1.update(34, *g)
    
    print()
    g = (CURRENT)
    print("-", g, t1.get(*g))
    
    
    print()
    print(t1.string_tree())
    
    
if __name__ == "__main__":
    main()
    
    