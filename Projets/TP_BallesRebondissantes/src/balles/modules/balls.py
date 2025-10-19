"""
BALLS
balls.py
"""
import modules.maths as maths
import modules.colors as colors
import pygame


class Balle:
    """
    Define a ball.
    """
    window: pygame.Surface
    position: maths.Vector2D
    inertia: maths.Vector2D
    color: colors.Color
    
    def __init__(
        self,
        window, 
        position: maths.Vector2D,
        inertia: maths.Vector2D, 
        color: colors.Color,
        radius: int,
    ) -> None: 
        self.window = window
        self.position = position
        self.inertia = inertia
        self.color = color
        self.radius = radius
    
    def __repr__(self) -> str:
        return f"Balle(x={self.position.x}, y={self.position.y}, dx={self.inertia.x}, dy={self.inertia.y})"
        
    def move(self) -> None:
        """
        Apply intertia.
        """
        self.position = self.position + self.inertia
        
            
    def draw(self) -> None:
        pygame.draw.circle(
            self.window, 
            self.color.__tuple__(), 
            self.position.__tuple__(), 
            self.radius
        )
    
    def bounce(self) -> None:
        size = self.window.get_size()
        if self.position.x - self.radius <= 0 or self.position.x + self.radius > size[0]:
            self.inertia = maths.Vector2D(-self.inertia.x, self.inertia.y)
        
        if self.position.y - self.radius <= 0 or self.position.y + self.radius > size[1]:
            self.inertia = maths.Vector2D(self.inertia.x, -self.inertia.y)
    
    def is_colliding(self, other: 'Balle') -> bool:
        """
        Check if two balls collide.
        """
        distance: maths.Vector2D = maths.Vector2D(
            self.position.x - other.position.x, 
            self.position.y - other.position.y
        )
        # print("coll.")
        return distance.magnitude < float(other.radius + self.radius)     
    
    def collision(self, other: 'Balle') -> None:
        """
        Do collisions if positions
        """
        if self.is_colliding(other):
            tmp = self.inertia
            self.inertia = other.inertia
            other.inertia = tmp

