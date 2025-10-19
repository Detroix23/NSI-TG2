"""
BALLS
window.py
"""

import random
import time
import pygame
from enum import Enum

import modules.colors as colors
import modules.maths as maths
import modules.balls as balls


class Collide(Enum):
    NORMAL = 0
    SPLIT = 1


def main(color_mode: colors.Mode, collide_mode: Collide = Collide.NORMAL) -> None:
    """
    Main window execution.
    """
    size: tuple[int, int] = (1920,1080)
    back_color: tuple[int, int, int] = (0, 0, 0)
    
    pygame.display.init()
    screen: pygame.Surface = pygame.display.set_mode(size, pygame.FULLSCREEN, vsync=1)
    screen.fill(back_color)
    
    continuer = True
    
    # Balles
    all_balls: list[balls.Balle] = list()
    quantity: int = random.randint(5, 20)
    
    for _ in range(quantity):
        radius: int = random.randint(10, 50)
        color: colors.Color
        if color_mode == colors.Mode.INFECTION:
            color = colors.Infected.NO
        else:
            color = colors.random_color()
        
        all_balls.append(balls.Balle(
            screen,
            position=maths.Vector2D(
                random.randint(2 * radius, size[0] - 2 * radius),
                random.randint(2 * radius, size[1] - 2 * radius),
            ),
            inertia=maths.Vector2D(
                random.randint(1, 10),
                random.randint(1, 10),
            ),
            color=color, 
            radius=radius
        ))
    
    # Starting infection.
    if color_mode == colors.Mode.INFECTION:
        all_balls[0].color = colors.Infected.YES
    
    # Main loop
    print("*Main loop started.*")
    while continuer:
        # Clear each frame.
        if color_mode == colors.Mode.EPILEPSY:
            screen.fill(colors.random_color())
        else:
            screen.fill(back_color)
        
        for id1, b in enumerate(all_balls):
            if color_mode == colors.Mode.EPILEPSY:
                b.color = colors.random_color()    
            elif color_mode == colors.Mode.GRADIENT:
                b.color.increment()
            
            b.bounce()
            b.move()
            b.draw()
            for id2, b2 in enumerate(all_balls):
                if b2 is b:   
                    continue
                if not b.is_colliding(b2):
                    continue
                
                b.collision(b2)
                # Prone to infection.
                if (b.color == colors.Infected.YES
                    or b2.color == colors.Infected.YES
                ):
                    b.color = colors.Infected.YES
                    b2.color = colors.Infected.YES
                
                if (collide_mode == Collide.SPLIT):
                    # New ball child.
                    print("New ball child")
                    all_balls.append(balls.Balle(
                        screen,
                        position=maths.Vector2D(
                            b2.position.x,
                            b.position.y,
                        ),
                        inertia=maths.Vector2D(
                            b.inertia.x,
                            b2.inertia.y,
                        ),
                        color=colors.Base.WHITE, 
                        radius=(b.radius + b2.radius) // 2
                    ))
                    
            
        # Rafraîchissement de l'écran
        pygame.display.flip()  
        time.sleep(0.02)
        
        for event in pygame.event.get():
            # Si l'utilisateur ferme la fenêtre
            if event.type == pygame.QUIT:  
                pygame.display.quit()
                continuer = False
        
    print("*Main loop ended.*")