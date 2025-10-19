"""
BALLS
colors.py
"""
import random
from enum import Enum

class Mode(Enum):
    NO_ERASE = 0
    EPILEPSY = 1
    FIXED = 2
    GRADIENT = 3
    INFECTION = 4
    

class Color:
    """
    Define a RGB256 color.
    """
    r: int
    g: int
    b: int
    
    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __tuple__(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)

    @staticmethod
    def random() -> 'Color':
        return Color(*[random.randint(0, 255) for _ in range(3)])

    def increment(self) -> None:
        """
        Increment components to make a smooth gradient over time.
        """
        self.r += 1
        self.g += 1
        self.b += 1
        
        self.r %= 255
        self.g %= 255
        self.b %= 255


class Base:
    BLACK = Color(0, 0, 0)
    WHITE = Color(255, 255, 255)
    RED = Color(255, 0, 0)
    

def random_color() -> tuple[int, int, int]:
    """
    Get a class `Color` of random colors (0-255).
    """
    return Color.random()

