from typing import Any
import pygame

WHITE = (255, 255, 255)

class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print ('Unable to load spritesheet image:'), filename
            raise SystemExit(message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
        
        
 
class Player(pygame.sprite.Sprite):
    #This class represents a Player. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height, speed, sprite_location):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the Player, and its x and y position, width and height.
        # Set the background color and set it to be transparent
 
        #Initialise attributes of the Player.
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed
 
 
        # Instead we could load a proper picture of a Player...
        ss = spritesheet(sprite_location)
        self.images = ss.images_at([(0, 512, 64, 64), (64, 512, 64, 64), (128, 512, 64, 64), (192, 512, 64, 64), (256, 512, 64, 64), (320, 512, 64, 64), (384, 512, 64, 64), (448, 512, 64, 64), (512, 512, 64, 64)], colorkey = -1)

        self.image = self.images[0]
        self.current_image = 0
        
        self.auxTimer = 0
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.auxTimer == 5:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
            self.auxTimer = 0
        else:
            self.auxTimer += 1
        return super().update(*args, **kwargs)
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
 
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])