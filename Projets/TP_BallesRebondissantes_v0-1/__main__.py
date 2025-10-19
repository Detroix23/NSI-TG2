import random
import time
import math

import pygame
from pygame.locals import *


ecran = (640,480)
taille = 10

pygame.display.init()
fenetre: pygame.Surface = pygame.display.set_mode(ecran)
fenetre.fill([0,0,0])

class Vector2D:
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
        
class Balle:
    window: pygame.Surface
    position: Vector2D
    inertia: Vector2D
    color: tuple[int, int, int]
    
    def __init__(
        self,
        window, 
        position: Vector2D,
        inertia: Vector2D, 
        color: tuple[int, int, int],
        radius: int,
    ) -> None: 
        self.window = window
        self.position = position
        self.inertia = inertia
        self.color = color
        self.radius = radius
    
    def __repr__(self) -> str:
        return f"Balle(x={self.position.x}, y={self.position.y}, dx={self.inertia.x}, dy={self.inertia.y})"
        
    def deplacer(self):
        self.position = self.position + self.inertia
        
            
    def dessiner(self):
        pygame.draw.circle(
            self.window, 
            self.color, 
            self.position.__tuple__(), 
            self.radius
        )
    
    def rebondir(self):
        size = self.window.get_size()
        if self.position.x - self.radius <= 0 or self.position.x + self.radius > size[0]:
            self.inertia = Vector2D(-self.inertia.x, self.inertia.y)
        
        if self.position.y - self.radius <= 0 or self.position.y + self.radius > size[1]:
            self.inertia = Vector2D(self.inertia.x, -self.inertia.y)
    
    def is_colliding(self, other: 'Balle') -> bool:
       distance: Vector2D = Vector2D(
           self.position.x - other.position.x, 
           self.position.y - other.position.y
       )
       print("coll.")
       return distance.magnitude < float(other.radius)     
    
    def collision(self, other):
        distance: Vector2D = Vector2D(
            self.position.x - other.position.x, 
            self.position.y - other.position.y
        )
        if distance.magnitude < float(other.radius + self.radius):
            print("coll.")
            tmp = self.inertia
            self.inertia = other.inertia
            other.inertia = tmp


def random_color() -> tuple[int, int, int]:
    return tuple(random.randint(0, 255) for _ in range(3))
    
continuer = True

# Balles
balls: list[Balle] = list()
for _ in range(4):
    radius = random.randint(10, 50)
    balls.append(Balle(
        fenetre,
        Vector2D(
            random.randint(2 * radius, ecran[0] - 2 * radius),
            random.randint(2 * radius, ecran[0] - 2 * radius),
        ),
        Vector2D(
            random.randint(1, 10),
            random.randint(1, 10),
        ),
        random_color(), 
        radius
    ))

while continuer:
    fenetre.fill(random_color())
    for b in balls:
        b.rebondir()
        b.deplacer()
        b.dessiner()
        for b2 in balls:
            b.color = random_color()
            if b2 is not b:
                b.collision(b2)
                
            
    # Rafraîchissement de l'écran
    pygame.display.flip()  
    time.sleep(0.02)
    
    for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:  
            pygame.display.quit()
            continuer = False
