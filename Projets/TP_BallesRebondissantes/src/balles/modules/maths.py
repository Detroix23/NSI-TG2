"""
BALLS
maths.py
"""
import math

class Vector2D:
    """
    Define a vector.
    """
    x: int
    y: int
    
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, other: object) -> 'Vector2D':
        if isinstance(other, Vector2D):
            return Vector2D(
                self.x + other.x,
                self.y + other.y,
            )
        else:
            raise ValueError(f"(X) - Other is not a valid type ({other}, {type(other)})")
    
    def __tuple__(self) -> tuple[int, int]:
        return (self.x, self.y)
