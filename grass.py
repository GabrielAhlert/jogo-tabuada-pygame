from typing import Any
import pygame
import random

class Grass(pygame.sprite.Sprite):
    #This class represents a Grass. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, starty=0, startx=0, width=800, height=600):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Instead we could load a proper picture of a Grass...
        image = pygame.image.load("1987.png").convert_alpha()
        self.image = pygame.transform.scale(image, (80, 80))       
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
        starty += random.randint(0, 20)
        
        #Initialise attributes of the Grass.
        self.x = startx
        self.y = starty
        self.rect.y = self.y
        self.rect.x = self.x
        self.width = width
        self.height = height
        
        
        
    def moveForward(self, speed):
        if self.y > self.height:
            self.y = 0
        self.y += speed
        self.rect.y = self.y
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def updateAndDraw(self, screen, speed):
        self.moveForward(speed)
        self.draw(screen)
        
    
        

        
    
    
        
