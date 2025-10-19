"""
BALLS
window.py
"""

import random
import time
import pygame

import modules.colors as colors
import modules.maths as maths
import modules.balls as balls


def main(color_mode: colors.Mode) -> None:
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
        radius = random.randint(10, 50)
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
            color=colors.random_color(), 
            radius=radius
        ))
    
    # Main loop
    print("*Main loop started.*")
    while continuer:
        if color_mode == colors.Mode.EPILEPSY:
            screen.fill(colors.random_color())
        elif color_mode in [colors.Mode.FIXED, colors.Mode.GRADIENT]:
            screen.fill(back_color)
        
        for b in all_balls:
            if color_mode == colors.Mode.EPILEPSY:
                b.color = colors.random_color()    
            elif color_mode == colors.Mode.GRADIENT:
                b.color.increment()
            
            b.bounce()
            b.move()
            b.draw()
            for b2 in all_balls:
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
        
    print("*Main loop ended.*")