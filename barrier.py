import pygame
WHITE = (255, 255, 255)
 
class Barrier(pygame.sprite.Sprite):
    #This class represents a Barrier. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height, speed, number):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the Barrier, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        #Initialise attributes of the Barrier.
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed
 
        # Draw the Barrier (a rectangle!)
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
 
        # Instead we could load a proper picture of a Barrier...
        # self.image = pygame.image.load("Barrier.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        #Write the number of the barrier on it
        

    def setNumber(self, number):
        self.number = number
        font = pygame.font.SysFont('Arial', 26)
        text = font.render(str(self.number), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.width // 2, self.height // 2)
        self.image.blit(text, textRect)

    def getNumber(self):
        return self.number

 
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