"""
CLI - Shapes
basics.py
Draw shapes on the terminal.
"""

import maths.maths as maths
import animations.screen as screen


class Shape:
    position: maths.Vector2D
    
    def __init__(self, position: maths.Vector2D) -> None:
        self.position: maths.Vector2D = position
    
    def draw(self) -> None:
        raise 
