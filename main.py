import pygame, random, time
#Let's import the Player Class
from player import Player
from barrier import Barrier

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

speed = 2
posibleRange = (1,10)
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)


SCREENWIDTH=800
SCREENHEIGHT=600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tabuada")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()


playerPlayer1 = Player(DARKBLUE, 60, 80, 70)
playerPlayer1.rect.x = 130
playerPlayer1.rect.y = SCREENHEIGHT - 100

playerPlayer2 = Player(DARKRED, 60, 80, 70)
playerPlayer2.rect.x = 530
playerPlayer2.rect.y = SCREENHEIGHT - 100

Barrier1 = Barrier(random.choice(colorList), 60, 80)
Barrier1.rect.x = 50
Barrier1.rect.y = 200.0

Barrier2 = Barrier(random.choice(colorList), 60, 80)
Barrier2.rect.x = 130
Barrier2.rect.y = 0.0

Barrier3 = Barrier(random.choice(colorList), 60, 80)
Barrier3.rect.x = 210
Barrier3.rect.y = 0

Barrier4 = Barrier(random.choice(colorList), 60, 80)
Barrier4.rect.x = 290
Barrier4.rect.y = 0

Barrier5 = Barrier(random.choice(colorList), 60, 80)
Barrier5.rect.x = 450
Barrier5.rect.y = 0

Barrier6 = Barrier(random.choice(colorList), 60, 80)
Barrier6.rect.x = 530
Barrier6.rect.y = 0

Barrier7 = Barrier(random.choice(colorList), 60, 80)
Barrier7.rect.x = 610
Barrier7.rect.y = 0

Barrier8 = Barrier(random.choice(colorList), 60, 80)
Barrier8.rect.x = 690
Barrier8.rect.y = 0


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

while PlayerryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                PlayerryOn=False
            elif event.type==pygame.KEYDOWN:
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
                if speed > 0.2:
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
        screen.fill(GREEN)

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