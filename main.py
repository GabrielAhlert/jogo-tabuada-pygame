import pygame, random, time
#Let's import the Player Class
from player import Player
from barrier import Barrier
from grass import Grass
from pygame import mixer

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 100, 100)
DARKRED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
DARKBLUE = (0, 0, 255)
DARKGREEN = (72,93,20)

speed = 2
posibleRange = (1,10)
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)


SCREENWIDTH=800
SCREENHEIGHT=600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Tabuada")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()


playerPlayer1 = Player(DARKBLUE, 60, 80, 70)
playerPlayer1.rect.x = 130
playerPlayer1.rect.y = SCREENHEIGHT - 100

playerPlayer2 = Player(DARKRED, 60, 80, 70)
playerPlayer2.rect.x = 530
playerPlayer2.rect.y = SCREENHEIGHT - 100

Barrier1 = Barrier(random.choice(colorList), 60, 80, -200)
Barrier1.rect.x = 50


Barrier2 = Barrier(random.choice(colorList), 60, 80, -200)
Barrier2.rect.x = 130


Barrier3 = Barrier(random.choice(colorList), 60, 80, -200)
Barrier3.rect.x = 210


Barrier4 = Barrier(random.choice(colorList), 60, 80, -200)
Barrier4.rect.x = 290


Barrier5 = Barrier(random.choice(colorList), 60, 80, -200 )
Barrier5.rect.x = 450


Barrier6 = Barrier(random.choice(colorList), 60, 80, -200)
Barrier6.rect.x = 530


Barrier7 = Barrier(random.choice(colorList), 60, 80, -200)
Barrier7.rect.x = 610


Barrier8 = Barrier(random.choice(colorList), 60, 80, -200)
Barrier8.rect.x = 690



# Add the Player to the list of objects
all_sprites_list.add(playerPlayer1)
all_sprites_list.add(playerPlayer2)
all_sprites_list.add(Barrier1)
all_sprites_list.add(Barrier2)
all_sprites_list.add(Barrier3)
all_sprites_list.add(Barrier4)
all_sprites_list.add(Barrier5)
all_sprites_list.add(Barrier6)
all_sprites_list.add(Barrier7)
all_sprites_list.add(Barrier8)

all_coming_BarriersLeft = pygame.sprite.Group()
all_coming_BarriersLeft.add(Barrier1)
all_coming_BarriersLeft.add(Barrier2)
all_coming_BarriersLeft.add(Barrier3)
all_coming_BarriersLeft.add(Barrier4)

all_coming_BarriersRight = pygame.sprite.Group()
all_coming_BarriersRight.add(Barrier5)
all_coming_BarriersRight.add(Barrier6)
all_coming_BarriersRight.add(Barrier7)
all_coming_BarriersRight.add(Barrier8)

numbersLeft = []
numbersRight = []
score=0

for Barrier in all_coming_BarriersLeft:
    number = random.randint(posibleRange[0],posibleRange[1])
    Barrier.setNumber(number)
    numbersLeft.append(number)

for Barrier in all_coming_BarriersRight:
    number = random.randint(posibleRange[0],posibleRange[1])
    Barrier.setNumber(number)
    numbersRight.append(number)

anwser = random.choice(numbersLeft) * random.choice(numbersRight)


#Allowing the user to close the window...
PlayerryOn = True
clock=pygame.time.Clock()
starttime = time.time() + 300.00
mixer.init() 
mixer.music.load("ambient.mp3") 
mixer.music.set_volume(0.7) 
mixer.music.play() 


grasses = pygame.sprite.Group()
for i in range(0,SCREENHEIGHT,50):
    grasses.add(Grass(i, -20, SCREENWIDTH, SCREENHEIGHT))
    grasses.add(Grass(i, 340, SCREENWIDTH, SCREENHEIGHT))
    grasses.add(Grass(i, 380, SCREENWIDTH, SCREENHEIGHT))
    grasses.add(Grass(i, 740, SCREENWIDTH, SCREENHEIGHT))
    






while PlayerryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                PlayerryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    PlayerryOn=False
                if event.key==pygame.K_d:
                    if playerPlayer1.rect.x < 290:
                        playerPlayer1.moveRight(80)
                elif event.key==pygame.K_a:
                    if playerPlayer1.rect.x > 50:
                        playerPlayer1.moveLeft(80)
                elif event.key==pygame.K_LEFT:
                    if playerPlayer2.rect.x > 450:
                        playerPlayer2.moveLeft(80)
                elif event.key==pygame.K_RIGHT:
                    if playerPlayer2.rect.x < 690:
                        playerPlayer2.moveRight(80)

        for Barrier in all_coming_BarriersLeft:
            Barrier.moveForward(speed)
        
        for Barrier in all_coming_BarriersRight:
            Barrier.moveForward(speed)
            
            
        if Barrier1.rect.y > SCREENHEIGHT-160:
            collisionsP1 = pygame.sprite.spritecollide(playerPlayer1, all_coming_BarriersLeft, False)[0].getNumber()
            collisionsP2 = pygame.sprite.spritecollide(playerPlayer2, all_coming_BarriersRight, False)[0].getNumber()
            if collisionsP1*collisionsP2 == anwser:
                score += 1
                speed += 0.1
                print("CORRECT")
            else:
                print("WRONG")
                if speed > 0.3:
                    speed -= 0.2
                else:
                    speed = 0.2
                print("speed: " + str(speed))
            print(collisionsP1*collisionsP2)
            numbersLeft = []
            for barrier in all_coming_BarriersLeft:
                number = random.randint(posibleRange[0],posibleRange[1])
                numbersLeft.append(number)
                barrier.repaint(random.choice(colorList))
                barrier.y = 0
                barrier.setNumber(number)
            numbersRight = []
            for barrier in all_coming_BarriersRight:
                number = random.randint(posibleRange[0],posibleRange[1])
                numbersRight.append(number)
                barrier.repaint(random.choice(colorList))
                barrier.y = 0
                barrier.setNumber(number)
            numberleft = random.choice(numbersLeft)
            numberright = random.choice(numbersRight)
            anwser = numberleft * numberright
    
            
        # #Game Logic
        # for Barrier in all_coming_BarriersLeft:
        #     Barrier.moveForward(speed)
        #     if Barrier.rect.y > SCREENHEIGHT:
        #         #Barrier.changeSpeed(random.randint(barrierSpeed, 100))
        #         Barrier.repaint(random.choice(colorList))
        #         Barrier.rect.y = -200
        #         Barrier.setNumber(random.randint(1,10))


        # for Barrier in all_coming_BarriersRight:
        #     Barrier.moveForward(speed)
        #     if Barrier.rect.y > SCREENHEIGHT:
        #         #Barrier.changeSpeed(random.randint(barrierSpeed, 100))
        #         Barrier.repaint(random.choice(colorList))
        #         Barrier.rect.y = -200
        #         Barrier.setNumber(random.randint(1,10))

        all_sprites_list.update()
        timeleftMin = int((starttime - time.time())/60)
        timeleftSec = int((starttime - time.time())%60)

        #Drawing on Screen
        screen.fill(DARKGREEN)

        
        #Draw The Road
        pygame.draw.rect(screen, GREY, [40,0, 320,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [120,0],[120,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [200,0],[200,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [280,0],[280,SCREENHEIGHT],5)

        #Draw The Second Road
        pygame.draw.rect(screen, GREY, [440,0, 320,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [520,0],[520,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [600,0],[600,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [680,0],[680,SCREENHEIGHT],5)

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)
        
        for grass in grasses:
            grass.updateAndDraw(screen, speed)

        # Draw the score and top score  
        pygame.draw.rect(screen, (0,0,0), [0,0, SCREENWIDTH,80])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(score),True,WHITE)
        screen.blit(text, [20, 10])
        # text = font.render("Top Score: " + str(10),True,WHITE)
        # screen.blit(text, [20, 40])
        
        # Draw the time left
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Tempo Restante: " + str(timeleftMin) + ":" + str(timeleftSec),True,WHITE)
        screen.blit(text, [20, 40])

        
        # Draw Rules to win match
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render("       X        = " + str(anwser),True,WHITE)
        screen.blit(text, (288, 20))
        pygame.draw.rect(screen, DARKBLUE, [300,20, 40,40])
        pygame.draw.rect(screen, DARKRED, [380,20, 40,40])


        #Refresh Screen
        pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit()