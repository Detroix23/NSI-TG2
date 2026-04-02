# -*- coding: utf-8 -*-
"""
@author: Noémie Exartier
"""

import pygame
import time
from pygame.locals import *
from random import randint

ecran = (640,480)
taille = 10

pygame.display.init()
fenetre = pygame.display.set_mode(ecran)
fenetre.fill([0,0,0])

class Balle :
    def __init__(self):
        self.x = randint(0,ecran[0])
        self.y = randint(0,ecran[1])       
        self.dx = randint(-5,5)
        self.dy = randint(-5,5)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.taille = taille
        
    def deplacer(self):
        # mouvement de la balle self
        self.x += self.dx
        self.y += self.dy         
            
    def dessiner(self):
        pygame.draw.circle(fenetre,self.color,(self.x,self.y),self.taille)
        
    
    def rebondir(self):
       # rebond de la balle self
        if self.x < self.taille or self.x > ecran[0]-self.taille :
            self.dx = -self.dx
        if self.y < self.taille or self.y > ecran[1]-self.taille :
            self.dy = -self.dy



continuer = True


b = Balle()

while continuer:
    fenetre.fill([0,0,0])
    b.rebondir()
    b.deplacer()
    b.dessiner()
    
    pygame.display.flip()   #Rafraîchissement de l'écran
    time.sleep(0.01)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Si l'utilisateur ferme la fenêtre
            pygame.display.quit()
            continuer = False
